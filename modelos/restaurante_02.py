class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca  = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano 


carro_1 = Carro('Sedan','Cinza','2015')
carro_2 = Carro('Hatch','Branco','2017')

# 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante_2:
    def __init__(self,nome,categoria,estrela,deliveri):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.estrela = estrela
        self.deliveri = deliveri

    # 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_1 = Restaurante_2('Felipe Burguer','Lanchonete',4.5,True)
restaurante_1 = Restaurante_2('Gulosos','Lanchonete',4,True)

# 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

# 5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self,nome,sexo,idade,cpf):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.cpf = cpf

cliente_1 = Cliente('Lucas Henrique','M','24',112231412)