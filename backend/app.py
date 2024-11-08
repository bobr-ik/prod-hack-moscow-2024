from data.orm import SyncORM
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flasgger import Flasgger, swag_from
from aiogram import Bot, Dispatcher, Router     
from bot.config import settings
import asyncio
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from bot.handlers import rt
app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Мой API", "uiversion": 3}

flasgger = Flasgger(app)
CORS(app)

SyncORM.create_table()
SyncORM.insert_data()

# @app.route('/', methods=['GET'])
# def hello_world():
#     data = request.args.get('id')
#     data = 1
#     return jsonify({'site': render_template('temp1.html', data=SyncORM.select_data(data)), 'data': data})


@app.route('/get_user_history', methods=['GET'])
@swag_from("users.yml")
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

dp = Dispatcher()
bot = Bot(settings.TOKEN)

async def main():
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    app.run(host='0.0.0.0', port=5000)