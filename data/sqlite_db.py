"""Модуль для работы с БД бота"""
import sqlite3 as sq


def sql_start():
    """
        Функция создания БД или подключение к ней
        если она уже создана
    """
    global base, cur
    #  подключение к БД
    base = sq.connect('bakery_db.db')
    #  курсор для взаимодействия с БД
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    #  создаем Таблицу юзеров
    base.execute('CREATE TABLE IF NOT EXISTS users(userid INTEGER primary key, nickname TEXT, email TEXT, counter INTEGER, reputation INTEGER, cart text, premium INTEGER, ban INTEGER, nomer INTEGER)')
    #  создаем Таблицы в БД, в которую будем вносить данные
    base.execute('CREATE TABLE IF NOT EXISTS auto(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')

    base.execute('CREATE TABLE IF NOT EXISTS Audi(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Buick(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS BMW(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Cadillac(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Chevrolet(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Chrysler(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Dodge(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Ford(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS GMC(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Honda(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Hyundai(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Infinity(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Jaguar(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Jeep(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Lexus(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Lincoln(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Mercedes(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Mercury(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Mitsubishi(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Nissan(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Plymouth(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Tesla(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Toyota(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Others(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')

    base.execute('CREATE TABLE IF NOT EXISTS Audiparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Buickparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS BMWparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Cadillacparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Chevroletparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Chryslerparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Dodgeparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Fordparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS GMCparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Hondaparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Hyundaiparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Infinityparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Jaguarparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Jeepparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Lexusparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Lincolnparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Mercedesparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Mercuryparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Mitsubishiparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS parts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Plymouthparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Teslaparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Toyotaparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS Othersparts(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')


    base.execute('CREATE TABLE IF NOT EXISTS eda(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS opteda(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS viezdpovara(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')

    base.execute('CREATE TABLE IF NOT EXISTS construction(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS arenda(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS commerc(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')

    base.execute('CREATE TABLE IF NOT EXISTS bitovaya(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS interior(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS posuda(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')

    #Раздел работы
    base.execute('CREATE TABLE IF NOT EXISTS handymanwork(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS driverwork(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS runnerwork(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')
    base.execute('CREATE TABLE IF NOT EXISTS itwork(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT , userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')

    #Другое
    base.execute('CREATE TABLE IF NOT EXISTS other(img TEXT, name TEXT, description TEXT, region TEXT, gorod TEXT, contact TEXT, price TEXT, userid INTEGER, premium INTEGER, date INTEGER, nomer integer primary key autoincrement)')

    #  сохраняем изменения
    base.commit()


async def sql_add_product(state, userid):
    """Функция добавления новой продукта в выбранную категорию"""
    async with state.proxy() as data:
        cur.execute(f'INSERT INTO {data["category"]} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, null)', tuple(data.values())[1:])
        cur.execute(
            f'INSERT INTO users (userid, counter) VALUES ({userid}, 1) ON CONFLICT (userid) DO UPDATE SET counter = counter + 1')
        base.commit()



async def sql_add_new_item_in_gallery(state):
    """Функция добавления новой картинки в галерею"""
    async with state.proxy() as data:
        cur.execute('INSERT INTO gallery VALUES (?, ?)', tuple(data.values()))
        base.commit()


async def sql_add_new_item_in_timetable(state):
    """Функция добавления нового расписания"""
    async with state.proxy() as data:
        cur.execute('INSERT INTO timetable VALUES (?)', tuple(data.values()))
        base.commit()


async def sql_loads_all_products_from_category(category):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    return cur.execute(f'SELECT * FROM {category}').fetchall()

async def sql_loads_concrect_products_from_category(category, name):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    return cur.execute(f'SELECT userid from {category} WHERE name = {name}')

async def sql_loads_users_products_from_category(category, userid):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    return cur.execute(f'SELECT * from {category} WHERE userid = "{userid}"').fetchall()

async def sql_loads_user_stats(userid):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    return cur.execute(f'SELECT counter from users WHERE userid = "{userid}"').fetchone()

async def sql_loads_ban(userid):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    return cur.execute(f'SELECT ban from users WHERE userid="{userid}"').fetchone()

async def testuserid(userid):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    return cur.execute(f'SELECT * from users WHERE userid="{userid}"').fetchall()


async def sql_set_ban(userid):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    cur.execute(f'INSERT INTO users (userid, ban) VALUES ("{userid}", 1)')
    base.commit()

async def sql_set_unban(userid):
    """Возвращает все продукты из категории хлеб которые есть в бд"""
    cur.execute(f'INSERT INTO users (userid, ban, counter) VALUES ("{userid}", 0, 0)')
    base.commit()

async def sql_check_block(userid):
    return cur.execute(f'SELECT ban FROM users WHERE userid = "{userid}"').fetchone()

async def sql_loads_all_gallery():
    """Возвращает все значения из галереи которые есть в бд"""
    return cur.execute('SELECT * FROM gallery').fetchall()


async def sql_loads_last_timetable():
    """Возвращает актуальное расписание из бд"""
    return cur.execute('SELECT * FROM timetable').fetchall()[-1]


async def sql_delete_product(data):
    """Удаление хлеба из БД"""
    p1 = data.split('$')[0]
    p2 = data.split('$')[1]
    p3 = data.split('$')[2]
    cur.execute(f'DELETE FROM {p1} WHERE nomer = {p2}')
    cur.execute(
        f'INSERT INTO users (userid, counter) VALUES ({p3}, 1) ON CONFLICT (userid) DO UPDATE SET counter = counter - 1')
    base.commit()


async def sql_delete_from_gallery(description):
    """Удаление элемента из галереи"""
    cur.execute('DELETE FROM gallery WHERE description == ?', (description,))
    base.commit()
