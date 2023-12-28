from classes.classes import Operador
from imprimir.tabelas import Tabelas
from gerenciador.escritor import Escritor
from gerenciador.leitor import Leitor
from imprimir.menu import Menu

import configparser, os

class Main:
  def __init__(self):
    self.operadores = Leitor().ler_csv_operadores()
    self.pessoas = Leitor().ler_csv_pessoas()
    self.chaves = Leitor().ler_csv_chaves(self.pessoas)
    self.objetos = Leitor().ler_csv_objetos(self.operadores, self.pessoas)
    self.ativo = True
    self.autenticado = False
    self.ativo_achados_perdidos = False
    self.ativo_gerenciar_chaves = False
    self.operador_autenticado = None
    self.opcoes_index = {
      "1": self.login, 
      "2": self.cadastrar_operador, 
      "3": self.encerrar
      }
    self.opcoes_operador = {
      "1": self.cadastrar_pessoa,
      "2": self.achados_perdidos,
      "3": self.gerenciar_chaves,
      "4": self.sair,
      "5": self.encerrar
      }
    self.opcoes_achados_perdidos = {
      "1": self.registrar_objeto,
      "2": self.retirar_objeto,
      "3": self.filtrar_objeto,
      "4": self.listar_objetos,
      "5": self.voltar,
      "6": self.encerrar
    }
    self.opcoes_gerenciar_chaves = {
      "1": self.cadastrar_chave,
      "2": self.registrar_saida,
      "3": self.coletar_chave,
      "4": self.filtrar_chave,
      "5": self.listar_chaves,
      "6": self.voltar,
      "7": self.encerrar
    }

  def executar(self):
    '''
    Inicia o programa e pede para o usuário escolher 
    alguma das opções mostradas.
    Verifica se a ação escolhida e válida, se for, executa a ação
    '''
    while self.ativo:
      Menu().menu_index()
      op = input("Informe uma opção: ")
      acao = self.opcoes_index.get(op)
      if acao:
        self.__limpar_terminal()
        acao()
        if self.autenticado:
          self.executar_operador()
      else:
        print("\nOpção inválida.")
        self.__limpar_terminal()

  def executar_operador(self):
    '''
    Inicia a tela do Operador.e pede para o usuário escolher 
    alguma das opções mostradas.
    Verifica se a ação escolhida e válida, se for, executa a ação
    '''
    while self.autenticado:
      Menu().menu_operador()
      op = input("Informe uma opcao: ")
      acao = self.opcoes_operador.get(op)
      if acao:
        self.__limpar_terminal()
        acao()
      else:
        print("\nOpção inválida.")
        self.__limpar_terminal()

  def achados_perdidos(self):
    '''
    Inicia a tela dos Achados e Perdidos e pede para o usuário escolher 
    alguma das opções mostradas.
    Verifica se a ação escolhida e válida, se for, executa a ação
    '''
    self.ativo_achados_perdidos = True
    while self.ativo_achados_perdidos:
      Menu().menu_achados_perdidos()
      op = input("Informe uma opção: ")
      acao = self.opcoes_achados_perdidos.get(op)
      if acao:
        self.__limpar_terminal()
        acao()
      else:
        print("\nOpção inválida.")
        self.__limpar_terminal()

  def gerenciar_chaves(self):
    '''
    Inicia a tela do Gerenciador de Chaves e pede para o usuário escolher 
    alguma das opções mostradas.
    Verifica se a ação escolhida e válida, se for, executa a ação
    '''
    self.ativo_gerenciar_chaves = True
    while self.ativo_gerenciar_chaves:
      Menu().menu_gerenciar_chaves()
      op = input("Informe uma opção: ")
      acao = self.opcoes_gerenciar_chaves.get(op)
      if acao:
        self.__limpar_terminal()
        acao()
      else:
        print("\nOpção inválida.\n")
        self.__limpar_terminal()

  def login(self):
    '''
    Verifica se há algum operador cadastrado, se houver, pede a senha e a matrícula
    verificando se são válidos, se for, o operador é logado no sistema
    '''
    print("          LOGIN         ")
    print("------------------------")
    if not self.operadores:
      print("\nNenhum operador cadastrado no sistema.")
    else:
      matricula = input("Matrícula: ")
      senha = input("Senha: ")
      operador = None
      for operador_v in self.operadores:
        if operador_v.login(matricula=matricula, senha=senha):
          operador = operador_v
      if not operador:
        print("\nMatrícula e/ou senha inválidos.")
      else:
        self.autenticado = True
        self.operador_autenticado = operador
        print("\nOperador autenticado!")
    self.__limpar_terminal()

  def cadastrar_operador(self):
    '''
    Verifica se o operador tem o acesso validado, se tiver, pede
    os dados de um novo operador para ser cadastrado. Apos coletar os dados, verifica-se se
    o operador já existe no sistema
    '''
    if self.__valida_admin():
        continuar = True
        while continuar:
          self.__limpar_terminal()
          print("   CADASTRAR OPERADOR   ")
          print("------------------------")
          nome = (input("Nome: "))
          matricula = (input("Matrícula: "))
          contato = (input("Contato: "))
          ocupacao = (input("Ocupação (discente, docente ou servidor): "))
          senha = (input("Senha: "))
          print("--------------------------")
          if not self.operadores:
            self.operadores.append(Operador(nome, matricula, contato, ocupacao, senha))
            print("Operador adicionado com sucesso!")
          else:
            if [operador for operador in self.operadores if operador.get_matricula() == matricula]:
              print("O operador já está cadastrado.")
            else:
              self.operadores.append(Operador(nome, matricula, contato, ocupacao, senha))
              print("Operador adicionado com sucesso!")
          self.__salvar_dados()
          op = input("Continuar cadastrando? [s/n]: ")
          if op.lower() == "n":
            continuar = False
        self.__limpar_terminal()
    else:
      self.__limpar_terminal()

  def cadastrar_pessoa(self):
    '''
    Pede os dados de uma pessoa a ser cadastrada, verifica se ela existe no sistema,
    caso não exista, o objeto pessoa é cadastrado
    '''
    print("                CADASTRAR PESSOA                ")
    print("------------------------------------------------")
    nome = (input("Nome: "))
    matricula = (input("Matrícula: "))
    contato = (input("Contato: "))
    ocupacao = (input("Ocupação (discente, docente ou servidor): "))
    if self.pessoas.filtrar(matricula):
      print("\nMatrícula já registrada no sistema.")
    else:
      self.operador_autenticado.cadastrar_pessoa(nome, matricula, contato, ocupacao, self.pessoas)
      self.__salvar_dados()
      print("\nPessoa adicionada!")
    self.__limpar_terminal()

  def registrar_objeto(self):
    '''
    Pede os dados de um objeto a ser cadastrada, apos isso, verifica se ele existe no sistema,
    caso não exista, o objeto Objeto é cadastrado
    '''
    print("        REGISTRAR OBJETO        ")
    print("--------------------------------")
    id = input("ID: ")
    nome = input("Nome: ")
    descricao = input("Descriçao: ")
    local_encontro = input("Local de encontro: ")
    if self.objetos.filtrar_por_id(id):
      print("----------------------------------")
      print("ID não disponível para uso.")
    else:
      self.operador_autenticado.registrar_objeto(id, nome, descricao, local_encontro, self.objetos)
      print("----------------------------------")
      print("Objeto registrado!")
      self.__salvar_dados()
    self.__limpar_terminal()

  def retirar_objeto(self):
    '''
    verifica se há objetos cadastrados no sistema, se houverem, recebe a matricula
    de quem veio buscar e o id do objeto, se existir um objeto com
    id igual ao informado, o objeto é retirado da lista de objetos e
    adicionado na lista de retirados
    '''
    print("                  RETIRAR OBJETO                 ")
    print("-------------------------------------------------")
    if not self.objetos:
      print("Nenhum objeto registrado.")
    else:
      pessoa_que_buscou = None
      while True:
        matricula = input("Matrícula da pessoa que veio buscar: ")
        pessoa_que_buscou = self.pessoas.filtrar(matricula)
        if not pessoa_que_buscou:
          print("Pessoa não registrada.")
          op = input("Informar a matricula novamente? [s/n] ")
          if op.lower() == "n":
            self.__limpar_terminal()
            return
        else:
          break
      id_objeto = input("ID do objeto: ")
      objeto_retirado = self.objetos.filtrar_por_id(id_objeto)
      if not objeto_retirado:
        print("Objeto não encontrado.")
      else:
        self.operador_autenticado.retirar_objeto(objeto_retirado, pessoa_que_buscou)
        print("Objeto retirado!")
        self.__salvar_dados()
    self.__limpar_terminal()

  def filtrar_objeto(self):
    '''
    Pede Nome, Descrição, ID ou Local de Encontro do objeto e com a informação
    obtida mostra a lista de objetos com a informação correspondente
    '''
    print("                         BUSCAR OBJETO                        ")
    print("--------------------------------------------------------------")
    campo = input("Nome, Descrição, ID ou Local de Encontro do objeto: ")
    resultado = self.objetos.filtrar(campo)
    if not resultado:
      print("\nNenhuma correspondência de objetos.")
    else:
      for objeto in resultado:
        print(Tabelas().criarDataframeObjeto(resultado))
      print("")
    self.__limpar_terminal()

  def listar_objetos(self):
    '''
    Verifica se há algum objeto na lsita, se houver, exibe todos os objetos
    '''
    print("                       LISTA DE OBJETOS                       ")
    print("--------------------------------------------------------------")
    if not self.objetos:
      print("\nNenhum objeto registrado.")
    else:
      print(Tabelas().criarDataframeObjeto(self.objetos))
      print("")
    self.__limpar_terminal()

  def cadastrar_chave(self):
    '''
    Pede o número e o ambiente de uma chave, apos isso, verifica se ela já está
    no sistema, se não estiver, ela é cadastrada
    '''
    print("   CADASTRAR CHAVE   ")
    print("---------------------")
    numero = input("Número: ")
    ambiente = input("Ambiente (ex: Sala): ")
    if self.chaves.filtrar(numero):
      print("\nA chave já registrada no sistema.")
    else:
      self.operador_autenticado.cadastrar_chave(numero, ambiente, self.chaves)
      print("\nChave cadastrada!")
    self.__salvar_dados()
    self.__limpar_terminal()

  def registrar_saida(self):
    '''
    Verifica se há alguma chave registrada, se houver, pede a matrícula
    de quem veio buscar, se essa pessoa estiver cadastrada, pede o
    número da chave, se a chave existir no sistema ela registrar a saida
    '''
    print("                 REGISTRAR SAÍDA                 ")
    print("-------------------------------------------------")
    if not self.chaves:
      print("Nenhuma chave registrada.")
    else:
      pessoa_que_retirou = None
      while True:
        matricula = input("Matrícula da pessoa que veio buscar: ")
        pessoa_que_retirou = self.pessoas.filtrar(matricula)
        if not pessoa_que_retirou:
          print("Pessoa não registrada.")
          op = input("Informar a matricula novamente? [s/n] ")
          if op.lower() == "n":
            self.__limpar_terminal()
            return
        else:
          break
      numero = input("Número da chave: ")
      chave = self.chaves.filtrar(numero)
      if not chave:
        print("Chave não encontrada.")
      else:
        self.operador_autenticado.registrar_saida_chave(chave, pessoa_que_retirou)
        print("Operação realizada!")
        self.__salvar_dados()
    self.__limpar_terminal()

  def coletar_chave(self):
    '''
    Informa-se o numero da chave, se ela existir, ela é coletada
    '''
    print("   REGISTRAR COLETA   ")
    print("----------------------")
    numero = input("Número da chave: ")
    chave = self.chaves.filtrar(numero)
    if not chave:
      print("\nA chave não existe.")
    else:
      self.operador_autenticado.coletar_chave(chave)
      print("\nOperação realizada!")
      self.__salvar_dados()
    self.__limpar_terminal()

  def listar_chaves(self):
    '''
    Verifica se há chaves, se houver, todas serão exibidas
    '''
    print("          LISTA DE CHAVES         ")
    print("----------------------------------")
    if not self.chaves:
      print("Nenhuma chave registrada no sistema.")
      print("------------------------------------")
    else:
      print(Tabelas().criarDataframeChave(self.chaves))
      print("")
    self.__limpar_terminal()

  def filtrar_chave(self):
    '''
    Informa-se o numero da chave e verifica se ela existe no sistema, se existir
    somente ela é exibida
    '''
    print("   BUSCAR CHAVE   ")
    print("-------------------")
    numero = input("Número da chave: ")
    chave = self.chaves.filtrar(numero)
    if chave:
      print(Tabelas().criarDataframeChaveFiltrada(chave))
    else:
      print("\nChave não encontrada no sistema.")
    self.__limpar_terminal()

  def voltar(self):
    '''
    Encerra a execução atual
    '''
    self.ativo_achados_perdidos = False
    self.ativo_gerenciar_chaves = False

  def sair(self):
    '''
    Deslogar o operador atual
    '''
    self.operador_autenticado = None
    self.autenticado = False

  def encerrar(self):
    '''
    Encerra a aplicação
    '''
    self.ativo = False
    self.autenticado = False
    self.ativo_achados_perdidos = False
    self.ativo_gerenciar_chaves = False
    self.operador_autenticado = None

  def __salvar_dados(self):
    '''
    Salva as listas nos seus respectivos arquivos CSV 
    '''
    Escritor().escrever_dados_csv(self.chaves, self.objetos, self.operadores, self.pessoas)

  def __valida_admin(self):
    '''
    Valida o acesso ao admin
    '''
    config = configparser.ConfigParser()
    config.read("configuracoes.ini")
    print("   VALIDAR ACESSO   ")
    print("---------------------")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == config.get("admin", "usuario") and senha == config.get("admin", "senha"):
      print("\nAcesso permitido!")
      return True
    else:
      print("\nUsuário e/ou senha inválidos.")
      return False

  def __limpar_terminal(self):
    '''
    Limpa o terminal
    '''
    os.system("pause")
    os.system("cls")

if __name__ == "__main__":
  Main().executar()