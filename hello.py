# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:45:32 2019

@author: hmazo
"""
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import quandl

aapl = quandl.get("WIKI/AAPL", start_date="2018-01-01", end_date="2019-01-01")
aapl.head()