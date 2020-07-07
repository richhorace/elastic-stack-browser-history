
import json
import os
import sqlite3
import time

from config import USER_PATH
from local import LOG_DIR

def get_path(browser,browser_params):
    if browser == 'brave':
        BRAVE_PATH = "Library/Application Support/BraveSoftware/Brave-Browser/Default/History"
        hist_path = USER_PATH + BRAVE_PATH
        hist_sql = "SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime') AS visit_date, url, title AS url_title  FROM urls ORDER BY visit_date DESC"
        browser_params['browser_name'] = browser
        browser_params['hist_path'] = hist_path
        browser_params['hist_sql'] = hist_sql
        return browser_params
    elif browser == 'chrome':
        CHROME_PATH = "Library/Application Support/Google/Chrome/Default/History"
        hist_path = USER_PATH + CHROME_PATH
        hist_sql = "SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime') AS visit_date, url, title AS url_title  FROM urls ORDER BY visit_date DESC"
        browser_params['browser_name'] = browser
        browser_params['hist_path'] = hist_path
        browser_params['hist_sql'] = hist_sql
        return browser_params
    elif browser == 'edge':
        EDGE_PATH = "Library/Application Support/Microsoft Edge/Default/History"
        hist_path = USER_PATH + EDGE_PATH
        hist_sql = "SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime') AS visit_date, url, title AS url_title  FROM urls ORDER BY visit_date DESC"
        browser_params['browser_name'] = browser
        browser_params['hist_path'] = hist_path
        browser_params['hist_sql'] = hist_sql
        return browser_params
    elif browser == 'firefox':
        FIREFOX_PATH = "Library/Application Support/Firefox/Profiles/tsmorvto.default-release/places.sqlite"
        hist_path = USER_PATH + FIREFOX_PATH
        hist_sql = "SELECT datetime(moz_historyvisits.visit_date/1000000,'unixepoch','localtime') AS visit_date, moz_places.url AS url, moz_places.title AS url_title FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id ORDER BY visit_date DESC"
        browser_params['browser_name'] = browser
        browser_params['hist_path'] = hist_path
        browser_params['hist_sql'] = hist_sql
        return browser_params
    elif browser == 'safari':
        SAFARI_PATH = "Library/Safari/History.db"
        hist_path = USER_PATH + SAFARI_PATH
        hist_sql = "SELECT datetime(visit_time + 978307200, 'unixepoch', 'localtime') AS visit_date, url, title AS url_title FROM history_visits INNER JOIN history_items ON history_items.id = history_visits.history_item ORDER BY visit_date DESC"
        browser_params['browser_name'] = browser
        browser_params['hist_path'] = hist_path
        browser_params['hist_sql'] = hist_sql
        return browser_params

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_browser_hist(browser_params,timestr):
    bn = browser_params['browser_name']
    # connect to the SQlite databases
    connection = sqlite3.connect(browser_params['hist_path'])
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    try:
        cursor.execute(browser_params['hist_sql'])
    except:
        browser_open = ("\t" + bn + "!! " +"is open. Please close your browser and retry.")
        print(browser_open.upper())

    tables = cursor.fetchall()
    results = len(tables)
    print("{}: Results {}".format(bn, results))
    print()

    if results >0:
        dict_bn = {"browser":bn}
        jsonFile = open(LOG_DIR + "/"+ bn + "-" + timestr + ".json","w")

        for v in tables:
            v.update(dict_bn)
            jsonFile.write(json.dumps(v) + '\n')


def main():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    browsers = ['brave','chrome','firefox','safari','edge']
    for browser in browsers:
        print("Starting {}".format(browser))
        browser_params = {}
        path = get_path(browser,browser_params)
        if path:
            get_browser_hist(browser_params,timestr)
main()