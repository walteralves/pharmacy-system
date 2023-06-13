def register_medicine(conexao, nome, quantidade, preco):
  cursor = conexao.cursor()
  
  sql = 'INSERT INTO produto(nome, quantidade, preco) VALUES (?, ?, false)'
  cursor.execute(sql, [nome, quantidade, preco])
  conexao.commit()
  
  return True

def list_medicine(conexao):
  cursor = conexao.cursor()
  sql = 'SELEC * FROM produto'
  cursor.execute(sql)
  return cursor.fetchall()

def update_medicine(conexao, quantidade, preco):
  cursor = conexao.cursor()
  sql = 'SELECT * FROM produto WHERE id = ?'
  cursor.execute(sql, [id])
  
  if cursor.fetchall() == []:
    return print('\nEste produto não está cadastrado no sistema!')
  
  sql = "UPDATE produto WHERE quantidade = ? and preco = ?"
  cursor.execute(sql, [quantidade, preco])
  print('\nProduto atualizado com sucesso!')
  
def delete_medicine(conexao, id):
  cursor = conexao.cursor()
  sql = 'SELECT * FROM produto WHERE id = ?'
  cursor.execute(sql, [id])
  
  if cursor.fetchall() == []:
    return print('\nEste produto não está cadastrado no sistema!')
  
  sql = 'DELETE FROM produto WHERE id = ?'
  cursor.execute(sql, [id])
  conexao.commit
  print('\nProduto detelato!')
