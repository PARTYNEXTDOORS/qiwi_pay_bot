from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btnTopUp = InlineKeyboardButton(text='Пополнить', callback_data='top_up')
topUpMenu = InlineKeyboardMarkup(row_width=1)
topUpMenu.insert(btnTopUp)


def buy_menu(isurl=True, url='', bill=''):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isurl:
        btnUrlQiwi = InlineKeyboardButton(text='Ссылка на оплату', url=url)
        qiwiMenu.insert(btnUrlQiwi)

    btnCheckQiwi = InlineKeyboardButton(text='Проверить оплату',
                                        callback_data='check_'+bill)
    qiwiMenu.insert(btnCheckQiwi)
    return qiwiMenu
