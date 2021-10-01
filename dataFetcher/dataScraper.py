import os

import requests


class Scraper:

    def __init__(self):
        self._url = os.environ["SUBSTITUTION_PLAN_URL"]

    def scrape(self):
        return requests.get(self._url).text
