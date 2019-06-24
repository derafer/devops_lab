# TODO script to get PR(Pull Request) statistics from GitHub.
# TODO Show help.
# TODO Print the program's installed version
# TODO Basic statistics about merged/closed rate.
# TODO Number of days opened.
# TODO Number of comments created.
# TODO Day of the week opened.
# TODO Hour of the day opened.
# TODO Week opened.
# TODO User who opened.
# TODO User who closed.
# TODO Attached labels.
# TODO Number of lines added.
# TODO Number of lines deleted.
# TODO Option to consider only pull requests opened on or after this date.
# TODO Only consider pull requests opened before this date.

import argparse
import requests
import getpass
import configparser
import json

# ("fb99359949c1556bcad2606e1388a29e857f029c")
r = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', headers={'Authorization': 'token fb99359949c1556bcad2606e1388a29e857f029c'})
json_string = r.json()
for dictinory in json_string:
    print(dictinory['title'])

