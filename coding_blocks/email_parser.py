#!/usr/bin/env python3

import requests
import json
import re
from random import randint



purple = '\033[95m'
yellow = '\033[93m'

email = re.compile("\A[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com|in)\Z")
url = 'https://hack-api.codingblocks.com/api/v2/users/'

f = open("emails.txt",'wt')

while (True):
    a = randint(0000,9999)
    r = requests.get(url+str(a))
    if r.status_code == 404:
	pass
    else:
	b = json.loads(r.text)
	for i in b['data']['attributes']:
	    print (u"{0} {2} : {1} {3}".format(yellow,purple,i,b['data']['attributes'][i]))
        print ("\n\n")
        try:
            if email.match(b['data']['attributes']['email']) != None:
                f.write(u"{}\n".format(b['data']['attributes']['email']))
        except:
            pass
