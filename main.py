import logging
import random

from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types.message import ContentTypes
from pyqiwip2p import QiwiP2P

import config as cfg
import murkups as nav
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

db = Database('sec_db')
p2p = QiwiP2P(auth_key=cfg.QIWI_TOKEN)


def is_number(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)

        await bot.send_message(
            message.from_user.id, f"Добро пожаловать!"
            f"\nВаш счет: {db.user_money(message.from_user.id)} руб.",
            reply_markup=nav.topUpMenu
            )


@dp.message_handler()
async def bot_mess(message: types.Message):
    if message.chat.type == 'private':
        if is_number(message.text):
            message_money = int(message.text)
            if message_money > - 5:
                comment = str(message.from_user.id) + '_' + str(
                    random.randint(1000, 9999))
                bill = p2p.bill(amount=message_money, lifetime=15,
                                comment=comment)
                db.add_check(message.from_user.id, message_money, bill.bill_id)

                await bot.send_message(message.from_user.id,
                                       f"Вам нужно отправить {message_money}"
                                       f"руб. на счет QIWI\nСсылку:"
                                       f"{bill.pay_url}\nУказав комментарий к"
                                       f"оплате: {comment}",
                                       reply_markup=nav.buy_menu
                                       (url=bill.pay_url), bill=bill.bill_id)
            else:
                await bot.send_message(
                    message.from_user.id,
                    'Минимальная сумма для пополнения 1 руб.'
                    )
        else:
            await bot.send_message(message.from_user.id, 'Введите целое число')


@dp.callback_query_handler(text='top_up')
async def top_up(callback: types.CallbackQuery):
    await bot.delete_message(
        callback.from_user.id,
        callback.message.message_id
        )
    await bot.send_message(
        callback.from_user.id,
        'Введите сумму для пополнения!'
        )


@dp.callback_query_handler(text_contains='check_')
async def check(callback: types.CallbackQuery):
    bill = str(callback.data[6:])
    info = db.get_check(bill)
    if info is not False:
        if str(p2p.check(bill_id=bill).status) == 'PAID':
            user_money = db.user_money(callback.from_user.id)
            money = int(info[2])
            db.set_money(callback.from_user.id, user_money+money)
            await bot.send_message(callback.from_user.id,
                                   'Ваш счет пополнен! Напишите /start')
        else:
            await bot.send_message(callback.from_user.id,
                                   'Вы не оплатили счет!',
                                   reply_markup=nav.buy_menu(False, bill=bill))

    else:
        await bot.send_message(callback.from_user.id, 'Счет не найден')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
