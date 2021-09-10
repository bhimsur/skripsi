from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .router import home, prediction, preprocessing

app = FastAPI()
app.include_router(home.router)
app.include_router(prediction.router)
app.include_router(preprocessing.router)
app.mount('/public', StaticFiles(directory='app/public'), name='public')
