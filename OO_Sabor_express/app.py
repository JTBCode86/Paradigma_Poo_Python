from modelos.restaurante import Restaurante
from modelos.Cardapio.bebida import Bebida
from modelos.Cardapio.prato import Prato

restaurante_praca = Restaurante('praça','gourmet')

bebida_suco = Bebida('Suco de Menancia',5.0,'grande') 
prato_paozinho = Prato('Paozinho',2.00,'O melhor pao da cidade')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    #Restaurante.listar_restaurantes()

    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()