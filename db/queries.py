# Существующие таблицы
CREATE_TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    email TEXT,
    city TEXT,
    photo TEXT
    )
"""

INSERT_registered_query = """
    INSERT INTO registered (fullname, age, email, city, photo)
    VALUES (?, ?, ?, ?, ?)
"""

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    photo TEXT,
    product_id TEXT,
    collection_id INTEGER,
    FOREIGN KEY (collection_id) REFERENCES collection(id)
    )
"""

INSERT_store_query = """
    INSERT INTO store (name_product, size, price, photo, product_id, collection_id)
    VALUES (?, ?, ?, ?, ?, ?)
"""

CREATE_TABLE_store_detail = """
    CREATE TABLE IF NOT EXISTS store_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    category TEXT,
    info_product TEXT
    )
"""

INSERT_store_detail_query = """
    INSERT INTO store_detail (product_id, category, info_product)
    VALUES (?, ?, ?)
"""

# Обновленная таблица collection
CREATE_TABLE_collection = """
    CREATE TABLE IF NOT EXISTS collection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_name TEXT NOT NULL,
    collection_description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""

INSERT_collection_query = """
    INSERT INTO collection (collection_name, collection_description)
    VALUES (?, ?)
"""

# Дополнительные запросы для работы с collection
GET_ALL_COLLECTIONS = """
    SELECT * FROM collection
"""

GET_COLLECTION_BY_ID = """
    SELECT * FROM collection WHERE id = ?
"""

UPDATE_COLLECTION = """
    UPDATE collection 
    SET collection_name = ?, collection_description = ?
    WHERE id = ?
"""

DELETE_COLLECTION = """
    DELETE FROM collection WHERE id = ?
"""