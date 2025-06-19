import json

# INSTRUÇÕES DE USO:
# Tenha certeza de que o arquivo "agenda.json"
# está no mesmo diretório que "agenda.py".

agenda = {}

def menu_principal():
    print(f"\n{' Agenda de Contatos ':=^30}")
    print("[1] Adicionar contato")
    print("[2] Buscar contato")
    print("[3] Editar contato")
    print("[4] Remover contato")
    print("[5] Sair")
    print("=" * 30 + "\n")
    opcao = input("Digite o número da operação desejada: ")
    return opcao

def adicionar_contato():
    usuario = "@" + input("\nDigite sua tag de usuário: ").lower()
    if usuario in agenda:
        print(f"ERRO: Tag de usuário {usuario} já existe.")
        return
    
    nome = input("\nDigite seu nome de usuário: ")
    
    print("\nExemplo de número de telefone: DDNNNN-NNNN.")
    print("Não inclua um '9' a mais depois do DDD.")
    print("D: DDD, N: Dígito.")
    celular = input("Digite seu número de telefone: ")
    if len(celular) != 11 or celular[6] != "-":
        print(f"ERRO: Número de telefone inválido.")
        return
    
    print("\nExemplo de e-mail: nomedoemail@gmail.com")
    email = input("Digite seu endereço eletrônico (e-mail): ")
    if "@" not in email or "." not in email[(email.index('@')):]: # A segunda condição checa 
        print("ERRO: E-mail inválido.")                           # se não há '.' depois do '@'.
        return                                                    # EX: 'teste.@gmailcom' é inválido.
    
    agenda[usuario] = [nome, celular, email]
    salvar_agenda()
    print(f"Contato {usuario} adicionado com sucesso.")

def buscar_contato(usuario : str):
    if usuario in agenda:
        auxtelefone = agenda[usuario][1]
        print("\n" + "=" * 30)
        print(f"Contato: {usuario}")
        print("=" * 30)
        print(f"Nome: {agenda[usuario][0]}")
        print(f"Telefone: {"(" + auxtelefone[:2] + ") 9" + auxtelefone[2:]}")
        print(f"E-mail: {agenda[usuario][2]}")
        print("=" * 30)
    else:
        print(f"ERRO: Usuário {usuario} não existe.")
    
def editar_contato(usuario1 : str):
    global agenda
    usuario = usuario1
    if usuario in agenda:
        campos = {"contato" : 0, "nome" : 1, "telefone" : 2, "e-mail" : 3}

        while True:
            buscar_contato(usuario)
            campo_edicao = input("Escolha o campo para editar ou [sair] para sair: ").lower()
            if campo_edicao == "sair":
                print("Edição encerrada com sucesso.")
                break
            if campo_edicao in campos:
                if campos[campo_edicao] == 0:
                    novatag = "@" + input("\nDigite a nova tag de usuário: ").lower()
                    if novatag in agenda:
                        print(f"ERRO: Tag de usuário {novatag} já existe.")
                    else:
                        agenda[novatag] = agenda[usuario]
                        print(f"Tag {agenda.pop(usuario)} virou {novatag} com sucesso.")
                        usuario = novatag

                elif campos[campo_edicao] == 1:
                    novonome = input("\nDigite o novo nome de usuário: ")
                    print(f"Nome {agenda[usuario][0]} virou {novonome} com sucesso.")
                    agenda[usuario][0] = novonome

                elif campos[campo_edicao] == 2:
                    print("\nExemplo de número de telefone: DDNNNN-NNNN.")
                    print("Não inclua um '9' a mais depois do DDD.")
                    print("D: DDD, N: Dígito.")
                    novotelefone = input("\nDigite o novo telefone: ")
                    if len(novotelefone) != 11 or novotelefone[6] != "-":
                        print(f"ERRO: Número de telefone inválido.")
                    else:
                        print(f"Nome {agenda[usuario][1]} virou {novotelefone} com sucesso.")
                        agenda[usuario][1] = novotelefone

                elif campos[campo_edicao] == 3:
                    print("\nExemplo de e-mail: nomedoemail@gmail.com")
                    novoemail = input("\nDigite o novo e-mail: ")
                    if "@" not in novoemail or "." not in novoemail[(novoemail.index('@')):]:
                        print("ERRO: E-mail inválido.")
                    else:                      
                        print(f"Nome {agenda[usuario][2]} virou {novoemail} com sucesso.")
                        agenda[usuario][2] = novoemail

            else:
                print(f"ERRO: Campo {campo_edicao} não existe.")
        salvar_agenda()
    else:
        print(f"ERRO: Usuário {usuario} não existe.")

def remover_contato(usuario1 : str):
    global agenda
    usuario = usuario1
    if usuario in agenda:
        print("[s] para sim, [n] para não")
        certeza = input(f"Tem certeza de que quer remover o contato {usuario}? ").lower()
        if certeza == "s":
            agenda.pop(usuario)
            print(f"Contato {usuario1} deletado com sucesso.")
            salvar_agenda()
        else:
            print(f"Contato {usuario} não foi deletado.")
    else:
        print(f"ERRO: Usuário {usuario} não existe.")   
    
def salvar_agenda():
    with open("agenda.json", "w") as saida:
        json.dump(agenda, saida)
 
def carregar_agenda():
    global agenda
    with open("agenda.json", "r", encoding='utf-8') as agendajson:
        agenda = json.load(agendajson)

def encerrar_programa():
    confirmar = 1
    confirmar = input("Digite 'confirmar' para finalizar o programa: ")
    return confirmar

carregar_agenda()

print("<>" * 36)
print(f"<>{'Agenda de Contatos':^68}<>")
print("Desenvolvido por: Willyam A. Medeiros e Arthur Herbster Fernandes Vogel")
print(f"<>{'No dia 18/06/25':^68}<>")
print("<>" * 36)

while True:
    opcao = menu_principal()[0:1] 
    if opcao.isnumeric():
        if int(opcao) in range(1, 6, 1):
            if   opcao == "1": # ADICIONAR CONTATO
                adicionar_contato()

            elif opcao == "2": # BUSCAR CONTATO
                usuario = "@" + input("\nDigite a tag de usuário para pesquisar: ").lower()
                buscar_contato(usuario)

            elif opcao == "3": # EDITAR CONTATO
                usuario = "@" + input("\nDigite a tag de usuário para editar: ").lower()
                editar_contato(usuario)

            elif opcao == "4": # REMOVER CONTATO
                usuario = "@" + input("\nDigite a tag de usuário para remover: ").lower()
                remover_contato(usuario)

            elif opcao == "5": # ENCERRAR PROGRAMA
                if encerrar_programa() == "confirmar":
                    print("Programa encerrado com sucesso.")
                    break
                else:
                    print("Programa não foi encerrado.")
        else: 
            print(f"ERRO: A opção {opcao} não é um número inteiro entre 1 e 5.")
    else:
        print(f"ERRO: A opção {opcao} não é uma opção válida.")
        print("Opções válidas: 1, 2, 3, 4, 5.")