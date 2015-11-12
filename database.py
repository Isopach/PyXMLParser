# coding: UTF-8

import sqlite3

def db_add_document(db_path, title, body, category):
    # DBを開く
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # documentsテーブルを開く（なければ作る）
    sql = "CREATE TABLE IF NOT EXISTS documents (" \
        "id INTEGER PRIMARY KEY, " \
        "title TEXT NOT NULL, " \
        "body TEXT NOT NULL, " \
        "category TEXT NOT NULL" \
        ");"
    cur.execute(sql)

    # titleがテーブル内に既に存在するかを調べる
    sql = "SELECT id FROM documents WHERE title = ?;"
    cur.execute(sql, (title,))
    id = cur.fetchone()
    if id != None:
        id = id[0]

    # テーブルに追加/置換する
    sql = "INSERT OR REPLACE INTO documents(id, title, body, category) VALUES(?, ?, ?, ?);"
    cur.execute(sql, (id, title, body, category))

    # DBを保存して閉じる
    con.commit()
    con.close()

#if __name__ == '__main__':
        # db_add_document("test.db", "title2", "body3")
