# playwright-indra
```
$ Depends on pytest-playwright

$ pip install pytest-playwright

$ pip install pytest-bdd

$ playwright install
```
Assignment from company to create testing automation project in python using cucumber, pytest-bdd and playwright
I was testing Azet.sk email service in this project.

Folders hierarchy:
```
├───features
│    └──email.feature - cucumber file
│    └──test_email.py - pytest-bdd test cases based by email.feature
│
├───pages
│    └──inbox_page.py - inbox page playwright functions
│    └──login_page.py - login page playwright functions
│    └──main_page.py - home page playwright functions
│    └──message_page.py - message page playwright functions
│
├───resources
│    └──attachment.txt
│
└───workflows
     └──email_workflow.py - python file to organize page functions into common functions
```
When you are launching the project don't forget to use additional arguments when building:
```
--headed --base-url https://www.azet.sk/
```
and environmental variables:
```
username=<your_username>;password=<your_password>
```
where you fill out your username and password after you register yourself into azet.sk

It was my first time doing such project as I briefly went throught python in school and I also never worked with pytest-dbb and playwright. It was a nice experience.

In the start I started creating test based on cucumber generator of suitcases but in the end I was grouping them together.
