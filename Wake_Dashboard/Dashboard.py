# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:59:47 2022

@author: benja
"""

import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('Location.csv')

add_sidebar = st.sidebar.selectbox('Selection',('School', 'DPI'))

