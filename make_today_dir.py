# -*- coding: utf8 -*-
from datetime import date
import os

today_dir = date.today().strftime("%Y.%d.%m")
i = 1
while os.path.exists(today_dir):
    today_dir = f'{date.today().strftime("%Y.%m.%d")}_{str(i)}'
    i += 1
os.makedirs(today_dir)
