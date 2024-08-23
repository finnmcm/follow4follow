#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:14:08 2024

@author: finnmcmillion
"""

import pandas as pd
import os
import json


with open('followers_1.json') as follower:
  followers = json.load(follower)
  
with open('following.json') as following:
  following = json.load(following)

follower_list = []
following_list = []
diff = []

#print(following['relationships_following'][0]['string_list_data'][0]['value'])

for i in range(len(followers)):
    follower = followers[i]['string_list_data'][0]['value']
    follower_list.append(follower)

for i in range(len(following['relationships_following'])):
    follow = following['relationships_following'][i]['string_list_data'][0]['value']
    following_list.append(follow)

for name in following_list:
    if name not in follower_list:
        diff.append(name)

for i in diff:
    print(i + "\n")