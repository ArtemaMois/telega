import sqlite3

#--------------------ОБНОВЛЕНИЕ БАЗЫ--------------------------------
def update_db(search_name, keys_name, keys):
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''update keyses set keys_name = ?, keys = ? where name = ?'''
    curr.execute(select_query, (keys_name, keys, search_name))
    conn.commit()
    print("Запись успешно обновлена!")

#---------------------------ДОБАВЛЕНИЕ ЗНАЧЕНИИЙ-----------------------
def database(row, name_id, keys_name, keys):
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''insert into keyses(id_row, name, keys_name, keys) VALUES (?, ?, ?, ?)''', (row, name_id, keys_name, keys)
    curr.execute(select_query, (row, name_id, keys_name, keys))
    conn.commit()
    print("Новые значения добавлены!")

#----------------------------ДОБАВЛЕНИЕ НОВЫХ СТРОК В ТАБЛИЦУ------------------------
def new_row(v1,v2,v3):
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''INSERT INTO keyses (name, keys_name, keys) VALUES (?,?,?);'''
    curr.execute(select_query, (v1,v2,v3))
    conn.commit()
    print("Новые строки добавлены!")

#-----------ВЫВОД ДАННЫХ------------------------------------
def output(name):
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''select * from keyses where name = ?'''
    curr.execute(select_query, (name,))
    out = curr.fetchall()
    print("вывел результат")
    return out
    

def sql_read(message):
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    print("Успешно подключено!")
    for ret in curr.execute('SELECT * FROM keyses').fetchall():
        return (message.from_user.id,f'ТЕМА:   {ret[0]}\nОписание: \n{ret[1]}')
    conn.commit()
    
def sql_readall():
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    print("Успешно подключено!")
    return (curr.execute('select * from keyses')).fetchall()


def sql_delete_command(data):
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    print("Успешно подключено!")
    curr.execute('DELETE FROM keyses WHERE name == ?', (data,))
    conn.commit()