# Desafio - Sistema Bancário
from datetime import datetime

class ContaBancaria:
    def __init__(self,usuario_nome):
        primeiro_nome=usuario_nome.split(' ')[0]
        usuario_nome=usuario_nome.replace(' ','_')
        saldo=self.ler_saldo(usuario_nome)
        self.opcoes(primeiro_nome,usuario_nome,saldo)

    def ler_saldo(self,usuario_nome):
        with open(f'{usuario_nome}_extrato.txt','r') as file:
                for line in file:
                    if 'Saldo' in line:
                        dividir_linha=line.split(' ')
                        saldo=dividir_linha[-1]
                        saldo_formatado=saldo
                        saldo=float(saldo.replace('R$',''))
                print('Saldo atual:',saldo_formatado)
                return saldo

    def opcoes(self,primeiro_nome,usuario_nome,saldo):
        print(f''' 
{primeiro_nome}, segue abaixo as opçoes de operação:
    1 - Deposito
    2 - Saque
    3 - Extrato
    4 - Sair do sistema
        
        ''')

        opcao_escolhida=input('Digite uma opção:')
        if int(opcao_escolhida) < 1 or int(opcao_escolhida)>4:
            print('Opção inválida.')
            self.opcoes(primeiro_nome,usuario_nome)
        if opcao_escolhida == '1':
            self.deposito(primeiro_nome,usuario_nome,saldo)
        if opcao_escolhida == '2':
            self.saque(primeiro_nome,usuario_nome,saldo)
        if opcao_escolhida == '3':
            self.extrato(primeiro_nome,usuario_nome,saldo)
        if opcao_escolhida == '4':
            self.sair()

    def data_time(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)	
        return dt_string

    def deposito(self,primeiro_nome,usuario_nome,saldo):
        valor_deposito=float(input('Digite o valor a ser depositado:'))
        dt_string=self.data_time()
        saldo=saldo+valor_deposito
        impressao= (f'Deposito - Data e hora: {dt_string},  Valor: +R${valor_deposito},  Saldo: R${saldo}\n')
        with open(f'{usuario_nome}_extrato.txt','a') as file:
            file.write(impressao)
        self.opcoes(primeiro_nome,usuario_nome,saldo)

    def saque(self,primeiro_nome,usuario_nome,saldo):
        valor_saque=float(input('Digite o valor a ser sacado:'))
        if valor_saque > saldo:
            print('Operaçao não pode ser efetuada. Saldo insuficiente.')
            return
        dt_string=self.data_time()
        saldo=saldo-valor_saque
        impressao= (f'Saque    - Data e hora: {dt_string},  Valor: +R${valor_saque},  Saldo: R${saldo}\n')
        with open(f'{usuario_nome}_extrato.txt','a') as file:
            file.write(impressao)  
        self.opcoes(primeiro_nome,usuario_nome,saldo)

    def extrato(self,primeiro_nome,usuario_nome,saldo):
        with open(f'{usuario_nome}_extrato.txt','r') as file:
            for line in file:
                print(line,end='')
        self.opcoes(primeiro_nome,usuario_nome,saldo)    

    def sair(self):
        print('Obrigado e volte sempre.')


class LoginCliente:
    def __init__(self):
        cpf=input('Favor digitar seu CPF:')
        with open('Clientes_Cadastrados.txt','r') as file:
                for line in file: #obtençao do nome do usuario
                    if cpf in line:
                        usuario=line.split(',')
                        usuario_nome=usuario[1]
                        print(f'Bem vindo {usuario[1]}!')
                        senha=input('Favor digitar sua senha:')
                        if senha == usuario[2]: #confirmaçao da senha
                            ContaBancaria(usuario_nome)
                            return
                        else:
                            return print('Senha inválida.')
                print('CPF não encontrado.')

cliente=LoginCliente()