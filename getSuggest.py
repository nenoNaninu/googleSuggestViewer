# -*- coding: utf-8 -*-

import argparse
from time import sleep
from string import ascii_lowercase
from string import digits
import requests
import urllib.parse
import codecs


class GoogleAutoComplete:
    def __init__(self):
        self.base_url = 'https://www.google.co.jp/complete/search?'\
                        'hl=ja&output=toolbar&ie=utf-8&oe=utf-8&'\
                        'client=firefox&q='

    def get_suggest(self, query):
        buf = requests.get(self.base_url +
                           urllib.parse.quote_plus(query)).json()
        # for item in buf:
        #     if type(item) == type(str):
        #         item.encode('cp932', errors='replace')    
        #     elif type(item) == type(list):
        #         for itemInItem in item:
        #             if type(itemInItem) == type(str):
        #                 itemInItem.encode('cp932', errors='replace')
        # try:
        #     print(buf)
        # except :
        #     return ""
        print(buf)
        suggests = [ph for ph in buf[1]]
        print(suggests)
        print("query: [{0}]({1})".format(query, len(suggests)))
        for ph in suggests:
            print(" ", ph)
        sleep(0.1)
        return suggests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phrase", help="調べたい単語")
    parser.add_argument("file", help="保存するファイル名")

    args = parser.parse_args()

    # Google Suggest キーワード取得
    gs = GoogleAutoComplete()
    
    # ret = gs.get_suggest_with_one_char(args.phrase)
    ret = gs.get_suggest(args.phrase)

    # ファイルに保存する
    fname = args.file
    with codecs.open(fname, 'w','utf-8') as fs:
        i = 0
        for key in ret:
            fs.write(key + "\n")
           