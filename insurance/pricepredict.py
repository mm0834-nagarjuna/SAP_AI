import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler


model = joblib.load('insurance_model.pkl')
Sc = StandardScaler()

def getPrice(jsonData):
    
    # Check if jsonData is not already a list
    if isinstance(jsonData, dict):
        jsonData = [jsonData]
    
    df = pd.DataFrame(jsonData)
    print(df)
    df = df.drop(['region'], axis=1)
    sex_mapping = {'male':1 , 'female':0}
    smoker_mapping = {'yes':1, 'no':0}
    df['sex'] = df['sex'].map(sex_mapping)
    df['smoker'] = df['smoker'].map(smoker_mapping)

    X = df.iloc[:,:-1].values
    Y = df.iloc[:,-1].values

    res = model.predict(X)
    print(res)
    return list(res)

    
    
# 61,female,29.07,0,yes
# 21,female,25.8,0,no
JsonData = [{
      "age": 52,
      "sex": "male",
      "bmi": 30.2,
      "children": 1,
      "smoker": "no",
      "region": "southwest",
      "charges": 9724
    },
    {
      "age": 47,
      "sex": "female",
      "bmi": 29.37,
      "children": 1,
      "smoker": "no",
      "region": "southeast",
      "charges": 8547
    },
    {
      "age": 48,
      "sex": "male",
      "bmi": 40.565,
      "children": 2,
      "smoker": "yes",
      "region": "northwest",
      "charges": 45702
    },
    {
      "age": 61,
      "sex": "male",
      "bmi": 38.38,
      "children": 0,
      "smoker": "no",
      "region": "northwest",
      "charges": 12950
    },
    {
      "age": 51,
      "sex": "female",
      "bmi": 18.05,
      "children": 0,
      "smoker": "no",
      "region": "northwest",
      "charges": 9644
    },
    {
      "age": 34,
      "sex": "male",
      "bmi": 21.375,
      "children": 0,
      "smoker": "no",
      "region": "northeast",
      "charges": 4500
    } ]
    

getPrice(JsonData)