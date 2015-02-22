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

json_data.close()
