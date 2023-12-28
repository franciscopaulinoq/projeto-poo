from classes.classes import Chave, Discente, Docente, Objeto, Operador, Servidor
from classes.listas import ListaChave, ListaObjeto, ListaOperador, ListaPessoa

import configparser, csv, os

class Leitor:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read("configuracoes.ini")

  def csv_esta_vazio(self, arquivo):
    '''
    Verifica se o csv está vazio, se sim retorna True, se não, retorna False
    '''
    if os.path.exists(arquivo):
      with open(arquivo, "r", newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        if next(leitor_csv) is None:
          return True
        else:
          return False
    else:
      return True

  def ler_csv_chaves(self, pessoas):
    '''
    Abre o arquivo csv.chaves no modo leitura(read) e transforma os valores das linhas
    em um objeto Chave, dando append desse objeto em uma lista, retorna essa lista 
    '''
    chaves = ListaChave()
    if not self.csv_esta_vazio(self.config.get("csv", "csv.chaves")):
      with open(self.config.get("csv", "csv.chaves"), 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv, None)
        for linha in leitor_csv:
          numero, ambiente, pessoa, horario, disponivel = linha
          pessoa = None if pessoa.lower() == "none" else pessoas.filtrar(pessoa)
          horario = None if horario.lower() == "none" else horario
          disponivel = True if disponivel.lower() == "true" else False
          chaves.append(Chave(
            numero=numero, 
            ambiente=ambiente,
            pessoa_que_retirou=pessoa, 
            horario_retirada=horario, 
            disponivel=disponivel
            ))
        return chaves
    else:
      return chaves

  def ler_csv_objetos(self, operadores, pessoas):
    '''
    Abre o arquivo csv.objetos no modo leitura(read) e transforma os valores das linhas
    em um objeto Objeto, dando append desse objeto em uma lista. Retorna essa lista 
    '''
    objetos = ListaObjeto()
    if not self.csv_esta_vazio(self.config.get("csv", "csv.objetos")):
      with open(self.config.get("csv", "csv.objetos"), 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv, None)
        for linha in leitor_csv:
          id, nome, descricao, operador, local_encontro, horario_chegada, pessoa_que_buscou, horario_retirada = linha
          operador = operadores.filtrar(operador)
          if pessoa_que_buscou.lower() == "none":
            objetos.append(Objeto(
                id=id, 
                nome=nome, 
                descricao=descricao, 
                operador=operador, 
                local_encontro=local_encontro, 
                horario_chegada=horario_chegada
                ))
          else:
            pessoa_que_buscou = pessoas.filtrar(pessoa_que_buscou)
            objetos.append(Objeto(
                id=id, 
                nome=nome, 
                descricao=descricao, 
                operador=operador, 
                local_encontro=local_encontro, 
                horario_chegada=horario_chegada,
                pessoa_que_buscou=pessoa_que_buscou,
                horario_retirada=horario_retirada
                ))
        return objetos
    else:
       return objetos

  def ler_csv_operadores(self):
    '''
    Abre o arquivo csv.operadores no modo leitura(read) e transforma os valores das linhas
    em um objeto Operador, dando append desse objeto em uma lista. Retorna essa lista 
    '''
    operadores = ListaOperador()
    if not self.csv_esta_vazio(self.config.get("csv", "csv.operadores")):
      with open(self.config.get("csv", "csv.operadores"), 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv, None)
        for linha in leitor_csv:
          nome, matricula, contato, ocupacao, senha = linha
          operadores.append(Operador(
            nome=nome, 
            matricula=matricula, 
            contato=contato, 
            ocupacao=ocupacao, 
            senha=senha
            ))
        return operadores
    else:
      return operadores

  def ler_csv_pessoas(self):
    '''
    Abre o arquivo csv.operadores no modo leitura(read) e transforma os valores das linhas
    em um objeto Operador, dando append desse objeto em uma lista. Retorna essa lista 
    '''
    pessoas = ListaPessoa()
    if not self.csv_esta_vazio(self.config.get("csv", "csv.pessoas")):
      with open(self.config.get("csv", "csv.pessoas"), 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)
        for linha in leitor_csv:
          nome, matricula, contato, ocupacao = linha
          if ocupacao == "Discente":
            pessoas.append(Discente(
              nome=nome, 
              matricula=matricula, 
              contato=contato
              ))
          if ocupacao == "Docente":
            pessoas.append(Docente(
              nome=nome, 
              matricula=matricula, 
              contato=contato
              ))
          if ocupacao == "Servidor":
            pessoas.append(Servidor(
              nome=nome, 
              matricula=matricula, 
              contato=contato
              ))
        return pessoas
    else:
      return pessoas