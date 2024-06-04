def exibirMensagem(nome):
    print(f"Seja bem-vindo {nome}")
    return f'Usuário logado: {nome}'

#usuario=exibirMensagem('Mateus')
#print(usuario)

nome=(input("Digite seu nome: "))
exibirMensagem(nome)


