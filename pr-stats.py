#!/usr/bin/env python
# script to get PR(Pull Request) statistics from GitHub.
# Usage:
# pr-stats [options] <user> [<repo>]
# pr-stats --version
# pr-stats (-h | --help)
# -h | --help Show help.
# -v | --version Print the program's installed version
# DONE -s | --base-stat Basic statistics about merged/closed rate.
# --day-opened Number of days opened.
# DONE --comments Number of comments created.
# --day ? Day of the week opened.
# --week-opened Week opened.
# DONE --open-by User who opened.
# DONE --closed-by User who closed.
# DONE --labels Attached labels.
# Number of lines added.
# Number of lines deleted.
# Option to consider only pull requests opened on or after this date.
# Only consider pull requests opened before this date.
# argparse https://docs.python.org/3.7/howto/argparse.html
# requests http://docs.python-requests.org/en/master/user/quickstart/
# getpass https://docs.python.org/3.7/library/getpass.html
# configparser https://docs.python.org/3/library/configparser.html

import argparse
import requests
import getpass
import configparser
# import json


class GHsurfer:
    """ base class for methods"""
    def print_base_stats(self):
        for i in self.gh_local:
            print("PR name is '%s' from '%s'" % (i['title'], i['user']['login']))
            print("state: ", i['state'], )
            print("created: ", i['created_at'])
            print("\n")

    def print_openby(self):
        for i in self.gh_local:
            print("PR number '%s' openby '%s'" % (i['number'], i['user']['login']))

    def print_closeby(self):

        for i in self.gh_local:
            if i['state'] == 'closed':
                print("PR number '%s' closed by '%s'" % (i['number'], i['user']['login']))

    def print_labels(self):
        for i in self.gh_local:
            labels = ""
            for b in i['labels']:
                if 'name' in b:
                    labels += b['name']
            print("Labels for PR in '%s' (by '%s'): %s" % (i['title'], i['user']['login'], labels))

    def print_labels_needwork(self):
        for i in self.gh_local:
            labels = ""
            for b in i['labels']:
                if 'name' in b:
                    labels += b['name']
            if 'needs work' in labels:
                print("PR with 'need work' labels '%s' %s" % (i['title'], i['url']))

    def dump_raw(self, url):
        """ dont work with password, because security"""
        # probably best is add this to gh_local['comments_url'], but not today :)
        raw = requests.get(url, headers={"Authorization": self.token})
        comments_json = raw.json()
        return comments_json

    def print_comments(self):
        for i in self.gh_local:
            c = self.dump_raw(i['comments_url'])
            if len(c) > 0:
                print(i['title'], "has %i comments:" % len(c))
                for fraze in c:
                    print(fraze['body'])

    def printraw(self):
        print(*self.gh_local, sep="\n")


class GHUserSurfer(GHsurfer):
    """ dumping provided github repo with username and password"""
    def __init__(self, url, username):
        self.gh_dump = requests.get(url, auth=(username, getpass.getpass()))
        self.gh_local = self.gh_dump.json()
        while 'next' in self.gh_dump.links.keys():
            self.gh_dump = requests.get(self.gh_dump.links['next']['url'])
            # auth=(username, passwd)) walk through pages
            self.gh_local.extend(self.gh_dump.json())


class GHTokenSurfer(GHsurfer):
    """ dumping provided github repo with token"""
    def __init__(self, url, token):
        self.token = token
        self.gh_dump = requests.get(url, headers={"Authorization": token})
        self.gh_local = self.gh_dump.json()
        while 'next' in self.gh_dump.links.keys():
            self.gh_dump = requests.get(
                self.gh_dump.links['next']['url'],
                headers={"Authorization": token}
            )
            self.gh_local.extend(self.gh_dump.json())


if __name__ == "__main__":

    line = argparse.ArgumentParser(
        description="Script to get PR(Pull Request) statistics from GitHub.  \
                    For best experience and security, pls use token",
        formatter_class=argparse.RawTextHelpFormatter
    )
    line.add_argument(
        "url", help="url for parsing \n"
                    "url must be like: \n"
                    "https://api.github.com/repos/USERNAME/REPONAME/pulls"
    )
    line.add_argument("--user", help="user for work with git")
    line.add_argument("--token", "-t", help="token for work with git")
    line.add_argument("--base-stat", help="print basic stat", action="store_true")
    line.add_argument("--comments", help="print all comments from PR", action="store_true")
    line.add_argument("--label", help="print labels for PR", action="store_true")
    line.add_argument("--open-by", help="show title of PR and issuer", action="store_true")
    line.add_argument("--closed-by", help="show title of PR and who close", action="store_true")
    line.add_argument("--label-needwork", help="specific option for devopslab PR",
                      action="store_true")

    args = line.parse_args()

    config = configparser.ConfigParser()
    config.read("config.ini")
    token_conf = config.get("common", "token")
    url = args.url
    url += "?state=all"
    if args.token is not None:
        token = args.token
        token = "token {}".format(token)
        a1 = GHTokenSurfer(url, token)
    elif config.has_option("common", "token") and not config.get("common", "token") == '':
        token = config.get("common", "token")
        token = "token {}".format(token)
        a1 = GHTokenSurfer(url, token)
    elif args.user is not None:
        username = config.get("common", "username")
        a1 = GHUserSurfer(url, username)
    elif config.has_option("common", "username") and not config.get("common", "username") == '':
        username = config.get("common", "username")
        a1 = GHUserSurfer(url, username)
    else:
        print("Please, provide token either username to work with program")
        print("For best experience and security, pls use token")
        quit()

    if args.comments:
        a1.print_comments()
    if args.label:
        a1.print_comments()
    if args.label_needwork:
        a1.print_labels_needwork()
    if args.open_by:
        a1.print_openby()
    if args.base_stat:
        a1.print_base_stats()
    if args.closed_by:
        a1.print_closeby()
