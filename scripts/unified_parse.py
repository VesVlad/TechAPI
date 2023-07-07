import json

import requests
from scripts.functions import from_base
from scripts.functions import db
import undetected_chromedriver as uc
import time
import bs4

def check_in_base(url: str):
    all_source = list(from_base('raw_data', 'course', name_col='url').keys())
    url = list(filter(lambda x: url in x, all_source))
    if len(url) > 0:
        return url[0]
    return None


def get_statistics(url: str):

    schema = getattr(db, 'raw_data')
    table = getattr(schema, 'course')
    url_in_base = check_in_base(url)
    if url_in_base:
        query = db.select(table).where(table.c.url == url_in_base)
        row = list(db.execute(query).all()[0])
        result = " ".join(list(filter(lambda x: isinstance(x, str), row)))

    else:
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        session = uc.Chrome(options=options)
        session.get('https://skillfactory.ru/frontend-razrabotchik')
        html = session.execute_script("return document.body.innerHTML")
        time.sleep(3)
        soup = bs4.BeautifulSoup(html, features="lxml")

        for script in soup(["script", "style", "header", "footer"]):
            script.extract()
        try:
            result = soup.find('main').get_text(' ')
        except:
            result = soup.get_text(' ')

    return requests.post(
            "http://185.127.150.35:6614/score_taxonomy", json={"text": result}
        ).json()
