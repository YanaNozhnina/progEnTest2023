import streamlit as st

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



