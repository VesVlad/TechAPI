from common_scripts.db import DB
from common_scripts.config_db import DB_COURSES
import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

db = DB(DB_COURSES)

headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
           "authority": "gb.ru",
           "method": "GET",
            "path": "/",
            "scheme": "https",
           "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br",
           "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "out_modal_leave=1; gb_lang_cookie=ru; _gcl_au=1.1.1574604367.1679673648; tmr_lvid=40fb14c2244887272c2afca867047bd0; tmr_lvidTS=1679673649622; _ym_uid=1679673651862003328; _ym_d=1679673651; advcake_session_id=ff080ec4-5b24-f26c-a529-38d3935a2d85; _ymab_param=dH4QkKexb3EhPS9sdVCfsonWv0FE5NYMv6HA3x8TQBfPLHAQjPyt3NERQbRlNTR7ITo0zYUAECE7az1SkwTnSRlQF0Y; __eventn_id=63el9650zi; flocktory-uuid=9066c145-3948-4de6-a09d-b1aabc46f17e-8; OAID=add8d7d7de5c739b6f4a8debdfbbf292; currencyIdV1=rub; sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2023-03-24%2023%3A01%3A09%7C%7C%7Cep%3Dhttps%3A%2F%2Fgb.ru%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; utm_aggregated_data=utm_source=google|||utm_medium=organic|||utm_campaign=(none)|||utm_content=(none)|||utm_term=(none); _tt_enable_cookie=1; _ttp=TBQbE0zqaLF_ckmUXYBArPL3GPZ; sbjs_current_add=fd%3D2023-03-24%2023%3A03%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fgb.ru%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; utm_source=gb.ru; utm_medium=referral; _ga_TKZXC87BVT=GS1.1.1680152241.8.1.1680152241.0.0.0; auth.strategy=local; regionIdV1=RU; lastDefinedRegionIdV1=RU; mtc_sid=trk91q4k4rxd1thf5xyjrxf; mautic_device_id=trk91q4k4rxd1thf5xyjrxf; _gid=GA1.2.1443470137.1681901233; rgn=ru; _gasessionid=20230421|03418877; _app_session=c52b6151a48825aff40487bf1a9dadd1; lessonMenuHidden=true; OABLOCK=1385.1679673806_1393.1679673837_1363.1681061509_1451.1682060464; OACAP=1385.3_1393.1_1363.1_1451.3; OASCAP=1363.1_1451.3; tag_manager_new_registration=true; registered=1; jwt_token=eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJnZWVrYnJhaW5zIiwiaWF0IjoxNjgyMDYwNDg4LCJhdWQiOlsiYWNjZXNzIl0sInVzZXJfaWQiOjk1NDc0OTMsInVwZiI6Im1hYyIsImV4cCI6MTY4NDY1MjQ4OCwiYXV0aGVudGljYXRhYmxlX3NhbHQiOiIiLCJyb2xlcyI6WyJ1c2VyIl19.s282WzvE9p8bgtovug2B7_OoBEZEpqo_TsbcQJgeBuQUIlg214Ps1voEFrEVLt0lmqilQqE0VSIDH40OourTJxxXuV-NgSHD3TEb-f0fLt2ptT6HujYOAdWDRo2VAO4jPRS0JuGZRVMe1vfh2UMbWBMFS2rQt4LHVTiKi_8ksEYA0vtz682i08dunsj8e5gX1d-1-qqIL2-5yaLxtppdaCCKSL2mBWDDPs-2rQHERyDdamj7ToVC6hK1TRerth4Leg3gGdEuV9Sosx3pencP8_f1xehh9Jb3WIsv_IkQi6345Z3xDQZ-b1ZWz6FmyZvP8sdFTepw6dUWO54-eGyJlg; __ddg1_=bnw8j3KPfHQvcne2knQl; __eventn_id_usr=%7B%22internal_id%22%3A%229547493%22%7D; tildauid=1682060491800.849268; mtc_id=9547493; _ym_isad=2; qrator_jsr=1682064938.509.MjaX6wuXpJDs2QZk-3ns41mevko7chhq6pok7gbovbtafgsrt-00; qrator_jsid=1682064938.509.MjaX6wuXpJDs2QZk-4209jhhul0vco31gm0m8vmcnsqbhllp8; _ga_D11RM3RGCC=GS1.1.1682064940.20.0.1682064940.0.0.0; sbjs_udata=vst%3D17%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F111.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgb.ru%2F%2Fgeek_university%2Fdesign%2Fenvironment-designer; landing_url=https://gb.ru//geek_university/design/environment-designer; advcake_trackid=81285529-01a6-f8b4-dc38-4fe655236fac; _ym_visorc=w; _ga=GA1.2.1823034124.1679673649; cto_bundle=KW1Oz19PU0dZTXM2Ukh6WGhvdFM3T25RbzMxQXRwYXdzMVhLQVZtaHk5cmF3bSUyQnNQQjd1Z1dBSjF4Q0Z1WWVCQ2VaTEV5cVp6RGNibGEzNXElMkZwZEVKZm12RjU3R0ZtSUdncEslMkIyWEpZbVJ5UGxHcVBwSzZ0aFB4WUYlMkZibUlKJTJCcmpPczBZQWZuU01aSmVPeVlXJTJGM2lVdjY4RWF0czg3MDFMZmxEYU1TSFcwcVZMQWhUeVc3dVV4eHNtemRiJTJCbU9ZUk8zag; tmr_detect=0%7C1682064943423"}


def from_base(schema, table, id_col='id', name_col='name'):
    schema = getattr(db, schema)
    table = getattr(schema, table)
    data = {}
    query = db.select(
        getattr(table.c, id_col),
        getattr(table.c, name_col)
    )
    for row in db.execute(query):
        data[row[name_col]] = row[id_col]
    return data

def source_links(courses_url):
    all_sourse = from_base('raw_data', 'source', name_col='url')
    if courses_url not in all_sourse.keys():
        source = db.execute(db.raw_data.source.insert(), {'url': courses_url})
        source_id = source.inserted_primary_key[0]
    else:
        source_id = all_sourse[courses_url]

    query = db.select(
        db.raw_data.course.c.url, 
        db.raw_data.course.c.id
    ).where(
        db.raw_data.course.c.source_id == source_id
    )
    last_links = {}
    for l in db.execute(query):
        last_links[l[0]] = l[1]
        
    return source_id, last_links

def drop_links(last_links, active_links):
    for link in last_links.keys():
        if link not in active_links:
            db.execute(
                db.raw_data.course_keywords.delete().where(
                    db.raw_data.course_keywords.c.course_id == last_links[link]
                )
            )
            db.execute(
                db.raw_data.course_skill.delete().where(
                    db.raw_data.course_skill.c.course_id == last_links[link]
                )
            )
            db.execute(
                db.raw_data.course_position.delete().where(
                    db.raw_data.course_position.c.course_id == last_links[link]
                )
            )
            db.execute(
                db.raw_data.course_relevance.delete().where(
                    db.raw_data.course_relevance.c.course_id == last_links[link]
                )
            )
            db.execute(
                db.raw_data.course.delete().where(
                    db.raw_data.course.c.url == link
                )
            )

def date_to_eng(date):
    date = date.split()
    month = date[1]
    if 'январ' in month:
        month = 'January'
    if 'февр' in month:
        month = 'February'
    if 'март' in month:
        month = 'March'
    if 'апрел' in month:
        month = 'April'
    if 'мая' in month:
        month = 'May'
    if 'июн' in month:
        month = 'June'
    if 'июл' in month:
        month = 'July'
    if 'авгус' in month:
        month = 'August'
    if 'сентя' in month:
        month = 'September'
    if 'октяб' in month:
        month = 'October'
    if 'нояб' in month:
        month = 'November'
    if 'декаб' in month:
        month = 'December'
    date[1] = month
    return ' '.join(str(x) for x in date)

def take_level(i):
    level = 4
    if i.find('i', attrs={'class': 'c-course-icon c-course-icon_level1'}):
        level = 1
    if i.find('i', attrs={'class': 'c-course-icon c-course-icon_level2'}):
        level = 2
    if i.find('i', attrs={'class': 'c-course-icon c-course-icon_level3'}):
        level = 3
    return level

def take_level_id(level):
    level_id = 0
    if level == 'easy' or level == 'Junior':
        level_id = 1
    elif level == 'normal' or level == 'Middle':
        level_id = 2
    elif level == 'hard' or level == 'Middle+':
        level_id = 3
    elif level == None:
        level_id = 4
    return level_id

def remove_trash(s):
    return re.sub(" +", " ", s.strip().replace("\n", " ").replace("\xa0", " ").replace("\u200d", " "))

def check_exist(object):
    if object is None:
        return None
    elif isinstance(object, list):
        if len(object) == 0:
            return None
    return object

def days_in_months(months, current_month):
    d_in_months_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                        "Jule": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    d_in_months_dict_ = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    current = d_in_months_dict[current_month]
    res = d_in_months_dict_[current]
    months -= 1
    while months > 0:
        if current == 12:
            current = 0
        current += 1
        months -= 1
        res += d_in_months_dict_[current]
    return res

def captcha_detector(driver, delay=3):
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//html[contains(@prefix, 'ogp.me')]")))
        # driver.find_element(By.XPATH, "//html[contains(@prefix, 'ogp.me')]")
    except TimeoutException:
        return False
    return True

def course_redirect(driver, course):
    course.click()
    driver.switch_to.window(driver.window_handles[-1])

def check_exist_selenium(driver, query: str, key = ''):
    result = None
    try:
        if key == 's':
            result = driver.find_elements(By.XPATH, query)
        elif key == '':
            result = driver.find_element(By.XPATH, query)
    except NoSuchElementException:
        return result
    if isinstance(result, list):
        if len(result) == 0:
            return None
    return result

def click(driver, elem):
    actions = ActionChains(driver)
    actions.move_to_element(elem)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(elem))
    actions.click()
    actions.perform()
    return elem

def wait_element(browser, query: str, delay: int):
    try:
        elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, query)))

    except TimeoutException:
        elem = None
        logging.warning('time limit')

    return elem