import pandas

class Tabelas:  
  def criarDataframeChave(self, chaves):
    '''
    Cria uma tabela com os dados de todas as chaves
    '''
    tabela_chaves = {
      'Número': [chave.get_numero() for chave in chaves],
      'Ambiente': [chave.get_ambiente() for chave in chaves],
      'Pessoa que Retirou': [chave.get_pessoa_que_retirou() for chave in chaves],
      'Horário de Retirada': [chave.get_horario_retirada() for chave in chaves],
      'Disponível': [chave.get_disponivel() for chave in chaves],
      }
    return pandas.DataFrame(tabela_chaves)
  
  def criarDataframeChaveFiltrada(self, chave):
    '''
    Cria uma tabela com os dados de uma chave específica que foi filtrada
    '''
    tabela_chave = {
      'Número': [chave.get_numero()],
      'Ambiente': [chave.get_ambiente()],
      'Pessoa que Retirou': [chave.get_pessoa_que_retirou()],
      'Horário de Retirada': [chave.get_horario_retirada()],
      'Disponível': [chave.get_disponivel()],
      }
    return pandas.DataFrame(tabela_chave)

  def criarDataframeObjeto(self, objetos):
    '''
    Cria uma tabela com os dados de todas as chaves
    '''
    tabela_objetos = {
       'ID': [objeto.get_id() for objeto in objetos],
       'Nome': [objeto.get_nome() for objeto in objetos],
       'Descrição': [objeto.get_descricao() for objeto in objetos],
       'Operador': [objeto.get_operador() for objeto in objetos],
       'Local de Encontro': [objeto.get_local_encontro() for objeto in objetos],
       'Pessoa que Buscou': [objeto.get_pessoa_que_buscou() for objeto in objetos],
       'Horário de Retirada': [objeto.get_horario_retirada() for objeto in objetos],
       }
    return pandas.DataFrame(tabela_objetos)