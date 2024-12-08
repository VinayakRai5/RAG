import base64
import streamlit as st
import time
from utils import answer, answer1

# Sidebar navigation
page = st.sidebar.selectbox("Jump to... 👇", ["About", "PDF", "Video"])

if page == 'About':
    st.markdown("""
        <h2 style="text-align: center;">Welcome to the Multi-Modal RAG WebApp</h2>
        <p style="text-align: center;">This app demonstrates a Multi-Modal Retrieval-Augmented Generation system.</p>
        """, unsafe_allow_html=True)
    st.image('multimodal.png')
    st.success("📣 Check out the 'Demo' section for more details on how the app works.")
    
elif page == 'PDF':
    st.sidebar.write("[Sample PDF Resource](https://eacpm.gov.in/wp-content/uploads/2023/01/Monuments-of-National-Importance.pdf)")
    st.markdown("""
        <h2 style="text-align: center;">Multi-Modal RAG (PDF)</h2>
        <p style="text-align: center;">Ask any question related to the provided PDF resource.</p>
        """, unsafe_allow_html=True)
    user_input = st.text_area(label="Enter your question:")

    if st.button("Submit"):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Normal RAG')
            with st.chat_message("user"):
                st.markdown(user_input)
            result, _ = answer(user_input)
            with st.chat_message("assistant"):
                with st.spinner('Processing...'):
                    time.sleep(2)
                st.markdown(result)

        with col2:
            st.subheader('Multi-Modal RAG')
            with st.chat_message("user"):
                st.markdown(user_input)
            result, relevant_images = answer(user_input)
            with st.chat_message("assistant"):
                with st.spinner('Processing...'):
                    time.sleep(2)
                st.markdown(result)
            if relevant_images:
                st.image(base64.b64decode(relevant_images[0]))

elif page == 'Video':
    st.markdown("""
        <h2 style="text-align: center;">Multi-Modal RAG (Video)</h2>
        <p style="text-align: center;">Ask any question related to the provided video resource.</p>
        """, unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=rRZdtAGInyQ&list=PLhRXULtLjLtfQ9COvoZg8Zg6ejTI3UPTG&index=1")  # Placeholder video link
    user_input = st.text_area(label="Enter your question:")

    if st.button("Submit"):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Normal RAG')
            with st.chat_message("user"):
                st.markdown(user_input)
            result, _ = answer1(user_input)
            with st.chat_message("assistant"):
                with st.spinner('Processing...'):
                    time.sleep(2)
                st.markdown(result)

        with col2:
            st.subheader('Multi-Modal RAG')
            with st.chat_message("user"):
                st.markdown(user_input)
            result, relevant_images = answer1(user_input)
            with st.chat_message("assistant"):
                with st.spinner('Processing...'):
                    time.sleep(2)
                st.markdown(result)
            if relevant_images:
                st.image(base64.b64decode(relevant_images[0]))
