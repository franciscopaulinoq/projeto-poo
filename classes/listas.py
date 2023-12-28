import abc

class Filtravel(abc.ABC):
  @abc.abstractmethod
  def filtrar():
    pass

class ListaChave(list, Filtravel):
  def filtrar(self, numero):
    '''
    Recebe um valor para numero e verifica se há alguma chave registrada
    com esse numero e a retorna
    '''
    for chave in self:
      if chave.get_numero() == numero:
        return chave

class ListaObjeto(list, Filtravel):
  def filtrar(self, campo):
    '''
    Recebe um valor para campo e verifica se há algum objeto registrado
    com algum valor igual ao campo informado, retorna o objeto encontrado
    '''
    return [
      objeto for objeto in self 
      if campo.lower() in objeto.get_nome().lower() or 
      campo.lower() in objeto.get_descricao().lower() or 
      campo.lower() in objeto.get_id().lower() or campo.lower() in 
      objeto.get_local_encontro().lower()
      ]
  
  def filtrar_por_id(self, id):
    '''
    Verifica se o valor do ID inofrmado é igual ao ID de algum
    objeto cadastrado na lista, retorna o objeto encontrado
    '''
    for objeto in self:
      if objeto.get_id() == id:
        return objeto

  def filtar_retirados(self):
    '''
    Retorna todos os objetos que foram retirados
    '''
    return [objeto for objeto in self if objeto.get_pessoa_que_buscou()]

class ListaOperador(list, Filtravel):
  def filtrar(self, matricula):
    '''
    Verifica se o valor da matricula inofrmada é igual a matricula de algum
    operador cadastrado na lista, retorna o operador encontrado
    '''
    for operador in self:
      if operador.get_matricula() == matricula:
        return operador

class ListaPessoa(list, Filtravel):
  def filtrar(self, matricula):
    '''
    Verifica se o valor da matricula inofrmada é igual a matricula de alguma
    pessoa cadastrado na lista, retorna a pessoa encontrada
    '''
    for pessoa in self:
      if pessoa.get_matricula() == matricula:
        return pessoa