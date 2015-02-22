#!/bin/bash

username=ads/
password=

echo $username
echo $password

curl --ntlm -A "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3" -u $username:$password https://home.qol.qub.ac.uk/_layouts/qol.home.timetable/webservice.ashx -o timetable.json --verbose
