#!/usr/bin/env python
# coding: utf-8

# In[66]:


import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from PIL import Image
class air:
    def airquality(self):
        url='https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd0000013f43dd62e27448bd6759892c8c5d4bfa&format=csv&offset=0&limit=2000'
        response=requests.get(url,params=None)
        k=[i.split(',') for i in  response.text.split('\n')]
        k.remove(k[0])
        df=pd.DataFrame(k)
        df1=df[[2,3,7,10]]
        df1.rename(columns=dict(zip(list(df1.columns),['state','city','pollutant','pollutant_avg'])),inplace=True)
        return df1

    def auto_co_visualizer(self):
        file=self.airquality()
        f1=file[file['pollutant']=='CO']
        x=np.array([])
        x=np.append(x,f1[f1['pollutant_avg']=='NA'].index.values)
        f1.drop(x,axis='index',inplace=True)
        f1=f1.astype({'pollutant_avg':'int64'})
        st.title('Real-time average carbon monoxide rate in Indian Cities (refreshes every one hour)')
        hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>

        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
        st.text('NOTE:If a city  shows multiple carbon monoxide rates, it is the data from multiple air quality monitoring stations in the  city.')
        i=st.sidebar.selectbox('Select state',list(np.unique(f1['state'])))
        c=f1[f1['state']==i]
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
        image = Image.open('air_quality_index_standards_CPCB_650.jpg')
        st.image(image)
if __name__ == "__main__":
    air().auto_co_visualizer()
    
      
