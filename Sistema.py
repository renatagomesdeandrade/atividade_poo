#1-Pessoa Fisica / 2- pessoa juridica / 3- sair
#Cadastrar pessoa fisica / 2 - lista pessoa fisica / 3 - sair
#Cadastrar pessoa juridica / 2 - listar pessoa juridica / 3 - sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica


def main():
    lista_pf = []
    while True:
        opcao = int(input("Escolha uma opção: 1- Pessoa Física / 2- Pessoa Juridica / 0- Sair"))
        if opcao == 1:
            while True: 
                opcao_pf = int(input("Escolha uma opção: 1- Cadastrar Pessoa Física / 2- Listar Pessoa Física /0- Voltar ao menu anterior "))
                #Cadastrar uma Pessoa Física
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa física")
                    novapf.cpf = input("Digite o CPF")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente números): "))

                    data_nascimento = input("Digite a data de nascimento (dd/MM/aaaa)")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365 #Calcula a idade da pessoa

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue #Retorna ao inicio do loop

                    #Cadastro de endereço
                    novo_end_pf.logradouro = input("Digte o logradouro: ")
                    novo_end_pf.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial? S ou N") 
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!!")

                    #LISTA PESSOA FÍSICA
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print(f"Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                #SAIR DO MENU ATUAL
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")

                else:
                    print("Opção inválida, por favor digite uma das opções indicadas: ")

        elif opcao == 2:
            print("Funcionalidade para pessoa juridica não implementadas")
            pass

        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema! Valeu!")
            break

        else:
            print("Opção inválida, por favor digite uma das opções válidas")    


if __name__ == "__main__":
    main() #Chama a função principal
