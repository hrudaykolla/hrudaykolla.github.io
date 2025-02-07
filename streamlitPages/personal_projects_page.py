import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os


def personal_projects():
    st.title("Personal Projects")
    
    st.header("Project 1: NLP projects")
    st.write("Description: This repository includes several NLP projects: a fake news classifier, a spam messages classifier, a stock price prediction model using LSTM, and a stock sentiment analysis.")
    st.write("Skills/Tools: Python, VScode, NLP, Machine Learning, Random Forest, Pandas, NLTK, Scikit-Learn")
    st.write("[GitHub Repository](https://github.com/hrudaykolla/nlp_projects)")


    st.header("Project 2: Segmentation with Convexity Prior")
    st.write("Description: Simple architecture for segmenting convex objects in images using user-provided scribbles. The proposed approach involves a primary model to segment pixels into foreground and background regions. The primary model’s output is subsequently passed to a Convex network, which refines the foreground pixels to adhere to the convexity prior, assuming smooth and continuous boundaries without concave regions. The architecture achieves memory efficiency and does not require training on a vast number of images, making it suitable for practical applications with limited computational resources.")
    st.write("Skills/Tools: Python, VScode, Deep Learning, Neural Networks, GitHub, Segmentation, Numpy, Matplotlib, Architecture Design.")
    st.write("[GitHub Repository](https://github.com/hrudaykolla/segmentation_with_convex_prior)")


    st.header("Project 3: Machine Learning Model")
    st.write("Description: Classification performed on Christams backdrop Images of 8 classes like 'Christmas Cookies', 'Christmas Presents', 'Christmas Tree', 'Fireworks', 'Penguin', 'Raindeer', 'Santa', 'Snowman'")
    st.write("[GitHub Repository](https://github.com/hrudaykolla/christmas-image-classification)")