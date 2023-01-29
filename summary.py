import nltk
import streamlit as st
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer

@st.cache(allow_output_mutation=True, ttl=48*3600)
def dwnld_lib():
    nltk.download('punkt')
    
dwnld_lib()

def text_summary(text):
    para = " ".join(text)
    # Create a plaintext parser and tokenizer
    parser = PlaintextParser.from_string(para, Tokenizer("english"))
    # Create a LexRank summarizer
    summarizer = LexRankSummarizer()
    # Summarize the text and print the results
    summ = []
    for sentence in summarizer(parser.document, 4):
        summy =  str(sentence).capitalize()
        summ.append(summy)
    return summ
