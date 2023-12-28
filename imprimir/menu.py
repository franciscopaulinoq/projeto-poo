class Menu:
  def menu_index(self):
    '''
    Exibe as opções do menu index, a primeira seção que aparece para o usuário
    '''
    print("GERENCIADOR COADES")
    print("1. Login")
    print("2. Cadastrar Operador")
    print("3. Encerrar")
  
  def menu_operador(self):
    '''
    Exibe as opções do menu operador, seção que aparece após o operador efetuar login
    '''
    print("MENU OPERADOR")
    print("1. Cadastrar Pessoa")
    print("2. Achados e Perdidos")
    print("3. Gerenciar Chaves")
    print("4. Sair")
    print("5. Encerrar")
  
  def menu_achados_perdidos(self):
    '''
    Exibe as opções do menu achados e perdidos, seção que aparece após o operador selecionar
    a opção "Achados e Perdidos" no menu operador
    '''
    print("MENU ACHADOS E PERDIDOS")
    print("1. Registrar Objeto")
    print("2. Retirar Objeto")
    print("3. Filtrar Objeto")
    print("4. Listar Objetos")
    print("5. Voltar")
    print("6. Encerrar")
  
  def menu_gerenciar_chaves(self):
    '''
    Exibe as opções do menu gerenciar chaves, seção que aparece após o operador selecionar
    a opção "Gerenciar Chaves" no menu operador
    '''
    print("MENU GERENCIAR CHAVES")
    print("1. Cadastrar Chave")
    print("2. Registrar Saída")
    print("3. Coletar Chave")
    print("4. Filtrar Chave")
    print("5. Listar Chaves")
    print("6. Voltar")
    print("7. Encerrar")