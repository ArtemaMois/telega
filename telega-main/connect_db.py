import psycopg2


def update_db(search_name, keys_name, keys, keys_state):
    conn = psycopg2.connect(dbname = "keys_bot", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''update keyses set keys_name = %s, keys = %s, keys_state = %s where sername = %s'''
    curr.execute(select_query, (keys_name, keys, keys_state, search_name))
    conn.commit()
    print("Запись успешно обновлена!")

def database(row, name_id, keys_name, keys, keys_state):
    conn = psycopg2.connect(dbname = "keys_bot", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''insert into keyses(id_row, name_id, keys_name, keys, keys_state) VALUES (%s, %s, %s, %s, %s)''', (row, name_id, keys_name, keys, keys_state)
    curr.execute(select_query, (row, name_id, keys_name, keys, keys_state))
    conn.commit()
    print("Новые значения добавлены!")

def new_row(v1,v2,v3,v4,v5):
    conn = psycopg2.connect(dbname = "keys_bot", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''INSERT INTO keyses (name_id, sername, keys_name, keys, keys_state) VALUES (%s,%s,%s,%s,%s);'''
    curr.execute(select_query, (v1,v2,v3,v4,v5))
    conn.commit()
    print("Новые строки добавлены!")

def output(name):
    conn = psycopg2.connect(dbname = "keys_bot", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
    curr = conn.cursor()
    print("Успешно подключено!")
    select_query = '''select * from keyses where sername = %s'''
    curr.execute(select_query, (name,))
    out = curr.fetchall()
    print("вывел результат")
    return out
    