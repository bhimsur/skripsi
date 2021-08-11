from starlette.responses import RedirectResponse
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
import keras
import joblib
import sklearn


app = FastAPI()

cnn_model = keras.models.load_model('model/cnn_final.h5')
tfidf_model = joblib.load('model/tfidf_final.pkl')
rf_model = joblib.load('model/rf_final.pkl')
svm_model = joblib.load('model/svm_final.pkl')
tokenizer_model = joblib.load('model/tokenizer.pkl')

class Text(BaseModel):
  text: str

@app.get('/')
async def index():
  return RedirectResponse(url='/docs')