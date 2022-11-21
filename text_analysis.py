from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# Importing the StringIO module.
from io import StringIO 
from nltk import corpus, FreqDist, word_tokenize
import altair as alt

st.write("## Analysing Shakespeare texts")

st.sidebar.header("Word Cloud Settings")
max_word = st.sidebar.slider("Max Words",10,200,100,10)
max_font = st.sidebar.slider("Size of largets word",50,350,60)
image_size = st.sidebar.slider("Image width",100,800,400,10)
random = st.sidebar.slider("Random State",30,100,42)


st.sidebar.header("Word Count Settings")
image = st.file_uploader("Choose a txt file")

if image is not None:
    # To convert to a string based IO:
    stringio = StringIO(image.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    dataset = stringio.read()
    #st.write(dataset)

    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came'])

tab1, tab2, tab3 = st.tabs(["Word Cloud","Bar Chart","View Text"])

with tab1:
        if image is not None:
            cloud = WordCloud(background_color = "white", 
                                max_words = max_word, 
                                max_font_size=max_font, 
                                stopwords = stopwords, 
                                random_state=random)

            wc = cloud.generate(dataset)
            word_cloud = cloud.to_file("wordcloud.png")
            st.image(wc.to_array(),width = image_size)

with tab2:
    if image is not None:
        

       def word_count(str):
    # Create an empty dictionary
        counts = dict()
        words = str.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    bar = pd.DataFrame(word_count(dataset).items(), columns=['Word', 'Count'])
        
    a = alt.Chart(bar).mark_bar().encode(
    x='Count',
    y='Word'
    ).properties(
    height=1500000
    ).interactive()
    st.write(a)
with tab3:
    if image is not None:
        st.write(dataset)