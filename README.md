# Python BDD framework for Selenoid
This is a python BDD (Behave) framework (with PageObject) for Selenoid hub, replacement of Selenium hub. 

This framework support multithreading running.

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
Script Path = selenoid-python-bdd-framework-behave/behave_runner.py
```
For Script Path it's better to use files explorer button and locate your virtual environment behave `__main__.py`

## Configuration
Before running tests, change `SELENOID_REMOTE_URL` variable in `core/settings.py` to your Selenoid address.

## Browsers
List of available browsers in `core/browsers.py`. To add and use more browsers, check Selenoid documentation – https://aerokube.com/selenoid/latest/#_browser_images

## Mobile Emulation
Mobile emulation is available only for Google Chrome. 

Usage: write new feature name with `Mobile - ` at the start — it will set mobile emulation.

Example:

`Mobile - check productivity` will run with mobile emulation.

`Check productivity on mobile` will run without mobile emulation (desktop mode, by default). 

To add more mobile devices:
1. Add new devices in `core/mobile_emulation.py`;
2. Add new keywords in `features/environment.py` and your features. 

## Run your tests
Multiple threads:
- Single-thread — execute command `python behave_runner.py` to run all tests in 1 thread;
- Multi-thread — execute command `python behave_runner.py --threads=5` to run all tests in 5 threads — 1 thread per feature.

Select browser:
- Execute command `python behave_runner.py -D browser=chrome` to run all tests using Google Chrome. Also, it's declared as default browser, so there is no need to use this command — you can use `behave` instead;
- Execute command `python behave_runner.py -D browser=firefox` to run all tests using Mozilla Firefox;

Generate JUnit report:
- Execute command `python behave_runner.py --junit` to run all tests and generate JUnit report files in directory `./reports`.

## Human-readable report from JUnit XML
1. Install using pip junit2html — `pip install junit2html`
2. Run command `junit2html junit_report_file.xml junit_humanreadable_report.html`
