"""Клиентские диспетчеры"""
from aiogram import types, Dispatcher
from keyboards import client_keyboards
from aiogram.dispatcher.filters import Text
from data import sqlite_db
from loader import bot, dp
from data.config import admins
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Комманда /start
async def commands_start(message: types.Message):
    """Приветственный хендлер для команд start и help"""
    #  отдаем клавиатуру при команде /start или /help
    await message.answer('\nПривет! Это бот "Барахолка USA"'
                         '\nВ нашем приложении можно размещать не более 5 товаров с  одного аккаунта'
                         '\nВы всегда можете самостоятельно удалить неактуальные объявления'
                         ''
                         '', reply_markup=client_keyboards.kb_client)
#    else:
#        await message.reply('okey')
    result = await sqlite_db.sql_loads_ban(message.from_user.id)
    if message.from_user.id == 145539070:
        await message.answer('Добро пожаловать в Админ-Панель! Выберите действие на клавиатуре')
        test = await sqlite_db.testuserid(message.from_user.id)
        print(test)
    else:
        if result is None:
            await sqlite_db.sql_set_unban(message.from_user.id)
            entry = await sqlite_db.sql_check_block(message.from_user.id)
            if entry is None:
                await message.answer('Привет, добро пожаловать!')
            elif entry == 1:
                await message.answer('Вы забанены за нарушение правил публикации!')
            else:
                await message.answer('Добро пожаловать на доску объявлений!'
                                     '\n'
                                     '\n'
                                     'Правилами пользования доски объявлений можно ознакомиться перейдя в раздел "Информация - Правила пользования"'
                                     '\n'
                                     '\n'
                                     'Подробные инструкции по добавлению или удалению объявлений находятся в разделе "Информация - Инструкции"'
                                     '\n'
                                     '\n'
                                     'Приятного пользования', reply_markup=client_keyboards.kb_clientinfo)

#async def load_address(message: types.Message):
#    """Хендлер для отображения адреса пекарни"""
#    await message.reply(address[0])
#    await message.answer_location(float(address[1]), float(address[2]))


#async def load_contacts(message: types.Message):
#    """Хендлер для отображения контактов пекарни"""
#    for name, phone in zip(names, phones):
#        await message.answer_contact(phone_number=phone, first_name=name)
#    await message.answer(email)

#Показать категории
async def show_products(message: types.Message):
    """Хендлер для команды 'продукция' отображает категории продукции"""
    await message.reply('Для добавления товара бот вас попросит: Приложить фотографию, Ввести название, Описание, Выбрать штат, Указать город, Контактные данные, цену.'
                        'Выберите пожалуйста категорию', reply_markup=client_keyboards.kb_category_for_show)
#Показать инструкции
async def show_instrukcii(message: types.Message):
    """Хендлер для команды 'продукция' отображает категории продукции"""
    await message.reply('Добавить объявление очень просто, если следовать инструкциям ниже:'
                        '\n'
                        '1) Нажать кнопку: Добавить объявление'
                        '\n'
                        '2) Выбрать категорию и субкатегорию'
                        '\n'
                        '3) Выбрать фотографию и отправить в окно чата'
                        '\n'
                        '4) Ввести название'
                        '\n'
                        '5) Ввести описание'
                        '\n'
                        '6) Выбрать ШТАТ из списка'
                        '\n'
                        '7) Вписать город'
                        '\n'
                        '8) Указать любые удобные контактные данные'
                        '\n'
                        '9) Указать цену'
                        '\n'
                        'На этом добавление закончено, свои объявления можно увидеть в разделе "Мои объявления"',  parse_mode=types.ParseMode.HTML, reply_markup=client_keyboards.kb_client)

#Показать правила
async def show_pravila(message: types.Message):
    """Хендлер для команды 'продукция' отображает категории продукции"""
    await message.reply('Для удобства пользования просим Вас придерживаться следующих правил:'
                        '\n'                      
                        'Указывать свои контактные данные для связи'
                        '\n'
                        'Не выкладывать объявления повторно'
                        '\n'
                        'После продажи или оказания услуги объявление удалять'
                        '\n',  parse_mode=types.ParseMode.HTML, reply_markup=client_keyboards.kb_client)

#Показать поддержку
async def show_support(message: types.Message):
   #Саппорт
    await message.reply('Настоящее приложение разработано для облегчения размещений объявлений о покупки и продажи чего либо.'
                        '\n<b>Текущая версия:</b> <i>1.4 от 06.19.2022</i>'
                        '\n'
                        '\nЕсли вам нравится это приложение, вы всегда можете отправить средства на поддержку проекта:'
                        '\n'
                        '<code>Тbc1qk45fpxn5z5vaxtgtj6cjltm2xhsvjftd2vck07</code>'
                        '\n'
                        '\n<i>Если у вас есть вопросы, или предложения, можете задать написать их в службу поддержки:</i>'
                        '\n'
                        '\n@RaDSupport_bot'
                        '\nСпасибо, что читаете это 😊',  parse_mode=types.ParseMode.HTML, reply_markup=client_keyboards.kb_clientinfo)

#Категория Автомобили
async def show_productsauto(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию', reply_markup=client_keyboards.kb_autocategory_for_show)

#Категория Автозапчастей
async def show_productsautoparts(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию', reply_markup=client_keyboards.kb_autoparts_for_show)

#Категория работы
async def show_productswork(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию', reply_markup=client_keyboards.kb_workscategory_for_show)

#Категория товары для дома
async def show_productshome(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию', reply_markup=client_keyboards.kb_homecategory_for_show)

#Категория дома
async def show_productsbuildings(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию', reply_markup=client_keyboards.kb_buildingcategory_for_show)

#Категория еда
async def show_productseda(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию', reply_markup=client_keyboards.kb_edacategory_for_show)

#Категория другое
async def show_productsothers(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию прочих товаров', reply_markup=client_keyboards.kb_otherscategory_for_show)

#Отобразить товары из категории
async def show_all_products_from_category(callback_query: types.CallbackQuery):
    """Отображает все товары выбранной категории"""
    category = callback_query.data.replace('show ', '')
    read = await sqlite_db.sql_loads_all_products_from_category(category)

    if len(read) >= 1:
        for ret in read:
            await bot.send_photo(callback_query.from_user.id, ret[0], f'.{ret[1]}\nОписание: {ret[2]}\nРегион: {ret[3]}\nГород: {ret[4]}\nКонтакты: {ret[5]}\nЦена: {ret[6]}')
            print(ret[7])
            userid = callback_query.from_user.id
            if userid == int(ret[7]) or str(callback_query.from_user.id) in admins:
                await bot.send_message(callback_query.from_user.id, text='Вы можете удалить это', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить объявление: "{ret[1]}" ?', callback_data=f'del_product {category}${ret[10]}${ret[7]}')))
    else:
        await bot.send_message(callback_query.from_user.id, text='В этой категории ещё нет товаров!')
        #, reply_markup=client_keyboards.kb_category_for_show

#Показать свои объявления
async def show_user_products_from_category(message: types.Message):
    """Отображает все товары выбранной категории"""

    userid = message.from_user.id
    bases = ["Audi", "Buick", "BMW", "Cadillac", "Chevrolet", "Chrysler", "Dodge", "Ford", "GMC", "Honda", "Hyundai",
             "Infinity", "Jaguar", "Jeep", "Lexus", "Lincoln", "Mercedes", "Mercury", "Mitsubishi", "Nissan",
             "Plymouth", "Tesla", "Toyota", "Others", "Audiparts", "Buickparts", "BMWparts", "Cadillacparts",
             "Chevroletparts", "Chryslerparts", "Dodgeparts", "Fordparts", "GMCparts", "Hondaparts", "Hyundaiparts",
             "Infinityparts", "Jaguarparts", "Jeepparts", "Lexusparts", "Lincolnparts", "Mercedesparts", "Mercuryparts",
             "Mitsubishiparts", "parts", "Plymouthparts", "Teslaparts", "Toyotaparts", "Othersparts", "eda", "opteda",
             "viezdpovara", "construction", "arenda", "commerc", "bitovaya", "interior", "posuda", "handymanwork",
             "driverwork", "runnerwork", "itwork", "others"]

    for x in bases:
        read = await sqlite_db.sql_loads_users_products_from_category(x, message.from_user.id)
        for ret in read:
            if len(ret) >= 1 and userid == int(ret[7]):
                await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nРегион: {ret[3]}\nГород: {ret[4]}\nКонтакты: {ret[5]}\nЦена {ret[6]}')
                userid = message.from_user.id
                if userid == int(ret[7]):
                    await bot.send_message(message.from_user.id, text='Вы можете удалить это', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить объявление: "{ret[1]}" ?', callback_data=f'del_product {x}${ret[10]}${ret[7]}')))
#            if len(ret) > 1:
#                await bot.send_message(message.from_user.id, text='Вы ещё не выкладывали товаров')
#                print(read)


#Удалить продукт из базы данных
async def delete_product_from_database(callback_query: types.CallbackQuery):
    """Срабатывает на кнопку удалить, и удаляет соответствующий продукт из БД"""
    data = callback_query.data.replace('del_product ', '')

    await sqlite_db.sql_delete_product(data)
    await bot.send_message(callback_query.from_user.id, text="Товар удалён")

#Отработка заголовков
def register_handlers_client(dp: Dispatcher):
    """
        Функция регистратор клиентских диспетчеров, вызывается из main.py
    """
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(show_products, Text(startswith='Каталог'))
    dp.register_message_handler(show_support, Text(startswith='Информация'))
    dp.register_message_handler(show_pravila, Text(startswith='Правила пользования'))
    dp.register_message_handler(show_instrukcii, Text(startswith='Инструкции'))
    dp.register_message_handler(show_user_products_from_category, Text('Мои объявления'))
    dp.register_callback_query_handler(show_productsauto, lambda x: x.data == 'automobilipomarkam')
    dp.register_callback_query_handler(show_productsautoparts, lambda x: x.data == 'autopartspogruppam')
    dp.register_callback_query_handler(show_productseda, lambda x: x.data == 'edapogruppam')
    dp.register_callback_query_handler(show_productshome, lambda x: x.data == 'homepogruppam')
    dp.register_callback_query_handler(show_productsbuildings, lambda x: x.data == 'buildingspogruppam')
    dp.register_callback_query_handler(show_productswork, lambda x: x.data == 'workpogruppam')
    dp.register_callback_query_handler(show_productsothers, lambda x: x.data == 'otherspogruppam')
    dp.register_callback_query_handler(show_all_products_from_category, lambda x: x.data.startswith('show'))
    dp.register_callback_query_handler(delete_product_from_database,
                                       lambda x: x.data.startswith('del_product'))