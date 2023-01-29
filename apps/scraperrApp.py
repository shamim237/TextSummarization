import re
import streamlit as st
from scrap import extract

def app():
    st.title('Scraper')
    st.write('Please provide a link or copy and paste this link- https://www.amazon.com/dp/B09B9TB61G')
    user_input = st.text_input('Enter website link','')
    with st.spinner('Please wait...'):
        if st.button('Scrape'):
            data = extract(user_input)
            sen = []
            for i in data:
                res = len(re.findall(r'\w+', i))
                if res == 2:
                    pass
                else:
                    res = i.replace('"', "'").replace("\n", "")
                    sen.append(res)

            pas = " ".join(sen)   
            st.write("Scrapted data: ")
            st.write(pas)
            st.success("Done!")
