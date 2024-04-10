#  Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автоматизированного контроля затрат на производство продукции
#  БД должна содержать таблица Расходы со следующей структурой записи:
#  Дата, Код продукта, Наименование продукта, Расходы, Сумма.
# -*- coding: utf-8 -*-

import sqlite3 as sq
from data_raskhody import info_raskhody

with sq.connect('raskhody.db') as con:
    con.execute("""CREATE TABLE IF NOT EXISTS raskhody(
            data_r DATE,    
            prod_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            imya_prod VARCHAR NOT NULL,
            raskh_res INTEGER NOT NULL,
            summa INTEGER NOT NULL)""")

with sq.connect('raskhody.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO raskhody VALUES (?, ?, ?, ?, ?)", info_raskhody)

# select

# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT imya_prod, summa FROM raskhody")
#     result = cur.fetchall()
#     print(result)
#
# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT data_r, imya_prod FROM raskhody")
#     result = cur.fetchall()
#     print(result)
#
# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT prod_id, raskh_res FROM raskhody")
#     result = cur.fetchall()
#     print(result)

# update
#
# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE raskhody SET raskh_res = 600 WHERE prod_id = 3")
#     cur.execute("SELECT * FROM raskhody")
#     result = cur.fetchall()
#     print(result)
#
# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE raskhody SET raskh_res = raskh_res+400  WHERE summa < 2000")
#     cur.execute("SELECT * FROM raskhody")
#     result = cur.fetchall()
# print(result)
#
# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE raskhody SET summa = summa-50 WHERE raskh_res > 200")
#     cur.execute("SELECT * FROM raskhody")
#     result = cur.fetchall()
#     print(result)

# delete

# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM raskhody WHERE prod_id = 7")
#     cur.execute("SELECT * FROM raskhody")
#     result = cur.fetchall()
#     print(result)
#
# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM raskhody WHERE summa > 5000")
#     cur.execute("SELECT * FROM raskhody")
#     result = cur.fetchall()
#     print(result)
#
#
# with sq.connect('raskhody.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM raskhody WHERE data_r < '2024-04-12'")
#     cur.execute("SELECT * FROM raskhody")
#     result = cur.fetchall()
#     print(result)
