import re
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def para(paragraph):
    model = AutoModelForSeq2SeqLM.from_pretrained("ramsrigouthamg/t5-large-paraphraser-diverse-high-quality")
    tokenizer = AutoTokenizer.from_pretrained("ramsrigouthamg/t5-large-paraphraser-diverse-high-quality")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    sen = []
    for i in paragraph:
        res = len(re.findall(r'\w+', i))
        if res == 2:
            pass
        else:
            res = i.replace('"', "'").replace("\n", "")
            sen.append(res)

    para = []
    for sentence in sen:
        text = "paraphrase: " + sentence + " </s>"

        encoding = tokenizer.encode_plus(text,max_length =1024, padding=True, return_tensors="pt")
        input_ids,attention_mask  = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

        model.eval()
        beam_outputs = model.generate(
            input_ids=input_ids,attention_mask=attention_mask,
            max_length=1024,
            early_stopping=True,
            num_beams=15,
            num_return_sequences=3)

        #for beam_output in beam_outputs:
        sent = tokenizer.decode(beam_outputs[2], skip_special_tokens=True,clean_up_tokenization_spaces=True)
        para.append(sent)
    paras = []
    for i in para:
        resf = i.replace("paraphrasedoutput: ", "")
        paras.append(resf)
    return paras
        

