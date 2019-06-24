# TODO script to get PR(Pull Request) statistics from GitHub.
# Usage:
# pr-stats [options] <user> [<repo>]
# pr-stats --version
# pr-stats (-h | --help)
# TODO -h | --help Show help.
# TODO -v | --version Print the program's installed version
# TODO -s | --base-stat Basic statistics about merged/closed rate.
# TODO --day-opened Number of days opened.
# TODO --comments Number of comments created.
# TODO --day ? Day of the week opened.
# TODO Hour of the day opened.
# TODO --week-opened Week opened.
# TODO -u | --user User who opened.
# TODO --closed-by User who closed.
# TODO --labels Attached labels.
# TODO Number of lines added.
# TODO Number of lines deleted.
# TODO Option to consider only pull requests opened on or after this date.
# TODO Only consider pull requests opened before this date.
# argparse https://docs.python.org/3.7/howto/argparse.html
# requests http://docs.python-requests.org/en/master/user/quickstart/
# getpass https://docs.python.org/3.7/library/getpass.html
# configparser https://docs.python.org/3/library/configparser.html

import argparse
import requests
import getpass
import configparser
import json

# TODO add class for storing all dump and methods for processing this dump

line = argparse.ArgumentParser()
url = "https://api.github.com/repos/alenaPy/devops_lab/pulls"
token = "06d3a96a3c90b8acd0012555546a84d3b61db745"
token = "token {}".format(token)

gh_dump = requests.get(url, headers={"Authorization": token})
gh_local = gh_dump.json()

while 'next' in gh_dump.links.keys():
  gh_dump=requests.get(gh_dump.links['next']['url'], headers={"Authorization": token}) # how its work
  gh_local.extend(gh_dump.json())
print(len(gh_local))
