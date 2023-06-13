def create_user(conexao, user, passowrd):
  cursor = conexao.cursor()
  
  sql = f'INSERT INTO usuario(user, password) VALUES (?, ?)'
  cursor.execute(sql, [user, passowrd])
  conexao.commit()
  
  return True

def list_user (conexao):
  cursor = conexao.cursor()
  sql = 'select * from usuario'
  cursor.execute(sql)
  return cursor.fetchall()


def login_user(conexao, user, password):
  cursor = conexao.cursor()
  sql = 'SELECT * FROM usuario WHERE user = ? and password = ?'
  cursor.execute(sql, [user, password])
  return cursor.fetchall()