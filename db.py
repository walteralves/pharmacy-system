import sqlite3

conn = sqlite3.connect('farmacia.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
      user_id INTEGER PRIMARY KEY AUTOINCREMENT,
      user VARCHAR(25),
      password INTEGER
    )
''')

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS produto (
      produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome VARCHAR(25),
      quantidade INTEGER,
      preco REAL
    )
''')

conn.commit()