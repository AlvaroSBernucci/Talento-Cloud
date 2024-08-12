def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o ano.")

def main():
    nome = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    
    print(f"Nome: {nome}")
    print(f"Idade em {ano_atual}: {idade} anos")
main()