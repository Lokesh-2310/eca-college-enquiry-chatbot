import pickle
import numpy as np

# Load the trained model from the file
with open('naive_bayes_model1.pkl', 'rb') as model_file:
    loaded_clf = pickle.load(model_file)

# Load the vectorizer
with open('tfidf_vectorizer1.pkl', 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)
    

def cleantext(text):
    text=text.lower()
    print(text)
    arr=np.array([text])
    X_test_tfidf = loaded_vectorizer.transform(arr)
    y_pred = loaded_clf.predict(X_test_tfidf)
    y_pred=str(y_pred[0])
    return y_pred
