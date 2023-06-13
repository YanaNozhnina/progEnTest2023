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
        Page("example_app/example_one.py", "Example One", ":books:"),
        # The pages appear in the order you pass them
        Page("example_app/example_four.py", "Example Four", "📖"),
        Page("example_app/example_two.py", "Example Two", "✏️"),
        # Will use the default icon and name based on the filename if you don't
        # pass them
        Page("example_app/example_three.py"),
        Page("example_app/example_five.py", "Example Five", "🧰"),
    ]
)

add_page_title()  # Optional method to add title and icon to current page