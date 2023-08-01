from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
from transformers import pipeline
import nltk

tokenizer = AutoTokenizer.from_pretrained("tuner007/pegasus_paraphrase", use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained("tuner007/pegasus_paraphrase")
nlp = pipeline('text2text-generation', model=model, tokenizer=tokenizer, truncation=True)

context = """
Deep learning, including convolutional neural networks (CNNs), a subtype of deep learning, has shown great promise in breast cancer research. CNNs are specifically designed for image analysis tasks and have been extensively used for breast cancer detection, classification, risk prediction, and prognosis. 
"""

def paraphrase_paragraph(sentences):
    # nlp = spacy.load('en_core_web_sm')
    array1 = []
    array2 = []
    
    for i in range(0, len(sentences)-1):
        array1.append(nlp(sentences[i]))
        
    for i in range(len(array1)):
        array2.append(array1[i][0]['generated_text'])
        
    para = ' '.join(array2)
    return para

def paraphrase(context):

    sentences=nltk.sent_tokenize(context)
    # print(sentences)

    array1 = []
    array2 = []

    if len(context) > 100:
        output=paraphrase_paragraph(sentences)
        print(output)
    else:
        result = nlp(context)
        sentence = result[0]['generated_text']
        print(sentence)

