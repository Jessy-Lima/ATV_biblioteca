class Itembiblioteca:
    def __init__(self, codigo: int, titulo: str, ano: int, disponivel: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    
    def get_ano(self):
        return self.__ano
    
    def get_disponivel(self):
        return self.__disponivel