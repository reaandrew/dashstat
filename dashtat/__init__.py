import os
import requests
import argparse
import datetime
import humanize
from dateutil.parser import parse
import falcon
import json

from dashtat.services import GithubService
from dashtat.resources import PullRequestsResource

import falcon

app = falcon.API()

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
ORG = os.environ['ORG']

service = GithubService(GITHUB_TOKEN)

app.add_route('/pulls', PullRequestsResource(ORG, service))
