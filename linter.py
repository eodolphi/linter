import json
import sys
from urlparse import urljoin

import git
import requests

API_URL = 'http://localhost:5000'


def push():
    report = sys.stdin.readlines()

    repo = git.Repo('.')
    commit = repo.commit()

    data = {
        'origin': [remote.origin.url for remote in repo.remotes],
        'branch': str(repo.active_branch),
        'commit': commit.hexsha,
        'author': {
            'name': commit.author.name,
            'email': commit.author.email
        },
        'report': [line.strip() for line in report]
    }

    print json.dumps(data, indent=4)
    response = requests.post(
        urljoin(API_URL, 'reports'),
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    response.raise_for_status()
