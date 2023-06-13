import io
import streamlit as st
from PIL import Image
import numpy as np

from st_pages import Page, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("example_app/streamlit_app.py", "Give it a chance!", "🚀"),
        Page("example_app/easy_disposal.py", "Proper disposal is easy!", "🌞"),
        Page("example_app/glass.py", "Glass", "🥛"),
        Page("example_app/metal.py", "Metal", "📎"),
        Page("example_app/paper.py", "Paper", "📰"),
        Page("example_app/plastic.py", "Plastic", "♻️"),
        Page("example_app/other.py", "Other", "🗑️"),
        
    ]
)

add_page_title()  # Optional method to add title and icon to current page