import pandas as pd
import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class HtmlParser:

    _url = "https://confluence.hflabs.ru/pages/viewpage.action?pageId="  # линк на конфу

    def __init__(self):
        self.bs4 = BeautifulSoup()
        self._session = requests.Session()

    def parse_table(
        self, html_string: str, one_table=True
    ) -> [
        pd.DataFrame,
    ]:
        pandas_lists = pd.read_html(html_string)
        logger.info(f"read {len(pandas_lists)}")
        if one_table and len(pandas_lists):
            return pandas_lists[0]  # пока тупо первую таблицу
        return pandas_lists

    def get_request(self, page_id) -> [requests.Response, None]:
        resp = self._session.get(f"{self._url}{page_id}")
        if resp.status_code != requests.codes.ok:
            logger.warning(f"status code isn't ok : is {resp.status_code}")
            return None
        return resp
