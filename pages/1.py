import streamlit as st
import requests
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import seaborn as sns
# from dotenv import load_dotenv
# import os

st.markdown("<h1 style='text-align: center;'>🚨지역별 성범죄 통계🚨</h1>",
            unsafe_allow_html=True)

# http://api.sexoffender.go.kr/index.jsp

# load_dotenv()
# key = os.getenv("key")
url = "http://api.sexoffender.go.kr/openapi/SOCitysStats/"
params = {"serviceKey": st.secrets['key']}
# API 호출
response = requests.get(url, params=params)

if response.status_code == 200:
    root = ET.fromstring(response.content)
    data = []

    for city in root.findall(".//City"):
        data.append(
            {
                "city-name": city.find("city-name").text,
                "city-count": city.find("city-count").text,
            }
        )
    df = pd.DataFrame(data)
    df['city-count']=df['city-count'].astype(int)
    df = df.sort_values('city-count', ascending=False)
    
    # 시각화
    mpl.rcParams['font.family']='Malgun Gothic'
    mpl.rcParams['font.size']=12
    mpl.rcParams['axes.unicode_minus']=False
    
    fig=plt.figure(figsize=(12, 6))
    sns.barplot(x='city-name', y='city-count', data=df)
    plt.xticks(rotation=45)
    # plt.show()
    st.pyplot(fig)