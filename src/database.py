# SQLiteを扱うためのライブラリ
import sqlite3


def create_database():
    """
    InventoryManagerで使用する
    SQLiteデータベースを作成する。
    """

    # dataフォルダ内にDBファイルを作成
    # 存在する場合は接続のみ行う
    conn = sqlite3.connect("data/items.db")

    # SQLを実行するためのカーソル作成
    cursor = conn.cursor()

    # =========================
    # users テーブル作成
    # =========================
    # システム利用者(リスナー)を管理
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        image_path TEXT
    )
    """)

    # =========================
    # items テーブル作成
    # =========================
    # アイテムマスタ
    # システムで扱うアイテム一覧
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        effect TEXT,
        default_duration INTEGER NOT NULL
    )
    """)

    # =========================
    # user_items テーブル作成
    # =========================
    # リスナーが実際に所持しているアイテム
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        -- 所有者
        user_id INTEGER NOT NULL,

        -- 所持アイテム
        item_id INTEGER NOT NULL,

        -- 取得日時
        created_at DATETIME NOT NULL,

        -- 消滅日時
        expires_at DATETIME NOT NULL,

        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
    )
    """)

    # DBへ保存
    conn.commit()

    # 接続終了
    conn.close()

    print("データベース作成完了")


if __name__ == "__main__":
    create_database()