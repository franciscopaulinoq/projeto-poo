from datetime import datetime, timedelta, timezone

import abc

class Pessoa(abc.ABC):
  def __init__(self, nome, matricula, contato, ocupacao):
    self.__nome = nome
    self.__matricula = matricula
    self.__contato = contato
    self.__ocupacao = ocupacao

  def get_nome(self):
    return self.__nome

  def get_matricula(self):
    return self.__matricula
  
  def get_contato(self):
    return self.__contato
  
  def get_ocupacao(self):
    return self.__ocupacao

  def __str__(self):
    return self.get_matricula()

class Discente(Pessoa):
  def __init__(self, nome, matricula, contato):
    super().__init__(nome, matricula, contato, "Discente")

class Docente(Pessoa):
  def __init__(self, nome, matricula, contato):
    super().__init__(nome, matricula, contato, "Docente")

class Servidor(Pessoa):
  def __init__(self, nome, matricula, contato):
    super().__init__(nome, matricula, contato, "Servidor")

class LoginMixIn:
  def login(operador, matricula, senha):
    if operador.get_matricula() == matricula and operador.get_senha() == senha:
      return True
    else:
      return False

class Operador(Pessoa, LoginMixIn):
  def __init__(self, nome, matricula, contato, ocupacao, senha):
    super().__init__(nome, matricula, contato, ocupacao)
    self.__senha = senha

  def get_senha(self):
    return self.__senha

  def cadastrar_chave(self, numero, ambiente, lista_chaves):
    lista_chaves.append(Chave(numero, ambiente))

  def registrar_saida_chave(self, chave, pessoa):
    chave.set_pessoa_que_retirou(pessoa)
    chave.set_disponivel(False)
    chave.set_horario_retirada(datetime.today().astimezone(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y %H:%M'))
    return True
  
  def coletar_chave(self, chave):
    chave.set_pessoa_que_retirou(None)
    chave.set_disponivel(True)
    chave.set_horario_retirada(None)
    return True
  
  def registrar_objeto(self, id, nome, descricao, local_encontro, lista_objetos):
    lista_objetos.append(Objeto(id, nome, descricao, self, local_encontro))
    return True
  
  def retirar_objeto(self, objeto, pessoa):
    objeto.set_pessoa_que_buscou(pessoa)
    objeto.set_horario_retirada(datetime.today().astimezone(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y %H:%M'))
    return True
  
  def cadastrar_pessoa(self, nome, matricula, contato, ocupacao, lista_pessoas):
    if ocupacao.lower() == "discente":
      lista_pessoas.append(Discente(nome, matricula, contato))
    if ocupacao.lower() == "docente":
      lista_pessoas.append(Docente(nome, matricula, contato))
    if ocupacao.lower() == "servidor":
      lista_pessoas.append(Servidor(nome, matricula, contato))
    return True

class Objeto:
  def __init__(
      self, 
      id, 
      nome, 
      descricao, 
      operador,
      local_encontro, 
      horario_chegada = datetime.today().astimezone(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y %H:%M'),  
      pessoa_que_buscou = None, 
      horario_retirada = None
      ):
    self.__id = id
    self.__nome = nome
    self.__descricao = descricao
    self.__operador = operador
    self.__local_encontro = local_encontro
    self.__horario_chegada = horario_chegada
    self.__pessoa_que_buscou = pessoa_que_buscou
    self.__horario_retirada = horario_retirada

  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome

  def get_descricao(self):
    return self.__descricao

  def get_operador(self):
    return self.__operador

  def get_horario_chegada(self):
    return self.__horario_chegada

  def get_local_encontro(self):
    return self.__local_encontro

  def get_pessoa_que_buscou(self):
    return self.__pessoa_que_buscou

  def set_pessoa_que_buscou(self, pessoa_que_buscou):
    self.__pessoa_que_buscou = pessoa_que_buscou

  def get_horario_retirada(self):
    return self.__horario_retirada

  def set_horario_retirada(self, horario_retirada):
    self.__horario_retirada = horario_retirada

class Chave:
  def __init__(
      self, 
      numero,
      ambiente, 
      pessoa_que_retirou = None, 
      horario_retirada = None, 
      disponivel = True
      ):
    self.__numero = numero
    self.__ambiente = ambiente
    self.__pessoa_que_retirou = pessoa_que_retirou
    self.__horario_retirada = horario_retirada
    self.__disponivel = disponivel

  def get_numero(self):
    return self.__numero
  
  def get_ambiente(self):
    return self.__ambiente
  
  def get_horario_retirada(self):
    return self.__horario_retirada
  
  def set_horario_retirada(self, horario_retirada):
    self.__horario_retirada = horario_retirada

  def get_pessoa_que_retirou(self):
    return self.__pessoa_que_retirou

  def set_pessoa_que_retirou(self, pessoa_que_retirou):
    self.__pessoa_que_retirou = pessoa_que_retirou

  def get_disponivel(self):
    return self.__disponivel

  def set_disponivel(self, disponivel):
    self.__disponivel = disponivel