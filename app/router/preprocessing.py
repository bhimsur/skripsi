from fastapi import APIRouter
import re
from nltk import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from app.model.input import DataRequest

stemmer = StemmerFactory().create_stemmer()
sw_remover = StopWordRemoverFactory().create_stop_word_remover()

def lowercase(text):
    return text.lower()

def remove_punctuation(text):
    text = re.sub('\n', ' ', text)
    text = re.sub('rt', ' ', text)
    text = re.sub('user', ' ', text)
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', ' ', text)
    text = re.sub(' +', ' ', text)
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    text = re.sub(r'\d+', '', text)
    return text

def remove_whitespace_leading_and_trailing(text):
    return text.strip()

def remove_whitespace_multiple(text):
    return re.sub('\s+', ' ', text.strip())

def remove_single_char(text):
    return re.sub(r'\b(?:\w{,1})\b', '', text)

def remove_stopword(text):
    return sw_remover.remove(text)

def tokenize(text):
    return word_tokenize(text)

def stemming(text):
    return stemmer.stem(text)

@router.post('/preprocessing', tags=['preprocessing'])
def do_preprocessing(request: DataRequest):
    text = request.text
    case_folding = lowercase(text)
    punctuation_removal = remove_punctuation(case_folding)
    text = remove_whitespace_leading_and_trailing(punctuation_removal)
    text = remove_whitespace_multiple(text)
    text = remove_single_char(text)
    tokenizing = tokenize(text)
    stopword_removal = remove_stopword(' '.join(tokenizing))
    word_stemming = stemming(stopword_removal)
    result = word_stemming
    return {
            'request': request.text,
            'result': result,
            'case_folding': case_folding,
            'punctuation_removal': punctuation_removal,
            'tokenizing': tokenizing,
            'stopword_removal': stopword_removal,
            'word_stemming': word_stemming
    }
