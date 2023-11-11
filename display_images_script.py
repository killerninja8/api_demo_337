# File: display_images_script.py
import pandas as pd
import wikipedia
from IPython.display import display, HTML

def display_images(wiki_data, n):
    df = pd.DataFrame(wiki_data)
    df = df.replace('{{|}}', '', regex=True)
    df = df.replace('nowrapl', '')

    for index in wikipedia.WikipediaPage('Walmart').images[:n]:
        # Create an HTML image tag to display the image
        img_tag = f'<img src="{index}" alt="{"IMG"}">'

        # Use IPython.display to render the image in the Notebook
        display(HTML(img_tag))
