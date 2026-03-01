from random import randint
class Conta :
    def __init__(self, nome_titular: str):
        self.nome_titular = nome_titular
        self.num_conta = randint(1000, 9999)
        self.saldo_cliente = 0.0
     
    def depositar(self, valor_deposito: float,):
        self.saldo_cliente += valor_deposito
        return f'Saldo disponivel: {self.saldo_cliente} '

    def sacar(self, valor_saque:float):
        if valor_saque > self.saldo_cliente :
           return "O valor do saque é maior do que o saldo disponivel"
        else:
            self.saldo_cliente -= valor_saque
            return f"Saque Realizado com sucesso\nSaldo Diponivel: {self.saldo_cliente}"

    def transferencia(self, valor_transferencia:float, conta_destino: "Conta" ):
        if valor_transferencia > self.saldo_cliente :
            return f"Saldo insuficiente para este valor"
        else: 
            self.saldo_cliente -= valor_transferencia
            conta_destino.saldo_cliente = valor_transferencia

      
    
    def verificar_saldo(self) :
        return self.saldo_cliente

    def __str__(self):
        return f"Nome Titular: {self.nome_titular}\nNumero da conta: {self.num_conta}\n Saldo:{self.saldo_cliente}"
        pass
c = Conta("Rafael")
c2 = Conta("Gigi")

# Fazendo um deposito em c
valor_deposito = float(input("Digite qual o valor que gostaria de depositar: "))
c.depositar(valor_deposito)

#Sacando um valor em c
valor_saque = float(input("Digite o valor que gostaria de sacar: "))
c.sacar(valor_saque)

# Fazendo trasnferencia
valor_transferencia = float(input("digite o valor da trasnferencia: "))
c.transferencia(valor_transferencia, c2)

print(c)
print(c2)