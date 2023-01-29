from scrap import extract
from paraphraser import parphrase
from summary import text_summary
import warnings
warnings.filterwarnings('ignore')

url = "https://www.amazon.com/dp/B09B9TB61G" # website to scrape data

data = extract("https://www.amazon.com/dp/B09B9TB61G")
paraphrase_data = parphrase(data)
summarized_data = text_summary(paraphrase_data)


with open("result_doc.txt", "w", encoding="utf-8") as result:
    result.write("Raw Data: " + "\n" + " ".join(data))
    result.write("\n\n")
    result.write("Paraphrased Data: " + "\n" + " ".join(paraphrase_data))
    result.write("\n\n")
    result.write("Summarization: " + "\n" + " ".join(summarized_data))
result.close()

