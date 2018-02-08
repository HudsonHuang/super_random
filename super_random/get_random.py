# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:03:20 2018

@author: hudson_huang

The API returns currency of EUR-USD as a random number, 
which updates rates daily around 4PM CET every working day.

"""

import requests
import time


def get_super_random(currency = 'USD',bit = 2, get_time_ticks = False):
    assert currency in ["USD"]
    assert bit < 5
    if currency == "USD":
        random, time_ticks = get_EUR_USD_random(bit)
        if get_time_ticks == False:
            return random
        else:
            return random, time_ticks
            
def get_EUR_USD_random(bit):
    url = "https://api.fixer.io/latest?symbols=USD"
    price_json = requests.get(url)
    time_ticks = time.time()
    price_content = price_json.content
    content_str = "".join(map(chr, price_content))
    content_list_forward = content_str.split('"USD":')[1]
    current_price = content_list_forward.split('}')[0]
    current_price = float(current_price)
    current_price_big = int(current_price*10000)
    random = current_price_big%(10**bit)
    return random, time_ticks



if __name__ == "__main__":
    # test super random
    print(get_super_random())