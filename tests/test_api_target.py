# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 2024

@author: Weiyuan Ding
"""
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.main_streamlit import search_items_API

def test_api_target():
    product = 'laptop'
    site = 'tg'
    result = search_items_API(site, product)
    assert result is not None
