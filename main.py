import logging
from parser.parser import HtmlParser
from gdrive.gdrive_excel import ExcelWorker

FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    # "https://docs.google.com/spreadsheets/d/1kZ5E7zE316kadIiKAWQE-o_xgagw5m5Ku45cDbWyzLI/edit?usp=sharing"
    gdrive_excel_link = "1kZ5E7zE316kadIiKAWQE-o_xgagw5m5Ku45cDbWyzLI"  # выше строка из которой можно взять линк на файл
    pg_id_parse = "1181220999"  # pg_id confluence
    paraser = HtmlParser()
    page_resp = paraser.get_request(page_id=pg_id_parse)
    if page_resp is None:
        logger.warning("incorrect resp")
        return
    logger.info("got response")

    df_result = paraser.parse_table(page_resp.text, one_table=True)
    if df_result.shape[0] != 0:
        logger.info("can save df")
        ew = ExcelWorker()
        ew.savedf(df_result, gdrive_excel_link)
    else:
        logger.warning("can save nothing")


if __name__ == "__main__":
    main()
