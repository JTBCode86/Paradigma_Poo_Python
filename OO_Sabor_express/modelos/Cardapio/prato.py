from modelos.Cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self._descricao = descricao