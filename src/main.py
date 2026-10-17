import sqlite3

conn = sqlite3.connect("data/items.db")

print("データベース接続成功！")

conn.close()