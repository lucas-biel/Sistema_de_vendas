class Produto:  # O produto tem título, valor e desconto.
    def __init__(self):
        self.titulo = None
        self.valor = 0
        self.desconto = 0
    
    # Métodos para inserir ou visualizar os dados de um produto
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def get_valor(self):
        return self.valor

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, novo_desconto):
        self.desconto = novo_desconto

    def descreve_produto(self):  # Onde são mostradas todas as informações do produto.
        print(f'Título: {self.get_titulo()}')
        print(f'Valor: R${self.get_valor():.2f}')
        print(f'Desconto: {self.get_desconto()}%')
        print(f'Valor final: R${self.get_valor():.2f}')


class Livro(Produto):  # Herda os atributos da classe Produto
    def __init__(self):
        self.autor = None  # atributo especial desta classe
        super().__init__()  # recebendo os atributos da classe pai

    def get_autor(self):
        return self.autor

    def set_autor(self, novo_autor):
        self.autor = novo_autor

    def get_valor(self):
        preco = super().get_valor()
        preco -= super().get_valor() * super().get_desconto() / 100
        return preco

    def descreve_produto(self):
        print(f'Livro: {super().get_titulo()}')  # uso de um método herdado da classe pai
        print(f'Autor(a): {self.get_autor()}')
        print(f'Valor: R${super().get_valor():.2f}')
        print(f'Desconto: {super().get_desconto()}%')
        print(f'Valor final: R${self.get_valor():.2f}')


class CD(Produto):
    def __init__(self):
        self.artista = None  # atributo especial desta classe
        super().__init__()

    def get_artista(self):
        return self.artista

    def set_artista(self, novo_artista):
        self.artista = novo_artista

    def get_valor(self):
        preco = super().get_valor()
        preco -= super().get_valor() * super().get_desconto() / 100
        return preco

    def descreve_produto(self):
        print(f'CD: {super().get_titulo()}')
        print(f'Artista: {self.get_artista()}')
        print(f'Valor: R${super().get_valor():.2f}')
        print(f'Desconto: {super().get_desconto()}%')
        print(f'Valor final: R${self.get_valor():.2f}')


class DVD(Produto):
    def __init__(self):
        self.duracao = None  # atributo especial desta classe
        super().__init__()

    def get_duracao(self):
        return self.duracao

    def set_duracao(self, nova_duracao):
        self.duracao = nova_duracao

    def get_valor(self):
        preco = super().get_valor()
        preco -= super().get_valor() * super().get_desconto() / 100
        return preco

    def descreve_produto(self):
        print(f'DVD: {super().get_titulo()}')
        print(f'Duração: {self.get_duracao()}h')
        print(f'Valor: R${super().get_valor():.2f}')
        print(f'Desconto: {super().get_desconto()}%')
        print(f'Valor final: R${self.get_valor():.2f}')


# Os produtos devem ser colocados manualmente.
'''
De acordo com o enunciado da questão, os livros tem 10% de desconto,
os CD's tem 15% e os DVD's tem 20%.
Os demais produtos não têm desconto.
'''
produto_1 = Produto()
produto_1. set_titulo('Ferro de Passar a Vapor 1200W')
produto_1.set_valor(100)
produto_1.set_desconto(0)

produto_2 = Produto()
produto_2. set_titulo('Máquina de Lavar 12kg - 110v')
produto_2.set_valor(1898)
produto_2.set_desconto(0)

livro_1 = Livro()
livro_1.set_titulo('A Rainha Vermelha')
livro_1.set_autor('Victoria Aveyard')
livro_1.set_valor(40)
livro_1.set_desconto(10)

livro_2 = Livro()
livro_2.set_titulo('O Menino do Pijama Listrado')
livro_2.set_autor('John Boyne')
livro_2.set_valor(30)
livro_2.set_desconto(10)

cd_1 = CD()
cd_1.set_titulo('Night Visions')
cd_1.set_artista('Imagine Dragons')
cd_1.set_valor(34)
cd_1.set_desconto(15)

cd_2 = CD()
cd_2.set_titulo('Banda Calypso - Vol. 4')
cd_2.set_artista('Banda Calypso')
cd_2.set_valor(20)
cd_2.set_desconto(15)

dvd_1 = DVD()
dvd_1.set_titulo('Frozen - Uma Aventura Congelante')
dvd_1.set_duracao('1:42')
dvd_1.set_valor(40)
dvd_1.set_desconto(20)

dvd_2 = DVD()
dvd_2.set_titulo('Jogo da Imitação')
dvd_2.set_duracao('2:30')
dvd_2.set_valor(60)
dvd_2.set_desconto(20)

# inserção de cada produto na lista. Aceito dicas de como otimizar essa parte
lista = []
lista.append(produto_1)
lista.append(produto_2)
lista.append(livro_1)
lista.append(livro_2)
lista.append(cd_1)
lista.append(cd_2)
lista.append(dvd_1)
lista.append(dvd_2)

# Classe onde será feita a interação com o usuário
class Menu:
    def __init__(self):
        self.lista = []
        self.opcao = None
        self.carrinho = []

    def get_lista(self):
        return self.lista

    def set_lista(self, nova_lista):
        self.lista = nova_lista

    def get_opcao(self):
        return self.opcao

    def set_opcao(self, nova_opcao):
        self.opcao = nova_opcao

    def get_carrinho(self):
        return self.carrinho

    def set_carrinho(self, novo_carrinho):
        self.carrinho = novo_carrinho

    def exibir_produtos(self):
        self.set_lista(lista)
        print()
        print('-' * 40)
        print('         PRODUTOS DISPONÍVEIS')
        print('-' * 40)
        for index, produto in enumerate(self.get_lista()):
            print('-=' * 20)
            print(f'Produto {index + 1}')
            produto.descreve_produto()
            print('-=' * 20)
            print()

    def adicionar_produto(self):
        print()
        id_produto = int(input('Digite o id do produto que você quer adicionar ao  carrinho: '))
        print()

        self.get_carrinho().append(self.get_lista()[id_produto - 1])

    def remover_produto(self):
        print()
        if self.get_carrinho() == []:
            print('O carrinho está vazio.\n')
        else:
            self.mostrar_carrinho()
            id_produto = int(input('Digite o id do produto que você deseja remover do carrinho: '))
            print()

            del self.get_carrinho()[id_produto - 1]

    def mostrar_carrinho(self):
        valor_total = 0

        print()
        if self.get_carrinho() == []:
            print('O carrinho está vazio.\n')
        else:
            print('-' * 40)
            print('              CARRINHO')
            print('-' * 40)
            for index, produto in enumerate(self.get_carrinho()):
                print(f'Produto {index + 1}')
                produto.descreve_produto()
                print()

                valor_total += produto.get_valor()

            print(f'Valor total da compra: R${valor_total:.2f}\n')
    
    def executar(self):
        while self.get_opcao() != '4':
            print('-' * 40)
            print('                 MENU')
            print('-' * 40)
            print('[1] - Adicionar produto ao carrinho.')
            print('[2] - Remover produto do carrinho.')
            print('[3] - Mostrar carrinho.')
            print('[4] - Sair.')

            opcao = input('Opção desejada: ')

            self.set_opcao(opcao)

            if self.get_opcao() == '1':
                self.exibir_produtos()
                self.adicionar_produto()
            elif self.get_opcao() == '2':
                self.remover_produto()
            elif self.get_opcao() == '3':
                self.mostrar_carrinho()
            elif self.get_opcao() == '4':
                print('Até mais.')
            else:
                print('Opção inválida! Tente novamente.')

m = Menu()
m.executar()
