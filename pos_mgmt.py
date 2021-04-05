# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:30:36 2021

@author: shane
"""

import pandas as pd
from src.admin import colclean, write_json
#Position management is super, super annoying
#let's fix that

#first, we need a list of all of the position numbers
#since we run reports with all of those, that's fine
def poslist():
    fileloc=r'Y:\Reports\vacant_positions.xlsx'
    df=colclean(pd.read_excel(fileloc))
    #what we want to end up with is just a collection of position numbers to start with
    #we can store that in our program data folder as json
    df.columns # to know which column to grab
    poslist=['00'+x for x in list(df.position_.astype('str').values)]
    dataloc=r'y:\reports\program data\positions'
    write_json(poslist,dataloc)
# we now have a json file which should be at 'y:\reports\program data\positions.json'

#now we need a reference point to establish what position numbers are in use
#luckily we have a data source for that
#this is for filtering and also for future-proofing

#we also need a way of determining if a position number requires updating
#this is for future-proofing

