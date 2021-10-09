<div align="center">
<h1>Timetable updater</h1>
<hr>
<strong>A tiny projects that keeps my timetable up to date.</strong><br><br>

<img src="https://img.shields.io/github/workflow/status/mathisburger/timetable-updater/build?style=for-the-badge">
<img src="https://img.shields.io/github/license/mathisburger/timetable-updater?style=for-the-badge"> 
<img src="https://img.shields.io/github/v/release/mathisburger/timetable-updater?style=for-the-badge">
</div>
<hr>
<div align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" height="128"/>
<img src=".media/cal.png" height="128" />
</div>

# Project information

The timetable updater is a small project from me, built a google calendar
that contains all of my school lessons. It`s just a simple script, that can
be executed as a crobjob or something like this. It fetches automatically all
updates from my schools website and updates them in my google calendar.

# Customize for yourself

It is kinda tricky to use this repo for your personal purposes, because
it is built and adapted for my schools infrastructure and only for
google calendars.
Nevertheless, it is possible to customize it a little bit. You can play 
arround with the environment variables.

| variable              	| explaination                                                                                                                  	|
|-----------------------	|-------------------------------------------------------------------------------------------------------------------------------	|
| SUBSTITUTION_PLAN_URL 	| This is the url that points directly on the substitution plan of your school. But it requires a special school infrastructure 	|
| CLASS_NAME            	| The name of your class, that shows up in the substitution plan                                                                	|
| CALENDAR_ID           	| The id of your google calendar that contains all your lessons                                                                 	|


# Installation & setup

If you want to setup this installation yourself you have to follow some quick steps.

1. Enable the google calendar API
    - Go to https://console.cloud.google.com/
    - Create a new project
    - enable the calendar API
    - create a new OAuth2.0 Client
    - download the `credentials.json` of the client

2. Paste the `credentials.json` into your directory or attach it to the docker volume, if you are using a docker container
3. Start your script or docker container
4. Click on the link in the logs. You have to authorize your application once
5. Start the application again
6. Now feel free to configure a crobjob or something else for it.

# Docker info

I recommend using `docker-compose` for setting up your docker volumes and services,
because it provides a much cleaner way of setting up everything than using
long commands filled with arguments.

