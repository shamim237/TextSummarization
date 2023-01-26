import streamlit as st
from scrap import extract
from paraphrase import para
from summary import summarize


st.title("Let's Summarize!")
link = st.text_input("Enter a product link from amazon....")
print(link)
@st.cache(allow_output_mutation=True)
def process():
    data = extract(link)
    #print(data)
    paras = para(data)
    summ = summarize(paras)

    st.success(summ)
st.button('Extract', on_click=process)
st.text("Here is the product description...")
