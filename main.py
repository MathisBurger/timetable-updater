from dataFetcher.dataFetcher import DataFetcher
from dotenv import load_dotenv
load_dotenv()

fetcher = DataFetcher()
fetcher.get_substitution()