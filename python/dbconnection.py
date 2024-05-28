from hdbcli import dbapi
import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

def Logistic_Regression(df):
        X = df.iloc[:,:-1].values
        Y = df.iloc[:,-1].values

        X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
        
        # Sc = StandardScaler()
        # X_train = Sc.fit_transform(X_train)
        # X_test = Sc.fit_transform(X_test)

        # Logistic Regression Model
        Log_R = LogisticRegression(random_state=0)
        Log_R.fit(X_train, Y_train)

        Y_pred = Log_R.predict(X_test)
        np.set_printoptions(precision=2)
        comparison = np.concatenate((Y_pred.reshape(len(Y_pred), 1), Y_test.reshape(len(Y_test), 1)), axis=1)
        print(comparison)
        

      

        # confuse the matrics 
        cm = confusion_matrix(Y_test, Y_pred)
        accuracy = accuracy_score(Y_test, Y_pred)
        print(cm, accuracy)  # 0.8710644677661169

        prediction = Log_R.predict([[3593423,3,5,7,226.3,95,38.47,274.3,109,23.32,242.7,119,10.92,8.2,3,2.21,2]])
        print(prediction)


def RDF(df):
    X = df.iloc[:,:-1].values
    Y = df.iloc[:,-1].values

    # Random Forest Regressor model 
   # split the data into train and test
    X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)


    # feature scaling
    from sklearn.preprocessing import StandardScaler
    Sc = StandardScaler()
    X_train = Sc.fit_transform(X_train)
    X_test = Sc.fit_transform(X_test)

    # Random Forest Model
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=0)
    classifier.fit(X_train, Y_train)

    # predict 
    Y_pred = classifier.predict(X_test)
    np.set_printoptions(precision=2)
    comparison = np.concatenate((Y_pred.reshape(len(Y_pred), 1), Y_test.reshape(len(Y_test), 1)), axis=1)
    print(comparison)

    # confusion of matrics and machine score
    from sklearn.metrics import confusion_matrix,accuracy_score
    print(confusion_matrix(Y_test,Y_pred), accuracy_score(Y_test,Y_pred)) # 0.9460269865067467

    predict = classifier.predict([[4091856,0,0,0,321.1,105,54.59,265.5,122,22.57,180.5,72,8.12,11.5,2,3.11,4]])
    print(predict)


def connect(host,port,user,password):
    admin_conn = dbapi.connect(
        address=host,
        port=port,
        user=user,
        password=password
    )
    print("connection successfull")

    cursor = admin_conn.cursor()

    cursor.execute('select * from C640464A1B8A45D88D1A6C3F3CCDDCB0.MY_BOOKSHOP_TELECOM_CHURN')
    result = cursor.fetchall()
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(result)

    Logistic_Regression(df)
    RDF(df)
   
    admin_conn.close()
    print("Connection closed")

host = 'c31acc17-042a-42e7-98cd-dd50887ae1f2.hana.trial-us10.hanacloud.ondemand.com'
port = 443
user = 'C640464A1B8A45D88D1A6C3F3CCDDCB0_6S8IFQDZ2UJW49SRBLUQ6HREC_RT'
password = 'Ln4NpyvSn3i.C2JIpyHBc0nZUO2wQ2MRl3RRZVkeEJngAFDjmnOQC3495RHpUNxITE4WWRLV2Wzbft_wvsTQTBFVa8LSv8D3K5lw.t7KjK84Sv89wBXhV41__oZViIHn'

connect(host,port,user,password)





