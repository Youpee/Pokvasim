# Pokvasim?
# Не забудь скачать этот репозиторий
## Инструкция по созданию бота
1. Переходишь в бота [BotFather](https://t.me/botfather)
2. ![Opa](https://i.ibb.co/WznWf1q/20230105-123904.png)
3. ![Конец](https://i.ibb.co/PjfFw8p/20230105-124104.png)
4. О нет я спалил токен😜

## Инструкция настройки ботяры
1. Открыть config.json
2. Посмотреть таблицу ниже

Название переменной  | Чему равна
----------------|----------------------
API_TOKEN      | Токен твоего бота. `string`
CHANNEL_ID      | Канал с которого будет считывать бот сообщения, по дефолту (-1001870582703). `int`
YOUR_ID  | Ваш айди, можно узнать переслав [боту](https://t.me/getmyid_bot) любое сообщение. `int`

## Запуск для ПК
1. [Скачать](https://www.python.org/downloads/) и установить Python
2. Открыть консоль, перейти по пути где находиться папка release(ели не шаришь как перейти по пути, вот [ссылка](https://comp-security.net/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D0%B9%D1%82%D0%B8-%D0%B2-%D0%BF%D0%B0%D0%BF%D0%BA%D1%83-%D0%B8%D0%BB%D0%B8-%D0%BD%D0%B0-%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9-%D0%B4%D0%B8%D1%81%D0%BA/)), написать в консоль `python3 main.py`
3. Ботяра остановиться только при закрытии консоли или за исключения(он напишет что делать в консоль😘)
4. Если вылетит ошибка `No module named 'requests'`, напиши в консоль `pip install requests`

## Запуск на Android(яблока не будет😊)
1. [Скачать](https://play.google.com/store/apps/details?id=com.termux) Termux(это мини линукс консоль)
2. Установить Python с помощю команды `pkg install python`
3. Перейти в папку release(проверь с помощю комады `pwd` в какой ты сейчас директории), написать в консоль `python3 main.py`
4. Короче что-то не работает, хз. Запуск на Android отменяется на неопределённое время, наверное завтра будет🤗

## Закончил?
Запускай бота и отправляй боту любой тип сообщений, и он их перешлёт в общий канал с ботами
