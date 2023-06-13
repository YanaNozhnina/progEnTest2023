import streamlit as st
import pandas as pd
import numpy as np

from st_pages import add_page_title

add_page_title()
st.subheader(":fire: + :hourglass_flowing_sand:")

st.write("Glass, especially glass food and beverage containers,\
          can be recycled over and over again. \
         Making new glass from recycled glass is typically cheaper than using raw materials. ")

st.subheader("Can I recycle different glass colors/types together?")
st.write("Most curbside recycling programs \
         accept different glass colors and \
         types mixed together and then sort the glass at the recovery facility.")
st.subheader("Can I recycle broken glass?")
st.write("No, broken glass should not go into the recycling bin.\
          Glass shards can harm workers and damage equipment.  ")
st.subheader("Can I leave my metal bottle cap on my glass bottle when I recycle?")
st.write("No, metal bottle caps should be recycled separately from the glass bottles.")

st.header("Local recycling")
df = pd.DataFrame(np.array([[],
                            [], 
                            [],
                            [],
                            []]),
    columns=['lat', 'lon'])
st.map(df)
st.subheader("«Уралвторма»")
st.write("ул. Высоцкого, 11")
st.write("Тел. +7 (902) 874-99-50")
st.write("ул. Академическая, 8А")
st.write("Тел. +7 (904) 382-31-30")
st.subheader("«Радон-с»")
st.write("ул. Мамина-Сибиряка, 85")
st.write("Тел. +7 (343) 350-02-45")
