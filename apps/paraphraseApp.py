import streamlit as st
from scrap import extract
from paraphraser import parphrase

def app():
    st.title('Paraphraser')
    st.write('Please provide a link or copy and paste this link in the cell below- https://www.amazon.com/dp/B09B9TB61G')
    user_input = st.text_input('Enter website link','')
    with st.spinner('Please wait...'):
        if st.button('Paraphrase'):
            data = extract(user_input)
            output = parphrase(data)   
            output = " ".join(output) 
            st.write("Paraphrased Text: ")
            st.write(output)
            st.success("Done!")
