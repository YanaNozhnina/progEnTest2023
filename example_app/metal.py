import streamlit as st
import pandas as pd
import numpy as np

from st_pages import add_page_title

add_page_title()
st.subheader("Fire :fire: + sand :hourglass_flowing_sand:")

st.write("In 2018, 19.2 million tons of ferrous metals (iron and steel) were generated.\
          EPA estimates that the recycling rate of ferrous metals from durable goods was 27.8 percent.\
          The same year, 2.5 million tons of nonferrous metals (not containing iron) were generated. \
         The recycling rate for nonferrous metals was approximately 68 percent.")

st.subheader("How do I recycle metal? ")
st.write("There are different programs and options for metal recycling depending on your locality.\
          Check to find out what is available in your area. ")

st.header("Aluminum")
st.write("In 2018, 3.9 million tons of aluminum municipal solid waste was generated.\
          The total recycling rate for aluminum items was 34.9 percent. Both aluminum cans and foil can be recycled. ")
st.subheader("Should aluminum cans be crushed before recycling them?")
st.write("No, generally, aluminum cans should not be crushed before they are recycled.\
          For areas with single-stream recycling, \
         crushed cans are harder to detect when being sorted at recycling facilities. \
         If you live in an area with multi-stream recycling, crushing cans is not an issue.")
st.subheader("Can I recycle aluminum foil?")
st.write("Yes, aluminum foil can be recycled. Make sure to remove any food residue before recycling.")

st.header("Local recycling")
df = pd.DataFrame(np.array([[56.83908653272441, 60.664743161437244],
                            [56.83864065320008, 60.64765229697966], 
                            [56.83217829989505, 60.69366639157996]]),
    columns=['lat', 'lon'])
st.map(df)
st.subheader("«СтеклоВторЕкб»")
st.write("улица Студенческая, д.49 Бокс №13")
st.write("Тел. +7 (922) 181-30-81")
st.subheader("Приём стеклопосуды")
st.write("ул. Гагарина, 47")
st.write("Тел. +7 (950) 190-38-56")
st.subheader("Пункт приема вторсырья")
st.write("ул. 40 Лет ВЛКСМ, 12")
st.write("Тел. +7 (908) 636-43-17")
