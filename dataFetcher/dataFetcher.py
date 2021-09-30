from dataFetcher.dataParser import Parser
from dataFetcher.dataScraper import Scraper


class DataFetcher:

    def __init__(self):
        self._scraper = Scraper()
        self._parser = Parser()

    def get_substitutions(self):
        html = self._scraper.scrape()
        return self._parser.get_substitution_of_class(html)
