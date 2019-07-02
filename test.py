#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:38:11 2019

@author: ashubunutu
"""


import pandas as pd;
import numpy as np;
from get_count import get_count

frame_rate=str(input("Please Enter The Frame rate:"))
count=get_count(frame_rate)