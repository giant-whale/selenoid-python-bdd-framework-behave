# Python BDD framework for Selenoid
This is a python BDD (Behave) framework (with PageObject) for Selenoid hub, replacement of Selenium hub. 

Read more about Selenoid — https://aerokube.com/selenoid/
Read more about Behave — https://behave.readthedocs.io/

## Requirements
Python 3.8

## Installation
1. Follow this guide to install and run Selenoid — https://aerokube.com/selenoid/latest/
2. Download Docker images with browsers for Selenoid. If you want to use VNC option, you have to download VNC versions too;
3. Create new virtual environment and use package manager pip to install all requirements: ```pip install -r requirements.txt```;

## (Optional) Configure your IDE (Pycharm)
For running tests in debug mode, create new configuration:
1. Run > Edit Configurations
2. Add New Configuration > Python
3. Fill fields: 
```
Name = Behave
Script Path = selenoid-python-bdd-framework-behave/.env/lib/python3.8/site-packages/behave/__main__.py
```
For Script Path it's better to use files explorer button and locate your virtual environment behave `__main__.py`

## Configuration
Before running tests, change `SELENOID_REMOTE_URL` variable in `core/settings.py` to your Selenoid address.

## Browsers
List of available browsers in `core/browsers.py`. To add and use more browsers, check Selenoid documentation – https://aerokube.com/selenoid/latest/#_browser_images

## Mobile Emulation
Mobile emulation is available only for Google Chrome. 

Usage:  

To add more mobile devices:
1. ...
2. Add new devices in `core/mobile_emulation.py`;
3. ... 

## Run your tests
Multiple threads:
- Single-thread — execute command `behave` to run all tests in 1 thread;
- Multi-thread — execute command ...

Select browser:
- Execute command `behave -D browser=chrome` to run all tests using Google Chrome. Also, it's declared as default browser, so there is no need to use this command — you can use `behave` instead;
- Execute command `behave -D browser=firefox` to run all tests using Mozilla Firefox;

Generate JUnit report:
- Execute command `behave --junit` to run all tests and generate JUnit report files in directory `./reports`.