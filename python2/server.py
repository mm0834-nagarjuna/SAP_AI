import os
from flask import Flask, jsonify, request
from cfenv import AppEnv
from hdbcli import dbapi
import pandas as pd
import numpy as np
import joblib
from PredictionModel import PredictPaymentDue

app = Flask(__name__)
env = AppEnv()

hana_service = 'hana'
hana = env.get_service(label=hana_service)

port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello():
    if hana is None:
        return "Can't connect to HANA service '{}' – check service name?".format(hana_service)
    else:
        conn = dbapi.connect(address='c31acc17-042a-42e7-98cd-dd50887ae1f2.hana.trial-us10.hanacloud.ondemand.com',
                             port=443,
                             user='C640464A1B8A45D88D1A6C3F3CCDDCB0_6S8IFQDZ2UJW49SRBLUQ6HREC_RT',
                             password='Ln4NpyvSn3i.C2JIpyHBc0nZUO2wQ2MRl3RRZVkeEJngAFDjmnOQC3495RHpUNxITE4WWRLV2Wzbft_wvsTQTBFVa8LSv8D3K5lw.t7KjK84Sv89wBXhV41__oZViIHn',
                             encrypt='true',
                             sslTrustStore=hana.credentials['certificate'])

        cursor = conn.cursor()
        cursor.execute('select * from C640464A1B8A45D88D1A6C3F3CCDDCB0.MY_BOOKSHOP_TELECOM_CHURN')
        result = cursor.fetchall()
    
    
        # Convert to pandas DataFrame
        df = pd.DataFrame(result)
        cursor.close()
        conn.close()

        return  str(df)








predictValues = []    
@app.route('/predict', methods=["POST"] )
def result():
    
    result = PredictPaymentDue(request.get_json())
    return list(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
