"""Админские клавиатуры"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Клавиши отмены действий "Отменить"
kb_otmena = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
button_otmena = KeyboardButton('Отменить')
kb_otmena.row(button_otmena)


#  callback кнопки для категорий продукции
kb_category = InlineKeyboardMarkup().add(InlineKeyboardButton('Автомобили', callback_data='automobilisell')). \
    add(InlineKeyboardButton('Автозапчасти', callback_data='autopartssell')). \
    add(InlineKeyboardButton('Товары для дома', callback_data='homesell')). \
    add(InlineKeyboardButton('Недвижимость', callback_data='buildingsell')). \
    add(InlineKeyboardButton('Услуги', callback_data='worksell')). \
    add(InlineKeyboardButton('Еда', callback_data='edasell')). \
    add(InlineKeyboardButton('Прочее', callback_data='othersell')). \
    add(InlineKeyboardButton('Отменить', callback_data='Отменить'))

#Для админки:
kb_edacategory = InlineKeyboardMarkup().add(InlineKeyboardButton('Домашняя кухня', callback_data='sell eda')). \
    add(InlineKeyboardButton('Оптовая кухня', callback_data='sell opteda')). \
    add(InlineKeyboardButton('Выездные повара', callback_data='sell viezdpovara'))

kb_buildingcategory = InlineKeyboardMarkup().add(InlineKeyboardButton('Продажа недвижимости', callback_data='sell construction')). \
    add(InlineKeyboardButton('Аренда недвижимости', callback_data='sell arenda')). \
    add(InlineKeyboardButton('Коммерческая аренда', callback_data='sell commerc'))

kb_homecategory = InlineKeyboardMarkup().add(InlineKeyboardButton('Бытовая техника', callback_data='sell bitovaya')). \
    add(InlineKeyboardButton('Интерьер', callback_data='sell interior')). \
    add(InlineKeyboardButton('Посуда', callback_data='sell posuda'))

kb_autocategory = InlineKeyboardMarkup().add(InlineKeyboardButton('Audi', callback_data='sell Audi')). \
    add(InlineKeyboardButton('Buick', callback_data='sell Buick')). \
    add(InlineKeyboardButton('Cadillac', callback_data='sell Cadillac')). \
    add(InlineKeyboardButton('Chevrolet', callback_data='sell Chevrolet')). \
    add(InlineKeyboardButton('Chrysler', callback_data='sell Chrysler')). \
    add(InlineKeyboardButton('Dodge', callback_data='sell Dodge')). \
    add(InlineKeyboardButton('Ford', callback_data='sell Ford')). \
    add(InlineKeyboardButton('GMC', callback_data='sell GMC')). \
    add(InlineKeyboardButton('Honda', callback_data='sell Honda')). \
    add(InlineKeyboardButton('Infinity', callback_data='sell Infinity')). \
    add(InlineKeyboardButton('Jaguar', callback_data='sell Jaguar')). \
    add(InlineKeyboardButton('Jeep', callback_data='sell Jeep')). \
    add(InlineKeyboardButton('Lexus', callback_data='sell Lexus')). \
    add(InlineKeyboardButton('Lincoln', callback_data='sell Lincoln')). \
    add(InlineKeyboardButton('Mercedes', callback_data='sell Mercedes')). \
    add(InlineKeyboardButton('Mercury', callback_data='sell Mercury')). \
    add(InlineKeyboardButton('Nissan', callback_data='sell Nissan')). \
    add(InlineKeyboardButton('Plymouth', callback_data='sell Plymouth')). \
    add(InlineKeyboardButton('Tesla', callback_data='sell Tesla')). \
    add(InlineKeyboardButton('Toyota', callback_data='sell Toyota')). \
    add(InlineKeyboardButton('Others', callback_data='sell Others'))


kb_autopartsategory = InlineKeyboardMarkup().add(InlineKeyboardButton('Audi', callback_data='sell Audiparts')). \
    add(InlineKeyboardButton('Buick', callback_data='sell Buickparts')). \
    add(InlineKeyboardButton('BMW', callback_data='sell BMWparts')). \
    add(InlineKeyboardButton('Cadillac', callback_data='sell Cadillacparts')). \
    add(InlineKeyboardButton('Chevrolet', callback_data='sell Chevroletparts')). \
    add(InlineKeyboardButton('Chrysler', callback_data='sell Chryslerparts')). \
    add(InlineKeyboardButton('Dodge', callback_data='sell Dodgeparts')). \
    add(InlineKeyboardButton('Ford', callback_data='sell Fordparts')). \
    add(InlineKeyboardButton('GMC', callback_data='sell GMCparts')). \
    add(InlineKeyboardButton('Honda', callback_data='sell Hondaparts')). \
    add(InlineKeyboardButton('Hyundai', callback_data='sell Hyundaiparts')). \
    add(InlineKeyboardButton('Infinity', callback_data='sell Infinityparts')). \
    add(InlineKeyboardButton('Jaguar', callback_data='sell Jaguarparts')). \
    add(InlineKeyboardButton('Jeep', callback_data='sell Jeepparts')). \
    add(InlineKeyboardButton('Lexus', callback_data='sell Lexusparts')). \
    add(InlineKeyboardButton('Lincoln', callback_data='sell Lincolnparts')). \
    add(InlineKeyboardButton('Mercedes', callback_data='sell Mercedesparts')). \
    add(InlineKeyboardButton('Mitsubishi', callback_data='sell Mitsubishiparts')). \
    add(InlineKeyboardButton('Mercury', callback_data='sell Mercuryparts')). \
    add(InlineKeyboardButton('Nissan', callback_data='sell Nissanparts')). \
    add(InlineKeyboardButton('Plymouth', callback_data='sell Plymouthparts')). \
    add(InlineKeyboardButton('Tesla', callback_data='sell Teslaparts')). \
    add(InlineKeyboardButton('Toyota', callback_data='sell Toyotaparts')). \
    add(InlineKeyboardButton('Others', callback_data='sell Othersparts'))

kb_workscategory = InlineKeyboardMarkup().add(InlineKeyboardButton('HandyMan', callback_data='sell handymanwork')). \
    add(InlineKeyboardButton('Driver', callback_data='sell driverwork')). \
    add(InlineKeyboardButton('Runner', callback_data='sell runnerwork')). \
    add(InlineKeyboardButton('IT', callback_data='sell itwork'))

kb_otherscategory = InlineKeyboardMarkup().add(InlineKeyboardButton('Прочее', callback_data='sell others'))

kb_category_for_del_product = InlineKeyboardMarkup().add(InlineKeyboardButton('Автомобили',
                                                                              callback_data='choice_category auto')). \
    add(InlineKeyboardButton('Автозапчасти', callback_data='choice_category autoparts')). \
    add(InlineKeyboardButton('Товары для дома', callback_data='choice_category home')). \
    add(InlineKeyboardButton('Недвижимость', callback_data='choice_category buildings')). \
    add(InlineKeyboardButton('Услуги', callback_data='choice_category work')). \
    add(InlineKeyboardButton('Еда', callback_data='choice_category eda')). \
    add(InlineKeyboardButton('Прочее', callback_data='choice_category others'))
