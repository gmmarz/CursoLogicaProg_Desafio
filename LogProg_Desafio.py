#Curso de lógica de programação 
#Desafio: Desenvolver uma aplicação simples para praticar os conceitos aprendidos: for, while , input e print.
#O operador de caixa de uma loja, cadastra cada cliente que comprar dados:  - Nome - Telefone e Endereço
#O fim do dia, quando operador digitar Fim termina o cadastro dos clientes.
#Sistem deve então realizar o sorteiro e um dos clientes, e informar qual o Nome do cliente sorteado e seu telefone.
import random

cli_lst = []

#Loop during work time to add clients that buy
while True:
    flg = input('Finalizar expediente (fim) Finalizar, (nxt)Próximo cliente: ').lower()
    if flg == 'fim':
        print('Fim do expediente')
        break
    else:
        dic = {'nome':'','tel':'','end':''}
        dic['nome'] = input('Nome cliente: ')
        dic['tel'] = input('Telefone: ')
        dic['end'] = input('Endereço: ')
        cli_lst.append(dic)

#Verificando se houve cliente para sortear:
if len(cli_lst)>=1:
    #Sortendo entre os clientes
    sorteado = random.randint(0,len(cli_lst)- 1)
    cli_Sorteado = cli_lst[sorteado]
    print(f'O cliente sorteado foi:\n Nome: {cli_Sorteado["nome"]}\nTelefone: {cli_Sorteado["tel"]}\nEndereço: {cli_Sorteado["end"]}')
else:
    print("Nenhum cliente cadastrador")
