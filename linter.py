import os
import sys
from urlparse import urljoin

import requests


def upload():
    url = urljoin(
        os.environ['LINTER_URL'], '/repos/{repo}/statuses/{sha}'
    ).format(
        repo=os.environ['TRAVIS_REPO_SLUG'],
        sha=os.environ['TRAVIS_COMMIT']
    )

    print url

    response = requests.post(
        url,
        sys.stdin.read()
    )

    response.raise_for_status()
