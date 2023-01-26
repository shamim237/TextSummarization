import streamlit as st
from scrap import extract
from paraphrase import para
from summary import summarize


st.title("Let's Summarize!")
link = st.text_input("Enter a product link from amazon....")
print(link)
def process():
    data = extract(link)
    #print(data)
    paras = para(data)
    @st.cache(allow_output_mutation=True)
    summ = summarize(paras)
    @st.cache(allow_output_mutation=True)
    st.success(summ)
st.button('Extract', on_click=process)
st.text("Here is the product description...")
