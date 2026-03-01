class Carrinho: 
    def __init__(self,nome:str):
        self.nome_dono = nome
        self.item = {}
    
    def adcionar_item(self, nome_item:str, valor_item:float, qtd_item:int):
        self.item[nome_item] = {
           "valor_item": valor_item,
           "qtd_item": qtd_item
            }

    def remover_item(self, nome_item:str):
        del self.item[nome_item]
        return f'Item {nome_item} deletado !'
    
    def atualizar_qtd(self, nome_item:str, qtd:int, ):
        if qtd <= 0 :
            del self.item[nome_item]
        else: 
            self.item[nome_item]['qtd_item'] = qtd

    def somar_valores(self) :
        vl_total =0
        for i in self.item :
            vl_total += (self.item[i]['qtd_item'] * self.item[i]['valor_item'])
        return f'O valor total da compra é {vl_total}'

    def __str__(self):
        return f'Carrinho do {self.nome_dono}\nItens: {self.item}'
    
carrinho1 = (Carrinho("Rafa"))

carrinho1.adcionar_item('booster', 25, 4)
carrinho1.adcionar_item('flores', 15, 4)

carrinho1.atualizar_qtd('booster', 10)

print(carrinho1.somar_valores())

print(carrinho1)