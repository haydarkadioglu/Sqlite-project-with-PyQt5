import sqlite3


connection = sqlite3.connect('library.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT, yazar TEXT, kitapno İNT)")
connection.commit()

def addbook(nam, writer, no):


    cursor.execute(f"INSERT INTO kitaplar VALUES ('{nam}', '{writer}', {no})")
    connection.commit()

def show():
    cursor.execute("SELECT * FROM kitaplar")
    print(cursor.fetchall())

def deletebook(x):
    cursor.execute(f"DELETE FROM kitaplar WHERE kitapno = {x}")
    connection.commit()


connection.close()
