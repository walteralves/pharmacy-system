def register_medicine(conexao, nome, quantidade, preco):
  cursor = conexao.cursor()
  
  sql = f'INSERT INTO produto(nome, quantidade, preco) VALUES (?, ?, ?)'
  cursor.execute(sql, [nome, quantidade, preco])
  conexao.commit()
  
  return True

def list_medicine(conexao):
  cursor = conexao.cursor()
  sql = 'SELECT * FROM produto'
  cursor.execute(sql)
  return cursor.fetchall()

def validate(conexao, produto_id):
  cursor = conexao.cursor()
  sql = 'SELECT * FROM produto WHERE produto_id = ?'
  cursor.execute(sql, [produto_id])
  
  return cursor.fetchall() == []

def update_medicine(conexao, produto_id, quantidade, preco):
  cursor = conexao.cursor()
  sql = 'UPDATE produto SET quantidade=? AND preco=? WHERE produto_id=?'
  cursor = conexao.cursor()
  cursor.execute(sql, [quantidade, preco, produto_id])
  conexao.commit()
  print('\nProduto atualizado com sucesso!')
  
def delete_medicine(conexao, produto_id):
  cursor = conexao.cursor()
  sql = 'SELECT * FROM produto WHERE produto_id = ?'
  cursor.execute(sql, [produto_id])
  
  if cursor.fetchall() == []:
    return print('\nEste produto não está cadastrado no sistema!')
  
  sql = 'DELETE FROM produto WHERE produto_id = ?'
  cursor.execute(sql, [produto_id])
  conexao.commit()
  print('\nProduto excluído!')
