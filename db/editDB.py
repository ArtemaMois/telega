import sqlite3

def setData(user, case):
    try:
        connection = sqlite3.connect('db/db.db')
        cursor = connection.cursor()
        query = f"""INSERT INTO cases (user, case_content) VALUES ("{user}", "{case}");"""
        cursor.execute(query)
        connection.commit()
        cursor.close()   
        return "Кейс добавлен"     
    except sqlite3.Error as error:
        return error
    finally:
        if connection:
            connection.close()

def getData(user = False):
    connection = sqlite3.connect('db/db.db')
    cursor = connection.cursor()
    try:
        if (user == False):
            query = """SELECT * FROM cases;"""
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        query = f"""SELECT * FROM cases WHERE user = "{user}"; """      
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except sqlite3.Error as error:
        return error
    finally:
        if connection:
            connection.close()

def removeData(id = False):
    connection = sqlite3.connect('db/db.db')
    cursor = connection.cursor()
    try:
        if (id == False):
            query = """DELETE FROM cases;"""
            cursor.execute(query)
            connection.commit()
            cursor.close()
            return "Таблица очищена"
        query = f"""DELETE FROM cases WHERE case_id = {id}"""
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return f"Кейс с id = {id} удален"
    except sqlite3.Error as error:
        return error
    finally:
        if connection:
            connection.close()