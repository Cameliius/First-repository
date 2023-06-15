import sqlite3
import logging

logging.basicConfig(level=logging.INFO)


class User:
    def __init__(self, name, surename, gender):
        self.name = name
        self.surname = surename
        self.gender = gender


def create_table_user(cursor):
    query = """
    CREATE TABLE IF NOT EXISTS User(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(70) NOT NULL,
    surname VARCHAR(70) NOT NULL,
    gender VARCHAR(70) DEFAULT 'M'
    );
    """
    cursor.execute(query)
    logging.info('Таблица Users успешно добавлена!')


def drop_table_user(cursor):
    query = """
    DROP TABLE IF EXISTS User;
    """
    cursor.execute(query)
    logging.info('Таблица User удалена!')


def add_user(cursor, user):
    query = """
    INSERT INTO User(name, surname, gender) VALUES (?, ?, ?)
    """
    cursor.execute(query, (user.name, user.surname, user.gender))
    logging.info(f'Пользователь {user.name} был успешно добавлен!')


def get_users_list(cursor):
    query = """
    SELECT * FROM User;
    """
    logging.info('Получение всех пользователей из таблицы User!')
    return cursor.execute(query).fetchall()


def get_users_list_by_gender(cursor, gender):
    query = """
    SELECT * FROM User WHERE gender = ?;
    """
    logging.info(f'Получение всех пользователей из таблицы User {gender} пола!')
    return cursor.execute(query, (gender,)).fetchall()


def get_user_by_id(cursor, id):
    query = """
    SELECT * FROM User WHERE id = ?
    """
    logging.info(f'Был получен пользователь с id:{id}')
    return cursor.execute(query, (id,))


def delete_data(cursor):
    query = """
    DELETE FROM User
    """
    cursor.execute(query)
    logging.info('Данные из таблицы User были удалены')


def delete_data_by_id(cursor, id):
    query = """
    DELETE FROM User WHERE id = ?
    """
    cursor.execute(query, (id,))
    logging.info(f'Данные пользователя с id: {id} были удалены')


def update_user_name(cursor, name):
    query = """
    UPDATE User SET name = ?;
    """
    logging.info('Имя было измененно')
    cursor.execute(query, (name,))


with sqlite3.connect('data.db') as cursor:
    logging.info('Подкоючение к базе данных прошло успешно')
    drop_table_user(cursor)
    create_table_user(cursor)
    add_user(cursor, User('Настя', 'Давыдова', 'Ж'))
    add_user(cursor, User('Петя', 'Петров', 'М'))
    add_user(cursor, User('Женя', 'Жеков', 'М'))
    print(get_users_list(cursor))
    one_data = get_user_by_id(cursor, 2)
    print(one_data)
    update_user_name(cursor, 'name')
    # delete_data(cursor)
    # delete_data_by_id(cursor, 2)
    print(get_users_list(cursor))
    print(get_users_list_by_gender(cursor, 'Ж'))
