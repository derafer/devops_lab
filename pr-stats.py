# TODO script to get PR(Pull Request) statistics from GitHub.
# Usage:
# pr-stats [options] <user> [<repo>]
# pr-stats --version
# pr-stats (-h | --help)
# DONE -h | --help Show help.
# TODO -v | --version Print the program's installed version
# TODO -s | --base-stat Basic statistics about merged/closed rate.
# TODO --day-opened Number of days opened.
# TODO --comments Number of comments created.
# TODO --day ? Day of the week opened.
# TODO --week-opened Week opened.
# TODO --open-by User who opened.
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


class GHsurfer:
    """ base class for methods"""
    def printraw(self):
        print(*self.gh_local, sep="\n")


class GHUserSurfer(GHsurfer):
    """ dumping provided github repo with username and password"""
    def __init__(self, url, username, passwd):
        self.gh_dump = requests.get(url, auth=(username, passwd))
        self.gh_local = self.gh_dump.json()
        while 'next' in self.gh_dump.links.keys():
            self.gh_dump=requests.get(self.gh_dump.links['next']['url'])
                                      #auth=(username, passwd)) # walk through pages
            self.gh_local.extend(self.gh_dump.json())


class GHTokenSurfer(GHsurfer):
    """ dumping provided github repo with token"""
    def __init__(self, url, token):
        self.gh_dump = requests.get(url, headers={"Authorization": token})
        self.gh_local = self.gh_dump.json()
        while 'next' in self.gh_dump.links.keys():
            self.gh_dump=requests.get(self.gh_dump.links['next']['url'], headers={"Authorization": token})
            self.gh_local.extend(self.gh_dump.json())


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("config.ini")
    token_conf = config.get("common", "token")
    line = argparse.ArgumentParser(description="script to get PR(Pull Request) statistics from GitHub")
    line.add_argument("--user", help="user for work with git")
    line.add_argument("--token", "-t", help="token for work with git")
    line.add_argument("url", help="url for parsing")
    args = line.parse_args()
    if args.user is not None:
        username = args.user
    elif config.has_option("common", "username"):
        username = config.get("common", "username")
    else:
        print("Please provide username")

    if args.token is not None:
        token = args.token
    elif config.has_option("common", "token"):
        token = config.get("common", "token")
    else:
        print("Please provide a token")
    token = "token {}".format(token)
    #url = "https://api.github.com/repos/Corwind/termite-install/pulls"
    #username = input("Type username: ")

    #username = "derafer"
    #passwd = getpass.getpass()