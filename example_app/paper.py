import streamlit as st
import pandas as pd
import numpy as np

from st_pages import add_page_title

add_page_title()
st.header("Your papers, please!")

st.write("Paper makes up 23 percent of municipal solid waste (trash) \
         generated each year, more than any other material. \
         Americans recycled about 68 percent of the paper they used in 2018. \
         This recovered paper is used to make new paper products, \
         which saves trees and other natural resources. \
         Most community or office recycling programs accept paper and paper products. \
         Check what your community or office program accepts before you put it in the bin. \
         Look for products that are made from recycled paper when you shop. \
         Better yet, consider if you really need to print in the first place.")

st.subheader("Can I recycle newspapers?")
st.write("Yes, newspapers can be recycled.")
st.subheader("Can I recycle magazines?")
st.write("Yes, magazines can be recycled. ")
st.subheader("Can I recycle pizza boxes? ")
st.write("Yes! Pizza boxes can be recycled, even if they have grease in them.\
          Make sure to remove any food scraps from the box and flatten it before placing it in the bin.")

st.header("Local recycling")
df = pd.DataFrame(np.array([[56.850070937905315, 60.6438780875638],
                            [56.84253295582028, 60.67638554449489], 
                            [56.84701142459734, 60.61574882565075],
                            [56.83473973233743, 60.623572764765655],
                            [56.832288865260466, 60.694096869352244]]),
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


