from fastapi import APIRouter
# from keras.preprocessing.sequence import pad_sequences
from app.model.input import DataRequest
from app.util.util import tfidf_model, rf_model, svm_model, mnb_model, bnb_model
# from app.util.util import tfidf_model, rf_model, svm_model, mnb_model, bnb_model, lstm_model, tokenizer_model, cnn_model

router = APIRouter()


def predict(data: DataRequest, model):
    text_input = data.text.lower()
    tfidf_transform = tfidf_model.transform([text_input])
    result = model.predict_proba(tfidf_transform[0])
    return {
        "text": text_input,
        "probability": {"negatif": result[0][0], "positif": result[0][1]},
        "prediction": "positif" if result[0][1] > result[0][0] else "negatif"
    }


# def predict_nn(data: DataRequest, model):
#     text_input = data.text.lower()
#     data_sequences = tokenizer_model.texts_to_sequences([text_input])
#     data_sequences = pad_sequences(data_sequences, maxlen=52)
#     result = model.predict([data_sequences])
#     result = result.tolist()[0][0]

#     if result <= 0.5:
#         negatif = result
#         positif = 1-result
#     else:
#         negatif = 1-result
#         positif = result
#     return {
#         "text": text_input,
#         "probability": {"negatif": negatif, "positif": positif},
#         "prediction": "positif" if positif > negatif else "negatif"
#     }


@router.post("/predict", tags=["Prediction"])
def do_predict(request: DataRequest):
    if request.method == "rf":
        return predict(request, rf_model)
    elif request.method == "svm":
        return predict(request, svm_model)
    elif request.method == "mnb":
        return predict(request, mnb_model)
    elif request.method == "bnb":
        return predict(request, bnb_model)
    # elif request.method == "lstm":
    #     return predict_nn(request, lstm_model)
    # elif request.method == "cnn":
    #     return predict_nn(request, cnn_model)
    else:
        return False
