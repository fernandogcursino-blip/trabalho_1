class TipoAtendimento:
    def __init__(self, codigo: int, nome: str, descricao: str):
        self._codigo = codigo
        self._nome = nome
        self._descricao = descricao

    @property
    def codigo(self): return self._codigo
    
    @property
    def nome(self): return self._nome
    
    @property
    def descricao(self): return self._descricao