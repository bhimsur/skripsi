from starlette.responses import RedirectResponse
from pydantic import BaseModel
from fastapi import FastAPI
import joblib
# import keras
# from keras.preprocessing.sequence import pad_sequences


app = FastAPI()

# cnn_model = keras.models.load_model('model/cnn_final.h5')
tfidf_model = joblib.load('model/tfidf_final.pkl')
rf_model = joblib.load('model/rf_final.pkl')
svm_model = joblib.load('model/svm_final.pkl')
# tokenizer_model = joblib.load('model/tokenizer.pkl')

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
  else:
    return {"status":False, "message":"method not allowed"}
  return {
    "status":True,
    "message":"success",
    "probability":{"negatif":res[0], "positif":res[1]},
    "prediction":"positif" if res[1] > res[0] else "negatif"
  }

# @app.post('/predict/nn')
# def predict_neural_network(data:Text):
#   data_sequences = tokenizer_model.texts_to_sequences([data.text])
#   data_sequences = pad_sequences(data_sequences, maxlen=52)
#   if data.method == 'cnn':
#     res = cnn_model.predict([data_sequences])
#     res = res.tolist()[0][0]
#   else:
#     return {'status':False, 'message':'method not allowed'}

#   if res <= 0.5:
#     negatif = res
#     positif = 1-res
#   else:
#     negatif = 1-res
#     positif = res
    
#   return {
#     'status':True,
#     'message':'success',
#     'probability': {'negatif':negatif, 'positif':positif},
#     'prediction':'positif' if positif > negatif else 'negatif'
#   }