import logging

from parser import QuotesParser

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
logger = logging.getLogger(__name__)

def main():
    quotes_parser = QuotesParser()
    pages = len(quotes_parser.get_count_pages())
    logger.info("Get %s pages", pages)
    quotes_parser.parse_all_page()
    logger.info("Work is done!")
    quotes_parser.write_data_to_json()
    logger.info("Data written successfully")


if __name__ == '__main__':
    main()