"""Пользовательские клавиатуры"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#  создаем кнопки
button_products = KeyboardButton('Каталог')
button_personal = KeyboardButton('Мои объявления')
button_add = KeyboardButton('Добавить объявление')
button_support = KeyboardButton('Информация')
button_pravila = KeyboardButton('Правила пользования')
button_instrukcii = KeyboardButton('Инструкции')


#  создаем клавиатуру из кнопок вместо обычной
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_clientinfo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_clientwo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_clientwo.row(button_products)


#  добавляем кнопки на клавиатуру в строку
kb_client.row(button_products).row(button_personal).row(button_add).row(button_support)
kb_clientinfo.row(button_pravila).row(button_instrukcii)


#  callback кнопки для категорий продукции
kb_category_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('Автомобили', callback_data='automobilipomarkam')). \
    add(InlineKeyboardButton('Автозапчасти', callback_data='autopartspogruppam')). \
    add(InlineKeyboardButton('Недвижимость', callback_data='buildingspogruppam')). \
    add(InlineKeyboardButton('Товары для дома', callback_data='homepogruppam')). \
    add(InlineKeyboardButton('Еда', callback_data='edapogruppam')). \
    add(InlineKeyboardButton('Услуги', callback_data='workpogruppam')). \
    add(InlineKeyboardButton('Прочее', callback_data='otherspogruppam'))

## CATEGORIES
kb_edacategory_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('Домашняя кухня', callback_data='show eda')). \
    add(InlineKeyboardButton('Оптовая кухня', callback_data='show opteda')). \
    add(InlineKeyboardButton('Выездные повара', callback_data='show viezdpovara'))

kb_buildingcategory_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('Продажа недвижимости', callback_data='show construction')). \
    add(InlineKeyboardButton('Аренда недвижимости', callback_data='show arenda')). \
    add(InlineKeyboardButton('Коммерческая аренда', callback_data='show commerc'))

kb_homecategory_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('Бытовая техника', callback_data='show bitovaya')). \
    add(InlineKeyboardButton('Интерьер', callback_data='show interior')). \
    add(InlineKeyboardButton('Посуда', callback_data='show posuda'))

#SUB AUTO
kb_autocategory_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('Audi', callback_data='show Audi')). \
    add(InlineKeyboardButton('Buick', callback_data='show Buick')). \
    add(InlineKeyboardButton('BMW', callback_data='show BMW')). \
    add(InlineKeyboardButton('Cadillac', callback_data='show Cadillac')). \
    add(InlineKeyboardButton('Chevrolet', callback_data='show Chevrolet')). \
    add(InlineKeyboardButton('Chrysler', callback_data='show Chrysler')). \
    add(InlineKeyboardButton('Dodge', callback_data='show Dodge')). \
    add(InlineKeyboardButton('Ford', callback_data='show Ford')). \
    add(InlineKeyboardButton('GMC', callback_data='show GMC')). \
    add(InlineKeyboardButton('Honda', callback_data='show Honda')). \
    add(InlineKeyboardButton('Hyundai', callback_data='show Hyundai')). \
    add(InlineKeyboardButton('Infinity', callback_data='show Infinity')). \
    add(InlineKeyboardButton('Jaguar', callback_data='show Jaguar')). \
    add(InlineKeyboardButton('Jeep', callback_data='show Jeep')). \
    add(InlineKeyboardButton('Lexus', callback_data='show Lexus')). \
    add(InlineKeyboardButton('Lincoln', callback_data='show Lincoln')). \
    add(InlineKeyboardButton('Mercedes', callback_data='show Mercedes')). \
    add(InlineKeyboardButton('Mercury', callback_data='show Mercury')). \
    add(InlineKeyboardButton('Mitsubishi', callback_data='show Mitsubishi')). \
    add(InlineKeyboardButton('Nissan', callback_data='show Nissan')). \
    add(InlineKeyboardButton('Plymouth', callback_data='show Plymouth')). \
    add(InlineKeyboardButton('Tesla', callback_data='show Tesla')). \
    add(InlineKeyboardButton('Toyota', callback_data='show Toyota')). \
    add(InlineKeyboardButton('Others', callback_data='show Others'))

#SUBAUTOPARTS
kb_autoparts_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('Audi', callback_data='show Audiparts')). \
    add(InlineKeyboardButton('Buick', callback_data='show Buickparts')). \
    add(InlineKeyboardButton('BMW', callback_data='show BMWparts')). \
    add(InlineKeyboardButton('Cadillac', callback_data='show Cadillacparts')). \
    add(InlineKeyboardButton('Chevrolet', callback_data='show Chevroletparts')). \
    add(InlineKeyboardButton('Chrysler', callback_data='show Chryslerparts')). \
    add(InlineKeyboardButton('Dodge', callback_data='show Dodgeparts')). \
    add(InlineKeyboardButton('Ford', callback_data='show Fordparts')). \
    add(InlineKeyboardButton('GMC', callback_data='show GMCparts')). \
    add(InlineKeyboardButton('Honda', callback_data='show Hondaparts')). \
    add(InlineKeyboardButton('Infinity', callback_data='show Infinityparts')). \
    add(InlineKeyboardButton('Jaguar', callback_data='show Jaguarparts')). \
    add(InlineKeyboardButton('Jeep', callback_data='show Jeepparts')). \
    add(InlineKeyboardButton('Lexus', callback_data='show Lexusparts')). \
    add(InlineKeyboardButton('Lincoln', callback_data='show Lincolnparts')). \
    add(InlineKeyboardButton('Mercedes', callback_data='show Mercedesparts')). \
    add(InlineKeyboardButton('Mitsubishi', callback_data='show Mitsubishiparts')). \
    add(InlineKeyboardButton('Mercury', callback_data='show Mercuryparts')). \
    add(InlineKeyboardButton('Nissan', callback_data='show Nissanparts')). \
    add(InlineKeyboardButton('Plymouth', callback_data='show Plymouthparts')). \
    add(InlineKeyboardButton('Tesla', callback_data='show Teslaparts')). \
    add(InlineKeyboardButton('Toyota', callback_data='show Toyotaparts')). \
    add(InlineKeyboardButton('Others', callback_data='show Othersparts'))

# Categories WORK
kb_workscategory_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('HandyMan', callback_data='show handymanwork')). \
    add(InlineKeyboardButton('Driver', callback_data='show driverwork')). \
    add(InlineKeyboardButton('Runner', callback_data='show runnerwork')). \
    add(InlineKeyboardButton('IT', callback_data='show itwork'))

#Sub otro
kb_otherscategory_for_show = InlineKeyboardMarkup().add(InlineKeyboardButton('Прочее', callback_data='show others'))
