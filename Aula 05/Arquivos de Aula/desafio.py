class Produto:  
    def __init__(self,nome_prod, preco_prod, categ_prod):
        self.nome = nome_prod
        self.preco = preco_prod
        self.categoria = categ_prod
    
    def desc_prod(self):
        print(f'O produto {self.nome}, custa R${self.preco},da categoria: {self.categoria}')

class Livro:
    def __init__(self,nome_livro, preco_livro, categ_livro):
        self.nomelv = nome_livro
        self.precolv = preco_livro
        self.categorialv = categ_livro

    def desc_livro(self):
        print(f'O livro {self.nomelv}, custa R${self.precolv},da categoria: {self.categorialv}')

class Filme:
    def __init__(self,nome_filme, preco_filme, categ_filme):
        self.nomefilm = nome_filme
        self.precofilm = preco_filme
        self.categoriafilm = categ_filme

    def desc_film(self):
        print(f'O filme {self.nomefilm}, custa R${self.precofilm},da categoria: {self.categoriafilm}')


product = Produto('Iphone','5000','celular')
product.desc_prod()

book = Livro('Pequeno Principe','50','Infantil')
book.desc_livro()

film = Filme('Goonies','25','Aventura')
film.desc_film()