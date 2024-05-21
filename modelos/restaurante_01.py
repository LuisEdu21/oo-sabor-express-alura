class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

Restaurante_praca = Restaurante()

Restaurante_praca.nome = 'Praça'
Restaurante_praca.categoria = 'Gourmet'

Restaurante_pizza = Restaurante()

restaurante = [Restaurante_praca, Restaurante_pizza]

# 1- Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

Restaurante_praca.categoria = 'Italiana'

# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(Restaurante_praca.nome)

# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if Restaurante_praca.ativo == True:
    print('Restaurante Ativo!')

else:
    print('Restaurante Fechado!')

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

# 5 - Altere o valor do atributo nome para 'Bistrô'.

Restaurante_praca.nome = 'Bistrô'

# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

Restaurante_pizza.nome = 'Pizza Place'
Restaurante_pizza.categoria = 'Fast Food'

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if Restaurante_pizza.categoria == 'Fast Food':
    print('A categoria esta correta!')
else:
    print('A cetegoria esta diferente!')

# 8 - Mude o estado da instância restaurante_pizza para ativo.

Restaurante_pizza.ativo = True

# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print('O nome do restaurante é: {}, e a categoria deele é: {}'.format(Restaurante_praca.nome, Restaurante_praca.categoria))
print('O nome do restaurante é: {}, e a categoria deele é: {}'.format(Restaurante_pizza.nome, Restaurante_pizza.categoria))

# print(dir(Restaurante_praca))
print(vars(Restaurante_praca))