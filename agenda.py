import json

agenda = {}

def menu_principal():
    print("\n--- AGENDA DE CONTATOS ---")
    print("[1] Adicionar contato")
    print("[2] Buscar contato")
    print("[3] Editar contato")
    print("[4] Remover contato")
    print("[5] Sair\n")
    opcao = input("Digite o número da operação desejada: ")
    return opcao

def adicionar_contato(usuario : str, nome : str, celular : str, email : str):
    agenda[usuario] = [nome, celular, email]
    salvar_agenda()

def buscar_contato(usuario : str):
    if usuario in agenda:
        print(agenda[usuario])
    else:
        print(f"ERRO: Usuário {usuario} não existe.")
    
def editar_contato(usuario : str, campo : str, novo_valor : str):
    if usuario in agenda:
        pass
    salvar_agenda()

def remover_contato(usuario : str):
    pass
    salvar_agenda()

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

while True:
    opcao = menu_principal()
    if opcao.isnumeric():
        if int(opcao) in range(1, 6, 1):
            if   opcao == "1": # ADICIONAR CONTATO
                usuario = "@" + input("\nDigite sua tag de usuário: ").lower()
                if usuario in agenda:
                    print(f"ERRO: Tag de usuário {usuario} já existe.")
                    continue
                
                nome = input("\nDigite seu nome de usuário: ")
                
                print("\nExemplo de número de telefone: DDNNNN-NNNN.")
                print("Não inclua um '9' a mais depois do DDD.")
                print("D: DDD, N: Dígito.")
                celular = input("Digite seu número de telefone: ")
                if len(celular) != 11 or celular[6] != "-":
                    print(f"ERRO: Número de telefone inválido.")
                    continue
                
                print("\nExemplo de e-mail: nomedoemail@gmail.com")
                email = input("Digite seu endereço eletrônico (e-mail): ")
                if "@" not in email or "." not in email[(email.index('@')):]: # A segunda condição checa 
                    print("ERRO: E-mail inválido.")                     # se não há '.' depois do '@'.
                    continue                                            # EX: 'teste.@gmailcom' é inválido.
                
                adicionar_contato(usuario, nome, celular, email)

            elif opcao == "2": # BUSCAR CONTATO
                usuario = "@" + input("\nDigite a tag de usuário para pesquisar: ").lower()
                buscar_contato(usuario)

            elif opcao == "3": # EDITAR CONTATO
                pass

            elif opcao == "4": # REMOVER CONTATO
                pass

            elif opcao == "5": # ENCERRAR PROGRAMA
                if encerrar_programa() == "confirmar":
                    print("Programa encerrado com sucesso.")
                    break
                else:
                    print("Programa não encerrado.")
        else:
            print(f"ERRO: A opção {opcao} não é um número inteiro entre 1 e 5.")
    else:
        print(f"ERRO: A opção {opcao} não é uma opção válida.")
        print("Opções válidas: 1, 2, 3, 4, 5.")