from starlette.responses import RedirectResponse
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
# import keras

app = FastAPI()

# cnn_model = keras.load_model('../model/cnn_final.h5')

class Text(BaseModel):
  text: str

@app.get('/')
async def index():
  return RedirectResponse(url='/docs')