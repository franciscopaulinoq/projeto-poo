import configparser, csv, os

class Escritor:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read("configuracoes.ini")

  def escrever_dados_csv(self, chaves, objetos, operadores, pessoas):
    '''
    Verifica se o diretorio existe, se nao existir, um diretorio é criado, após isso
    é verificado se existem chaves, objetos, operadores e pessoas, se sim
    o método escrever_*_csv de cada uma é executado 
    '''
    if not os.path.isdir("./dados"): # vemos de este diretorio ja existe
      os.mkdir("./dados") # aqui criamos a pasta caso nao exista
    if chaves:
      self.escrever_chaves_csv(chaves)
    if objetos:
      self.escrever_objetos_csv(objetos)
    if operadores:
      self.escrever_operadores_csv(operadores)
    if pessoas:
      self.escrever_pessoa_csv(pessoas)
    
  def escrever_chaves_csv(self, chaves):
    '''
    Abre um arquivo csv no modo escrita(write) para salvar os valores das chaves,
    em seguida, verifica-se se existe um valor para chave.get_pessoa_que_retirou
    se existir, a chave é salva com a matricula dessa pessoa, se não, a chave é salva com
    o próprio valor do objeto pessoa (None)
    '''
    with open(self.config.get("csv", "csv.chaves"), 'w', newline='') as arquivo_csv:
      escritor_csv = csv.writer(arquivo_csv)
      escritor_csv.writerow([
        'numero', 
        'ambiente', 
        'pessoa_que_retirou', 
        'horario_de_retirada', 
        'disponivel'
        ])
      for chave in chaves:
        if not chave.get_pessoa_que_retirou():
          escritor_csv.writerow([
            chave.get_numero(),
            chave.get_ambiente(),
            chave.get_pessoa_que_retirou(),
            chave.get_horario_retirada(),
            chave.get_disponivel()
            ])
        else:
          escritor_csv.writerow([
            chave.get_numero(),
            chave.get_ambiente(),
            chave.get_pessoa_que_retirou().get_matricula(),
            chave.get_horario_retirada(),
            chave.get_disponivel()
            ])
    
  def escrever_objetos_csv(self, objetos):
    '''
    Abre um arquivo csv no modo escrita(write) para salvar os valores dos objetos,
    em seguida, verifica-se se existe um valor para objeto.get_pessoa_que_buscou
    se existir, o objeto é salvo com a matricula dessa pessoa, se não, o objeto é salvo com
    o próprio valor do objeto pessoa (None)
    '''
    with open(self.config.get("csv", "csv.objetos"), 'w', newline='') as arquivo_csv:
      escritor_csv = csv.writer(arquivo_csv)
      escritor_csv.writerow([
        'id', 
        'nome', 
        'descricao', 
        'operador', 
        'local_encontro', 
        'horario_de_chegada', 
        'pessoa_que_buscou', 
        'horario_retirada'
        ])
      for objeto in objetos:
        if objeto.get_pessoa_que_buscou():
          escritor_csv.writerow([
            objeto.get_id(),
            objeto.get_nome(),
            objeto.get_descricao(),
            objeto.get_operador().get_matricula(),
            objeto.get_local_encontro(),
            objeto.get_horario_chegada(),
            objeto.get_pessoa_que_buscou().get_matricula(),
            objeto.get_horario_retirada()
            ])
        else:
          escritor_csv.writerow([
            objeto.get_id(),
            objeto.get_nome(),
            objeto.get_descricao(),
            objeto.get_operador().get_matricula(),
            objeto.get_local_encontro(),
            objeto.get_horario_chegada(),
            objeto.get_pessoa_que_buscou(),
            objeto.get_horario_retirada()
            ])
  
  def escrever_operadores_csv(self, operadores):
    '''
    Abre um arquivo csv no modo escrita(write) para salvar os valores dos operadores
    '''
    with open(self.config.get("csv", "csv.operadores"), 'w', newline='') as arquivo_csv:
      escritor_csv = csv.writer(arquivo_csv)
      escritor_csv.writerow(['nome', 'matricula', 'contato', 'ocupacao', 'senha'])
      for operador in operadores:
        escritor_csv.writerow([
          operador.get_nome(), 
          operador.get_matricula(), 
          operador.get_contato(), 
          operador.get_ocupacao(), 
          operador.get_senha()
          ])

  def escrever_pessoa_csv(self, pessoas):
    '''
    Abre um arquivo csv no modo escrita(write) para salvar os valores dos operadores
    '''
    with open(self.config.get("csv", "csv.pessoas"), 'w', newline='') as arquivo_csv:
      escritor_csv = csv.writer(arquivo_csv)
      escritor_csv.writerow(['nome', 'matricula', 'contato', 'ocupacao'])
      for pessoa in pessoas:
        escritor_csv.writerow([
          pessoa.get_nome(), 
          pessoa.get_matricula(), 
          pessoa.get_contato(), 
          pessoa.get_ocupacao()
          ])