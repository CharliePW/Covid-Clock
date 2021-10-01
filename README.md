# CA3 Covid Clock


## Introduction

This  project is meant for the general public. It's is a web page that displays the Covid cases in your local
area, displays the weather in your local area, as well as the top news stories in the country. You can also  schedule alarms for anytime within the day.


## Prerequisites

This project is written with python 3.9, so the user will need this version.
The modules used in this project are: flask, sched, pyttsx3, time, logging, requests and json
If the user hasn't already, he/she will need to download these using 'pip install <module>' in the terminal of command prompt.
This project uses the restful APIs, "http://api.openweathermap.org", "https://newsapi.org" and "https://api.coronavirus.data.gov.uk" and the user will need to register for their own api key for the weather and news api.


## Installation

There will be a setup.py file to help with the setup and installation of the packages and modules in this project


## Testing

There is a package in the CA3 Covid Clock called tests that runs tests for each function in each module. First you must download pytest with 'pip install pytest' then run the tests by typing in the command line
'pytest <module>'.


## How to run the code

In the 'app' directory, type 'python main.py' or with mac 'python3 main.py'. This will send an HTML request and you'll be able to find the ip address in the log file 'sys.log'


## Details

Author: Charles Pearman-Wright (c)

Licence: MIT License

Link to github: ** enter link **
