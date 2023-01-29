import streamlit as st
from scrap import extract
from paraphraser import parphrase
from summary import text_summary


def app():
    st.title('Summarizer')
    st.write('Please provide a link or copy and paste this link- https://www.amazon.com/dp/B09B9TB61G')
    user_input = st.text_input('Enter website link','')
    with st.spinner('Please wait...'):
        if st.button('Summarize'):
            data = extract(user_input)
            paras = parphrase(data)
            summ = text_summary(paras)
            output1 = " ".join(summ)
            st.write("Text Summary: ")
            st.write(output1)
            st.success('Done!')            
