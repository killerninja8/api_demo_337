# File: generate_wordcloud_function.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

def generate_wordcloud_from_df(wiki_data):
    products_list = [product for products_entry in wiki_data.loc['products'].str.split(',').iloc[-1] for product in products_entry if isinstance(product, str)]
    
    text = ' '.join(products_list)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
