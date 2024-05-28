import joblib
import numpy as np

def PredictPaymentDue(jsonData):
    values = list(jsonData.values())

    # Convert the list of values to a NumPy array
    data = np.array(values)

    load_model = joblib.load('./trained_model.pkl')
    predict = load_model.predict([data])
    return predict



def result():
    jsonData = {
    "payment1":200,
    "payment2":300,
    "payment3":400,
    "payment4":500,
    "payment5":600
    }
    result = PredictPaymentDue(jsonData)
    print(result)

result()