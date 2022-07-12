"""Админские диспетчеры"""
from aiogram import types, Dispatcher
from data.config import admins
from keyboards.admin_keyboards import kb_category_for_del_product, kb_workscategory, kb_autocategory, kb_category, \
    kb_edacategory, kb_buildingcategory, kb_homecategory, kb_autopartsategory, kb_otmena, kb_otherscategory
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import bot, dp
from keyboards import client_keyboards
import datetime
from data import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#  Классы машин состояний ----------------------------------------------------------------------------------------------
class FSMProduct(StatesGroup):
    """Класс машины состояний для добавления товаров"""
    category = State()  # состояние для категории
    photo = State()  # состояние для фотографии
    name = State()  # состояние для имени
    description = State()  # состояние для описания
    region = State()  # состояние для Региона
    gorod = State()  # состояние для Города
    contact = State()  # состояние для контактов
    price = State()  # состояние для цены
    userid = State()
    premium = State()
    datatime = State()


#  Отправка адмнского меню и выход из МС--------------------------------------------------------------------------------
async def cm_start(message: types.Message):
    """Отправляет админское меню администратору"""

@dp.message_handler(state="*", commands='Отменить')
@dp.message_handler(Text(equals='Отменить', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    """Выход из машины состояния если пользователь передумал"""
#    if str(message.from_user.id) in admins:
    current_state = await state.get_state()  # узнаем текущее состояние
        #  если  не находимся в машине состояние ни чего не делаем
    if current_state is None:
        return
        #  иначе завершаем машину состояния
    await state.finish()
    await message.reply('Вы отменили действие', reply_markup=client_keyboards.kb_client)


#  Добавление нового продукта в категорию-------------------------------------------------------------------------------
async def add_new_product(message: types.Message):
    """Запускает процесс добавления нового товара в БД"""
    print(message.from_user.id)
    counter = await sqlite_db.sql_loads_user_stats(message.from_user.id)
    print(counter[0])
    if counter is None or counter[0] <= 5:
        await message.reply('Выберите пожалуйста категорию⬇️ \n Вы всегда можете отменить действие, нажав "Отменить"', reply_markup=kb_category)
    else:
        await message.reply('На данный момент допустимо не более 5 публикаций с одного аккаунта.️', reply_markup=kb_category)

async def callback_add_new_product_category_automobili(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию',
                           reply_markup=kb_autocategory)
    await FSMProduct.category.set()


async def callback_add_new_product_category_autoparts(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию',
                           reply_markup=kb_autopartsategory)
    await FSMProduct.category.set()


async def callback_add_new_product_category_worksell(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию',
                           reply_markup=kb_workscategory)
    await FSMProduct.category.set()


async def callback_add_new_product_category_edasell(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию',
                           reply_markup=kb_edacategory)
    await FSMProduct.category.set()


async def callback_add_new_product_category_buildingssell(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию',
                           reply_markup=kb_buildingcategory)
    await FSMProduct.category.set()


async def callback_add_new_product_category_homesell(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию',
                           reply_markup=kb_homecategory)
    await FSMProduct.category.set()

async def callback_add_new_product_category_otherssell(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Выбирите субкатегорию',
                           reply_markup=kb_otherscategory)
    await FSMProduct.category.set()


async def callback_add_new_product(callback_query: types.CallbackQuery, state: FSMContext):
    """Функция для выяснения в какую категорию вносить изменения"""
    global category
    category = callback_query.data.replace('sell ', '')
    async with state.proxy() as data:
        data['category'] = category
    await FSMProduct.next()
    await bot.send_message(chat_id=callback_query.from_user.id, text='Теперь отправьте фото⬇️', reply_markup=kb_otmena)


async def load_photo(message: types.Message, state: FSMContext):
    """Ловит фото продукта"""
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMProduct.next()
    await message.reply('Теперь введите название⬇️', reply_markup=kb_otmena)

@dp.message_handler(lambda message: not len(message.text) <= 20, state=FSMProduct.name)
async def process_description_toobig(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Слишком длинное название, по правилам допускается не более 20 символов.", reply_markup=kb_otmena)


async def load_name(message: types.Message, state: FSMContext):
    """Ловит название продукта"""
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMProduct.next()
    await message.reply('Введи описание⬇️', reply_markup=kb_otmena)

@dp.message_handler(lambda message: not len(message.text) <= 100, state=FSMProduct.description)
async def process_description_toobig(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Слишком длинное описание, по правилам допускается не более 80 символов.", reply_markup=kb_otmena)

async def load_description(message: types.Message, state: FSMContext):
    """Ловит описание продукта"""
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMProduct.region.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY", "DC")

    await message.reply('Теперь укажи ШТАТ⬇️', reply_markup=markup)

@dp.message_handler(lambda message: message.text not in ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY", "DC"], state=FSMProduct.region)
async def process_age_invalid(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Введен неверный штат.")


async def load_region(message: types.Message, state: FSMContext):
    """Ловит описание продукта"""
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMProduct.gorod.set()
    await message.reply('Теперь укажи Город⬇️', reply_markup=kb_otmena)

@dp.message_handler(lambda message: not len(message.text) <= 20, state=FSMProduct.gorod)
async def process_description_toobig(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Слишком длинное название города, не более 20 символов", reply_markup=kb_otmena)



async def load_gorod(message: types.Message, state: FSMContext):
    """Ловит описание продукта"""
    async with state.proxy() as data:
        data['gorod'] = message.text
    await FSMProduct.contact.set()
    await message.reply('Теперь укажи Контактные данные⬇️', reply_markup=kb_otmena)

@dp.message_handler(lambda message: not len(message.text) <= 30, state=FSMProduct.contact)
async def process_description_toobig(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Слишком много букв в контактах, не более 30 символов", reply_markup=kb_otmena)

async def load_contact(message: types.Message, state: FSMContext):
    """Ловит описание продукта"""
    async with state.proxy() as data:
        data['contact'] = message.text
    await FSMProduct.price.set()
    await message.reply('Теперь укажи цену⬇️', reply_markup=kb_otmena)

@dp.message_handler(lambda message: not len(message.text) <= 15, state=FSMProduct.price)
async def process_summa_invalid(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Введена неверная сумма, не более 15 символов.", reply_markup=kb_otmena)

@dp.message_handler(lambda message: len(message.text) <= 15, state=FSMProduct.price)
async def load_price(message: types.Message, state: FSMContext):
    """Ловит цену продукта"""
    async with state.proxy() as data:
        data['price'] = str(message.text)
        data['userid'] = str(message.from_user.id)
        data['premium'] = int('0')
        data['datatime'] = datetime.datetime.now()
        #  вызываем функцию сохранения данных в БД
    await sqlite_db.sql_add_product(state, message.from_user.id)
    await message.answer('Продукт успешно добавлен!', reply_markup=client_keyboards.kb_client)
    await state.finish()




#  Реализация удаления продукта-----------------------------------------------------------------------------------------
async def delete_product(message: types.Message):
    """Хендлер для команды удалить продукт"""
    if str(message.from_user.id) in admins:
        await message.reply('Выберите пожалуйста категорию⬇️', reply_markup=kb_category_for_del_product)


async def show_all_products_from_category_for_del(callback_query: types.CallbackQuery):
    """
        Хендлер для отображения всех продуктов из выбранной
        категории, с кнойкой 'удалить' под каждым продуктом
    """
    global category_del_product
    category_del_product = callback_query.data.replace('choice_category ', '')
    read = await sqlite_db.sql_loads_all_products_from_category(category_del_product)
    for ret in read:
        await bot.send_photo(callback_query.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
        await bot.send_message(callback_query.from_user.id, text='⬇⬇⬇', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del_product {category_del_product}${ret[1]}')))





#  Регистрация хендлеров------------------------------------------------------------------------------------------------
def register_handlers_admin(dp: Dispatcher):
    """
        Функция регистратор админских диспетчеров, вызывается из main.py
    """
    dp.register_message_handler(cm_start, commands=['админ'])
    dp.register_message_handler(add_new_product, Text(startswith=['Добавить объявление']), state=None)
    dp.register_callback_query_handler(callback_add_new_product,
                                       lambda x: x.data.startswith('sell '),
                                       state=FSMProduct.category)
    # АВТОМОБИЛИ
    dp.register_callback_query_handler(callback_add_new_product_category_automobili,
                                       lambda x: x.data == 'automobilisell')
    # АВТОЗАПЧАСТИ
    dp.register_callback_query_handler(callback_add_new_product_category_autoparts,
                                       lambda x: x.data == 'autopartssell')

    # Услуги
    dp.register_callback_query_handler(callback_add_new_product_category_worksell,
                                       lambda x: x.data == 'worksell')
    dp.register_callback_query_handler(callback_add_new_product_category_otherssell,
                                       lambda x: x.data == 'others')

    dp.register_callback_query_handler(callback_add_new_product_category_edasell, lambda x: x.data == 'edasell'),
    dp.register_callback_query_handler(callback_add_new_product_category_homesell, lambda x: x.data == 'homesell'),
    dp.register_callback_query_handler(callback_add_new_product_category_buildingssell, lambda x: x.data == 'buildingsell'),
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMProduct.photo),
    dp.register_message_handler(load_name, state=FSMProduct.name),
    dp.register_message_handler(load_description, state=FSMProduct.description),
    dp.register_message_handler(load_region, state=FSMProduct.region),
    dp.register_message_handler(load_gorod, state=FSMProduct.gorod),
    dp.register_message_handler(load_contact, state=FSMProduct.contact),
    dp.register_message_handler(load_price, state=FSMProduct.price),
    dp.register_message_handler(delete_product, Text(startswith=['Удалить продукт'])),
    dp.register_callback_query_handler(show_all_products_from_category_for_del,
                                       lambda x: x.data.startswith('choice_category')),

