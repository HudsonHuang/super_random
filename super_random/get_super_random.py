# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:03:20 2018

@author: hudson_huang

This API returns exchange rate of EUR-USD as a random number, 
which updates rates daily around 4PM CET every working day.

"""

import requests
import time

__author__ = 'hudson_huang'
EUR_USD_url = "https://api.fixer.io/latest?symbols=USD"
target_currency_list = ["USD"]

def get_super_random(currency = 'USD',bit = 2, get_time_ticks = False):
    assert currency in target_currency_list
    assert bit < 5
    random, time_ticks = url_get_random(bit,currency = currency, url = EUR_USD_url)
    if get_time_ticks == False:
        return random
    else:
        return random, time_ticks
            
def url_get_random(bit, currency, url):
    reg = ['"',currency,'":'] 
    reg = ''.join(reg)
    price_json = requests.get(url)
    time_ticks = time.time()
    price_content = price_json.content
    content_str = "".join(map(chr, price_content))
    content_list_forward = content_str.split(reg)[1]
    current_price = content_list_forward.split('}')[0]
    current_price = float(current_price)
    current_price_big = int(current_price*10000)
    random = current_price_big%(10**bit)
    return random, time_ticks



if __name__ == "__main__":
    # test super random
     assert type(get_super_random(currency = 'USD')) is int