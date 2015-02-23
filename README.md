# Queen's Online Timetable Grabber
## A shell script to grab timetables from Queen's Online and insert them into Google Calendar

## Instructions
* Ensure you're running Ubuntu with Python 2.7 and curl installed (other distributions are available although, YMMV)
* Open run.sh and add your Queen's user and password to the variables at the top of the file
* authenticate your google account using the OAuth window that pops up in your web browser
* Paste the authentication code into your terminal window and press Enter
* Choose the calendar you wish to add your events to by typing the correct number in your terminal window
* That's it!

### To Do
* ~~Add option to select calendar to append events to~~
* ~~Append events to that calendar~~
* Add means by which to read set of configurations (e.g. default calendar to add to)
* Refresh auth token so don't have to keep opening new browser window each time the script runs

###Notes.
* [Login page for Queen's Online](https://home.qol.qub.ac.uk/)
* [URL for JSON timetable document](https://home.qol.qub.ac.uk/_layouts/qol.home.timetable/webservice.ashx)
* [Google Calendar API](https://developers.google.com/google-apps/calendar/)
* [OAuth docs Google](https://developers.google.com/accounts/docs/OAuth2WebServer)
