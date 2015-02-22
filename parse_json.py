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
import json
import pprint
import datetime

def convert_date(the_date, the_time):
    cat_date_time = the_date+' '+the_time
    # example date to convert from:
    # "05/03/2015 10:00"
    # example date to convert to:
    # "2015-03-05T10:00.000"
    return datetime.datetime.strptime(cat_date_time,
            '%d/%m/%Y %H:%M').isoformat('T')

json_data=open('timetable.json')

data = json.load(json_data)

# print out all the dates
days = data['Days']
# create dict with expected google calendar key value pairs

pp = pprint.PrettyPrinter(indent=4)
data_list = list()
for day in days:
    # multiple activities in a day
    if 'Date' in day:
        todays_date = day['Date']
        for activity in day['Activities']:
            dat = dict()
            dat['summary'] = activity['ModuleCode']+' '+activity['ActivityType']
            dat['location'] = activity['LocationName']
            
            dat['start'] = dict()
            dat['start']['dateTime'] = convert_date(todays_date, activity['StartTime'])
            dat['start']['timeZone'] = "Europe/London"

            dat['stop'] = dict()
            dat['stop']['dateTime'] = convert_date(todays_date, activity['EndTime'])
            dat['stop']['timeZone'] = "Europe/London"
            data_list.append(dat)

            json_dat = json.JSONEncoder().encode(dat)
            pp.pprint(json_dat)
            print('\n')

json_data.close()
