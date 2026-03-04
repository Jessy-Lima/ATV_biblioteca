from itembiblioteca import Itembiblioteca

class Revista(Itembiblioteca):
    def __init__(self, codigo, titulo, ano,):
        super().__init__(codigo, titulo, ano)