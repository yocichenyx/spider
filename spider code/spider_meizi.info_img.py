# -*- coding: utf-8 -*-
# @Author  : yocichen
# @Email   : yocichen@126.com
# @File    : meizi.py
# @Software: PyCharm
# @Time    : 2019/11/17 8:39

import re
import requests
from requests import RequestException
import time
import random
import os
from bs4 import BeautifulSoup
import lxml

def get_one_page(url):
    '''
    Get the html of a page by requests module
    :param url: page url
    :return: html / None
    '''
    try:
        head = ['Mozilla/5.0', 'Chrome/78.0.3904.97', 'Safari/537.36']
        headers = {
            'user-agent':head[random.randint(0, 2)]
        }
        response = requests.get(url, headers=headers) #, proxies={'http':'171.15.65.195:9999'}
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page_re(pattern_text, html):
    try:
        pattern = re.compile(pattern_text)
        res = re.findall(pattern, html)
        if res is None or len(res) == 0:
            return None
        else:
            return res
    except Exception:
        return None

def get_title_bs4(html, selector):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.select(selector)
    if res is None:
        return 'NULL'
    elif len(res) == 0:
        return 'NULL'
    else:
        return res[0].string

def name_format(dir_name):
    dir_name = dir_name.replace('"', "") \
        .replace('\\', "").replace('/', "") \
        .replace("*", "").replace("?", "") \
        .replace("<", "").replace(">", "") \
        .replace(":", "-")
    return dir_name

def make_dir(parent_dir, dir_name):
    if os.path.exists(parent_dir):
        dir_name = name_format(dir_name)
        path = parent_dir+'\\'+dir_name
        if not os.path.exists(path):
            os.mkdir(path, 0o755)
            return 1
        else:
            return 0
    else:
        return 0


def get_one_img(url, dir_path, img_name):
    try:
        html = requests.get(url)
        with open(dir_path+'\\'+img_name, 'wb') as f:
            f.write(html.content)
        f.close()
        print(dir_path+'\\'+img_name, ', ok')
        return 1
    except Exception:
        return None

def main(url, parent_dir):
    html = get_one_page(url)
    if html is not None:
        selector = 'body > section > div.content-wrap > div > header > h1 > a'
        dir_name = get_title_bs4(html, selector)
        if dir_name == 'NULL':
            print('title get failed')
            # return -1
        else:
            # print(dir_name)
            if make_dir(parent_dir, dir_name):
                print(parent_dir+'\\'+dir_name, ', create OK')
                pattern_text = '<img src="(.*?)"'
                res = parse_one_page_re(pattern_text, html)
                if res is None:
                    print('imgs get failed')
                else:
                    total = 0
                    for src in res:
                        src_get = get_one_img(src, parent_dir+'\\'+name_format(dir_name), os.path.basename(src))
                        if src_get is not None:
                            total += src_get
                    print(total, 'ok')
            else:
                print(parent_dir+'\\'+dir_name, ', not found')
                # return -2

if __name__ == '__main__':
    # you need use other url replace the url
    url = 'http://meizi.info/ariadna-majewska.html'
    # you need use other locatal directory path to replace the path
    main(url, 'D:\\pyfiles\\spider\\photos')