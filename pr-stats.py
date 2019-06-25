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
            self.gh_dump=requests.get(self.gh_dump.links['next']['url'],
                                      auth=(username, passwd)) # walk through pages
            self.gh_local.extend(self.gh_dump.json())


class GHTokenSurfer(GHsurfer):
    """ dumping provided github repo with token"""
    def __init__(self, url, token):
        self.gh_dump = requests.get(url, headers={"Authorization": token})
        self.gh_local = self.gh_dump.json()
        while 'next' in self.gh_dump.links.keys():
            self.gh_dump=requests.get(self.gh_dump.links['next']['url'])
                                      #headers={"Authorization": token}) # walk through pages
            self.gh_local.extend(self.gh_dump.json())


if __name__ == "__main__":
    line = argparse.ArgumentParser()
    url = "https://api.github.com/repos/Corwind/termite-install/pulls"
    token = "69b3fc5bc442f55ad002dc9bd154fc0d98932d5a"
    token = "token {}".format(token)

    #username = input("Type username: ")

    username = "derafer"
    passwd = ""
    #passwd = getpass.getpass()
    a1 = GHUserSurfer(url, username, passwd)

