# from keras.models import load_model
from joblib import load

# tokenizer_model = load("/app/resource/tokenizer.pkl")
# lstm_model = load_model("/app/resource/lstm_final.h5")
# cnn_model = load_model("/app/resource/cnn_final.h5")
tfidf_model = load("/app/resource/tfidf_final.pkl")
rf_model = load('/app/resource/rf_final.pkl')
svm_model = load('/app/resource/svm_final.pkl')
bnb_model = load('/app/resource/bnb_final.pkl')
mnb_model = load('/app/resource/mnb_final.pkl')
