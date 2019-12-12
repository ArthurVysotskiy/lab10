import sqlite3
from sqlite3 import Error


# Функція для створення з'єднання до БД 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


# Вибір всіх значень в таблиці tasks
def select_all_dohodu(conn):
    sql = 'SELECT * FROM oblik_dohodiv'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Вибрати доходи з сумою більше 1000
def select_high_sum_dohodu(conn):
    sql = 'SELECT * FROM oblik_dohodiv WHERE summa > 1000'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Створення нового доходу
def create_dohid(conn, dohid):
    sql = ''' INSERT INTO oblik_dohodiv(summa, dzherelo, data)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, dohid)


# Оновлення рядка
def update_data_dohodu(conn, data):
    sql = ''' UPDATE oblik_dohodiv
              SET summa = ?, dzherelo = ?, data = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


# Видалення доходу за його номером
def remove_dohid(conn, remove_dohid):
    sql = ''' DELETE FROM oblik_dohodiv WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, remove_dohid)
    conn.commit()


# Головна функція, яка виконується під час запуску скрипта
def main():

    # Шлях до БД
    database = r"db1.db" 
 
    # Встановлення з'єднання
    conn = create_connection(database)

    # Використовууючи встановлене з'єднання виконуються операції над БД
    with conn:
        print("\nВсі доходи (Номер, сума, джерело, дата)")
        select_all_dohodu(conn)
        print("\nДоходи з сумою більше 1000 (завдання, дата, приорітет)")
        select_high_sum_dohodu(conn)
        print("\nВставка нового рядка...")
        create_dohid(conn, ('1200','Біржа','15-12-2019'))
        print("\nВсі доходи (Номер, сума, джерело, дата)")
        select_all_dohodu(conn)
        print("\nЗміна рядка...")
        update_data_dohodu(conn, ('100','bonus','01-12-2019',1))
        print("\nВсі доходи (Номер, сума, джерело, дата)")
        select_all_dohodu(conn)        
        print("\nВставка нового рядка...")
        create_dohid(conn, ('200','olx','12-12-2019'))
        print("\nВсі доходи (Номер, сума, джерело, дата)")
        select_all_dohodu(conn)
        print("\nВидалення рядка")
        remove_dohid(conn, (2,))
        print("\nВсі доходи (Номер, сума, джерело, дата)")
        select_all_dohodu(conn)
        input('Press ENTER to exit') 
 
if __name__ == '__main__':
    main()