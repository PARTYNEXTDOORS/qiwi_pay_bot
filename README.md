<p align="left">
    
<img height="180em" src=https://i.pinimg.com/564x/5e/19/31/5e19312aa89069e9c78348e9618303fa.jpg />

</p>

____

<h1 align="left" id="macropower-title">Телеграм бот для приема платежей на qiwi кошелек</h1>

____

## Описание проекта:
Телеграм бот для приема платежей на киви кошелек. Бот написан на асинхронной библиотеке [Aiogram](https://docs.aiogram.dev/en/latest/telegram/index.html). К проекту подключена база данных [sqlite](https://www.sqlite.org/index.html) в которой харнится информация о юзерах и суммах чеков.

____

## Запуск проекта на локально сервере
Для начала стоит [создать бота](https://chatlabs.ru/botfather-instrukcziya-komandy-nastrojki/). После регистрации бота и получения токена нужно [создать токен в qiwi кошелке](https://qiwi.com/p2p-admin/api).
p.s На данный момент получить qiwi токен нельзя, так их выпуск временно отсановлен. Не переживатйе, можно сделать такого же бота и с постоянной ссылкой для оплаты (скоро будет на гитхабе).
+ склонировать репозиторий
```
git clone git@github.com:PARTYNEXTDOORS/qiwi_pay_bot.git
```
+ установить вирутиальное окружение
```
python -m venv venv`(для Windows)
python3 -m venv env`(для Mac/Linux)
```
+ активировать виртуальное окружение
```
source venv/Script/activate`(для Windows)
source venv/bin/activate`(для Mac/Linux)
```
+ установаить бибилиотеку aiogram
```
pip install aiogram
```
+ установить библиотеку pyqiwip2p
```
pip install pyQiwiP2P
```
+ для работы с бд нужен [SQLiteStudio](https://sqlitestudio.pl/)
+ в файле `config.py` ввести token бота и киви кошелька (если вы собираетесь выкладывать бота в открытый доступ, не забудьте перенести токены в файл `.env`, чтобы скрыть токены)
+ запустить код
```
python main.py
```
