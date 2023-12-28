import abc

class Filtravel(abc.ABC):
  @abc.abstractmethod
  def filtrar():
    pass

class ListaChave(list, Filtravel):
  def filtrar(self, numero):
    for chave in self:
      if chave.get_numero() == numero:
        return chave

class ListaObjeto(list, Filtravel):
  def filtrar(self, campo):
    return [
      objeto for objeto in self 
      if campo.lower() in objeto.get_nome().lower() or 
      campo.lower() in objeto.get_descricao().lower() or 
      campo.lower() in objeto.get_id().lower() or campo.lower() in 
      objeto.get_local_encontro().lower()
      ]
  
  def filtrar_por_id(self, id):
    for objeto in self:
      if objeto.get_id() == id:
        return objeto

  def filtar_retirados(self):
    return [objeto for objeto in self if objeto.get_pessoa_que_buscou()]

class ListaOperador(list, Filtravel):
  def filtrar(self, matricula):
    for operador in self:
      if operador.get_matricula() == matricula:
        return operador

class ListaPessoa(list, Filtravel):
  def filtrar(self, matricula):
    for pessoa in self:
      if pessoa.get_matricula() == matricula:
        return pessoa