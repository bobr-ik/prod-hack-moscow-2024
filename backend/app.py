from data.orm import SyncORM
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SyncORM.create_table()
SyncORM.insert_data()

# @app.route('/', methods=['GET'])
# def hello_world():
#     data = request.args.get('id')
#     data = 1
#     return jsonify({'site': render_template('temp1.html', data=SyncORM.select_data(data)), 'data': data})


@app.route('/get_user_history', methods=['GET'])
def get_user_history():
    lender_tg = request.args.get('lender_tg')
    debtor_tg = request.args.get('debtor_tg')
    return jsonify(SyncORM.get_user_history(lender_tg, debtor_tg))


@app.route('/get_user_debts', methods=['GET'])
def get_user_debts():
    lender_tg = request.args.get('lender_tg')
    return jsonify(SyncORM.get_user_debts(lender_tg))


@app.route('/insert_debt', methods=['POST'])
def insert_debt():
    lender_tg = request.args.get('lender_tg')
    debtor_tg = request.args.get('debtor_tg')
    amount = request.args.get('amount')
    event_name = request.args.get('event_name')
    event_date = request.args.get('event_date')
    return jsonify(SyncORM.insert_debt(lender_tg, debtor_tg, amount, event_name, event_date))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)