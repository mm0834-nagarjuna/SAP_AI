import os
from flask import Flask, request
from pricepredict import getPrice
from cfenv import AppEnv
from hdbcli import dbapi

env = AppEnv()
hana_service = 'hana'
hana = env.get_service(label=hana_service)

app = Flask(__name__)
port = int(os.environ.get('PORT', 4000))

@app.route('/')
def hello():
    admin_conn = dbapi.connect(address=hana.credentials['host'],
                             port=int(hana.credentials['port']),
                             user=hana.credentials['user'],
                             password=hana.credentials['password'],
                             encrypt='true',
                             sslTrustStore=hana.credentials['certificate'])


    cursor = admin_conn.cursor()

    cursor.execute(f'select * from C640464A1B8A45D88D1A6C3F3CCDDCB0.MY_BOOKSHOP_TELECOM_CHURN')
    result = cursor.fetchall()

    return f"Hi this  Page belongs to the Insurance price prediction based on the client AGE, SEX, BMI, CHILDREN, SMOKER, the results are {result} "


@app.route('/getPrice', methods=['POST'])
def InsurancePricePredict():
    result = getPrice(request.get_json())
    data = {
        "response" : result
    }
    return data
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
