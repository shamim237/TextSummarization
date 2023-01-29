import streamlit as st
from multiapp import MultiApp
from apps import paraphraseApp, summarizerApp, scraperrApp

app = MultiApp()

st.title("Python Dev Task @SkyRanko")
st.write("==================_Completed by_ **Shamim Mahbub**==================")
st.markdown("This app provides three services - :red[Scraping], :orange[Paraphrasing] and :blue[Summarizing]")
st.caption("Note: _After scraping data from Amazon, the data has been paraphrased using a model and then Summarization has been performed on the paraphrased data._")

# Add all your application here
app.add_app("Scraper", scraperrApp.app)
app.add_app("Paraphraser", paraphraseApp.app)
app.add_app("Summarizer", summarizerApp.app)
# The main app
app.run()
