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

# get the calendar list from calendar_list.json
cal_list=json.load(open('calendar_list.json'))['items']

#create dict of id-name pairs
calendar_dict = dict()
for item in cal_list:
    key = item['id']
    value = item['summary']
    calendar_dict[key] = value

print("Type the number of the calendar you want to add your timetable to:")
# print calendar names
for i in range(0,len(calendar_dict)):
    print(str(i)+': '+calendar_dict.values()[i])

calendar_index = raw_input("Type a number\n")
calendar_id = calendar_dict.keys()[int(calendar_index)]
calendar_name = calendar_dict.values()[int(calendar_index)]
print("Uploading timetable to '"+calendar_name+"'")

chosen_cal_file = open('chosen_calendar_id.txt', 'w')
chosen_cal_file.write(calendar_id)
chosen_cal_file.close()
