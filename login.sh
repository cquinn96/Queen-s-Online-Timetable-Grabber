#    Queen's Online Timetable Grabber - 
#        A Shell Script to grab timetables from Queen's 
#        Online and insert them into Google Calendar
#
#    Copyright (C) 2015 Michael J. Jones
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#!/bin/bash

username=ads/40137949
password=43JOKY5N17

echo $username
echo $password

curl --ntlm -A "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3" -u $username:$password https://home.qol.qub.ac.uk/_layouts/qol.home.timetable/webservice.ashx -o timetable.json --verbose

xdg-open "https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=574687958685-qh4ilk1uq1f80jc5qsoavsv3ccq64df8.apps.googleusercontent.com&scope=https://www.googleapis.com/auth/calendar&redirect_uri=urn:ietf:wg:oauth:2.0:oob" &

echo "\n\n\n\nPlease copy authorisation code here."
read auth_code

# now we need to get the token! ^_^
curl -X POST https://accounts.google.com/o/oauth2/token \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "code=$auth_code" \
    -d "client_id=574687958685-qh4ilk1uq1f80jc5qsoavsv3ccq64df8.apps.googleusercontent.com" \
    -d "client_secret=AXdvd3szV01ohOemWkdGxaVp" \
    -d "redirect_uri=urn:ietf:wg:oauth:2.0:oob" \
    -d "grant_type=authorization_code" -o access_token.txt

access_token=`python extract_access_token.py`

curl -H "Authorization: Bearer $access_token" https://www.googleapis.com/calendar/v3/users/me/calendarList > calendar_list.json

python choose_calendar.py

chosen_cal_id=`cat chosen_calendar_id.txt`
echo "chosen calendar id is $chosen_cal_id"

# now add calendar events one by one

python parse_json.py | xargs -L 1 -I %json% curl -X POST \
    -H "Authorization: Bearer $access_token" \
    -H "Content-Type: application/json" \
    -d '%json%' \
    https://www.googleapis.com/calendar/v3/calendars/$chosen_cal_id/events
