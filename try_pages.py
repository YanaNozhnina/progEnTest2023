import io
import streamlit as st
from PIL import Image
import numpy as np

from st_pages import Page, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("example_app/streamlit_app.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("example_app/metal.py", "Metal", "📎"),
        # The pages appear in the order you pass them
        Page("example_app/plastic.py", "Plastic", "♲"),
        Page("example_app/paper.py", "Paper", "📰"),
        # Will use the default icon and name based on the filename if you don't
        # pass them
        Page("example_app/glass.py", "Glass", "🥛"),
        Page("example_app/other.py", "Other", "🗑"),
    ]
)

add_page_title()  # Optional method to add title and icon to current page