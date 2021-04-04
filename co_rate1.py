#!/usr/bin/env python
# coding: utf-8

# In[66]:


import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import time
class air:
    def airquality(self):
        url='https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd0000013f43dd62e27448bd6759892c8c5d4bfa&format=csv&offset=0&limit=2000'
        response=requests.get(url,params=None)
        file=open('co_india.csv','w')
        file.write(response.text)
        file.close()
    def auto_co_visualizer(self):
        self.airquality()
        file=pd.read_csv('co_India.csv')
        file.drop('id',axis=1,inplace=True)
        f1=file[file['pollutant_id']=='CO']
        f1.drop('pollutant_unit',axis=1,inplace=True)
        f2=f1[['state','city','pollutant_avg']]
        f2.dropna(inplace=True)
        st.title('Realtime carbon monoxide rate in Indian Cities (refreshes every one hour)')
        i=st.sidebar.selectbox('Select state',list(np.unique(f2['state'])))
        c=f2[f2['state']==i]
        fig, ax = plt.subplots(figsize=(7,6))
        plt.title(i)
        ax.scatter(c['city'],c['pollutant_avg'],color='red')
        ax.set_xlabel('Cities')
        ax.set_ylabel('Carbon monoxide rate(aqi)')
        plt.xticks(list(c['city']),rotation='vertical')
        ax.set(facecolor='lightgray')
        plt.grid()
        st.pyplot(fig)
        st.button('Refresh')
if __name__ == "__main__":
    air().auto_co_visualizer()
    
      

