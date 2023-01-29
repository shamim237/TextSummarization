import re
import nlpaug.augmenter.word as naw


def load_model():
    aug = naw.ContextualWordEmbsAug(
        model_path='bert-base-uncased', action="insert")
    return aug

aug = load_model()

def parphrase(passage):
    sen = []
    for i in passage:
        res = len(re.findall(r'\w+', i))
        if res == 2:
            pass
        else:
            res = i.replace('"', "'").replace("\n", "")
            sen.append(res)

    pas = " ".join(sen)
    para_text = aug.augment(pas)
    return para_text


