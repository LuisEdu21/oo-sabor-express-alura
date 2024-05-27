from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Lucas', 10)
restaurante_praca.receber_avaliacao('Luis', 6)
restaurante_praca.receber_avaliacao('Emy', 2)
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa','Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()