from starlette.responses import RedirectResponse
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
# import keras
import joblib
import sklearn


app = FastAPI()

# cnn_model = keras.models.load_model('model/cnn_final.h5')
tfidf_model = joblib.load('model/tfidf_final.pkl')
rf_model = joblib.load('model/rf_final.pkl')
svm_model = joblib.load('model/svm_final.pkl')
tokenizer_model = joblib.load('model/tokenizer.pkl')

class Text(BaseModel):
  method: str
  text: str

@app.get('/')
def index():
  return RedirectResponse(url='/docs')

@app.post('/predict')
def predict(data: Text):
  tfidf_transform = tfidf_model.transform([data.text])
  if data.method == 'rf':
    res = rf_model.predict_proba(tfidf_transform)[0]
  elif data.method == 'svm':
    res = svm_model.predict_proba(tfidf_transform)[0]
  predict = dict({"negatif":res[0]*100, "positif":res[1]*100})
  return {
    "status":True,
    "message":"success",
    "probability":predict,
    "prediction":"positif" if predict["positif"] > predict["negatif"] else "negatif"
  } 