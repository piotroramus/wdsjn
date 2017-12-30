# WdSJN Project

## About

This project aims to find associations for some words by implementing Wettle & Rapp algorithm.
These findings are then compared with a common words' stimuli given by humans.

## Requirements
 - `Python 2`
 - `PLP library`
 
## Running in virtualenv

### Install virtualenv

`pip install virtualenv`

### Create virtualenv for a project

`cd wdsjn_path`
`virtualenv -p /usr/bin/python2.7 wdsjn`

### Activate the virtualenv

`source wdsjn/bin/activate`

### Install requirements

`pip install -r requirements.txt`

### When you are done

`deactivate`

## Running tests:

`pytest test/`