#!/bin/bash

username=ads/
password=

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

curl -H "Authorization: Bearer $access_token" https://www.googleapis.com/calendar/v3/users/me/calendarList

rm access_token.txt
rm timetable.json
