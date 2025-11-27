class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

remetentes = {}
destinatarios = {}
fila_mensagens = Queue()   
caixas_entrada = {}
historico_geral = []

def cadastrar_pessoa(tipo, nome):
    if tipo == "remetente":
        remetentes[nome] = {"nome": nome}
    elif tipo == "destinatario":
        destinatarios[nome] = {"nome": nome}
    print(f"{tipo.title()} '{nome}' cadastrado com sucesso!")

def enviar_mensagem(remetente, destinatario, texto):
    if remetente not in remetentes:
        print("Remetente não cadastrado.")
        return
    if destinatario not in destinatarios:
        print("Destinatário não cadastrado.")
        return

    mensagem = {
        "remetente": remetente,
        "destinatario": destinatario,
        "texto": texto
    }
    fila_mensagens.enqueue(mensagem)
    print("Mensagem adicionada à fila de envio 💌")

def entregar_mensagem():
    """Entrega a próxima mensagem da fila (FIFO)"""
    if fila_mensagens.isEmpty():
        print("Não há mensagens na fila para entregar.")
        return

    mensagem = fila_mensagens.dequeue()
    dest = mensagem["destinatario"]

    if dest not in caixas_entrada:
        caixas_entrada[dest] = []
    caixas_entrada[dest].append(mensagem)
    historico_geral.append(mensagem)

    print(f"💖 Mensagem entregue de {mensagem['remetente']} para {dest}!")

def listar_recebidas(nome):
    """Lista mensagens recebidas"""
    if nome not in caixas_entrada or not caixas_entrada[nome]:
        print(f"{nome} não tem mensagens recebidas.")
        return

    print(f"\n📥 Mensagens recebidas por {nome}:")
    for i, msg in enumerate(caixas_entrada[nome], 1):
        print(f"{i}. De: {msg['remetente']} - Texto: {msg['texto']}")

def listar_enviadas(nome):
    """Lista mensagens enviadas"""
    enviadas = [m for m in historico_geral if m["remetente"] == nome]
    if not enviadas:
        print(f"{nome} não enviou nenhuma mensagem ainda.")
        return

    print(f"\n📤 Mensagens enviadas por {nome}:")
    for i, msg in enumerate(enviadas, 1):
        print(f"{i}. Para: {msg['destinatario']} - Texto: {msg['texto']}")

def mostrar_historico():
    """Mostra o histórico geral"""
    if not historico_geral:
        print("Nenhuma mensagem foi entregue ainda.")
        return

    print("\n📜 Histórico geral de mensagens entregues:")
    for i, msg in enumerate(historico_geral, 1):
        print(f"{i}. {msg['remetente']} → {msg['destinatario']} | {msg['texto']}")
        
        
def pesquisar_mensagens(nome):
    resultados = [
        m for m in historico_geral
        if m["remetente"] == nome or m["destinatario"] == nome
    ]

    if not resultados:
        print("Nenhuma mensagem encontrada para esse nome.")
        return

    print(f"\n🔍 Mensagens relacionadas a '{nome}':")
    for i, msg in enumerate(resultados, 1):
        print(f"{i}. {msg['remetente']} → {msg['destinatario']} | {msg['texto']}")

def ranking_romanticos():
    contador = {}

    for msg in historico_geral:
        remet = msg["remetente"]
        contador[remet] = contador.get(remet, 0) + 1

    if not contador:
        print("Ainda não há mensagens entregues 💌")
        return

    print("\n🏆 Ranking dos mais românticos:")
    ranking = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    for pos, (nome, qtd) in enumerate(ranking, 1):
        print(f"{pos}º - {nome} 💖 ({qtd} mensagens)")
       
        
import time
import os

# Cores ANSI
RED = "\033[31m"
CORAL = "\033[38;5;209m"
RESET = "\033[0m"

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def apresentacao():
    limpar()

    title = [


"██╗     ███████╗████████╗████████╗███████╗████████╗██████╗       ██╗      ██████╗ ██╗   ██╗███████╗",
"██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗      ██║     ██╔═══██╗██║   ██║██╔════╝",
"██║     █████╗     ██║      ██║   █████╗     ██║   ██████╔╝      ██║     ██║   ██║██║   ██║█████╗  ",
"██║     ██╔══╝     ██║      ██║   ██╔══╝     ██║   ██╔══██╗      ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ",
"███████╗███████╗   ██║      ██║   ███████╗   ██║   ██║  ██║      ███████╗╚██████╔╝ ╚████╔╝ ███████╗",
"╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝      ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝",
    ]

    # Pintar de vermelho / e deixar o V coral
    print()
    for linha in title:
        linha_colorida = linha.replace(
            "V", f"{CORAL}V{RED}"
        )
        print(RED + linha_colorida + RESET)
        time.sleep(0.05)

    print("\n" + RED + "Carregando o sistema romântico..." + RESET, end="")
    for _ in range(5):
        print("💕", end="", flush=True)
        time.sleep(0.4)

    time.sleep(1)
    limpar()
        

def menu_principal():
    while True:
        print("\n" + "═" * 60)
        print("💗 C O R R E I O   D O   A M O R  💗".center(60))
        print("═" * 60)

        print("""
        1. 💌 Cadastro
        2. 👥 Mensagens
        3. 🏆 Extras
        0. ❌ Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_pessoas()
        elif opcao == "2":
            menu_mensagens()
        elif opcao == "3":
            menu_extras()
        elif opcao == "0":
            print("Saindo... obrigada por espalhar amor 💘")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

def menu_pessoas():
    while True:
        print("\n--- 👥 MENU DE Cadastro ---")
        print("""
        1. 💗 Cadastrar remetente
        2. 💐 Cadastrar destinatário
        0. 🔙 Voltar
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do remetente: ")
            cadastrar_pessoa("remetente", nome)

        elif opcao == "2":
            nome = input("Nome do destinatário: ")
            cadastrar_pessoa("destinatario", nome)

        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")
def menu_mensagens():
    while True:
        print("\n--- 💌 MENU DE MENSAGENS ---")
        print("""
        1. ✉️ Enviar mensagem
        2. 📬 Entregar próxima mensagem
        3. 📥 Listar recebidas
        4. 📤 Listar enviadas
        5. 🔍 Pesquisar mensagens
        6. 📜 Histórico geral
        0. 🔙 Voltar
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            remetente = input("Quem está enviando? ")
            destinatario = input("Para quem? ")
            texto = input("Escreva sua mensagem: ")
            enviar_mensagem(remetente, destinatario, texto)

        elif opcao == "2":
            entregar_mensagem()

        elif opcao == "3":
            nome = input("Listar recebidas de quem? ")
            listar_recebidas(nome)

        elif opcao == "4":
            nome = input("Listar enviadas por quem? ")
            listar_enviadas(nome)

        elif opcao == "5":
            termo = input("Pesquisar por nome: ")
            pesquisar_mensagens(termo)

        elif opcao == "6":
            mostrar_historico()

        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")
def menu_mensagens():
    while True:
        print("\n--- 💌 MENU DE MENSAGENS ---")
        print("""
        1. ✉️ Enviar mensagem
        2. 📬 Entregar próxima mensagem
        3. 📥 Listar recebidas
        4. 📤 Listar enviadas
        5. 🔍 Pesquisar mensagens
        6. 📜 Histórico geral
        0. 🔙 Voltar
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            remetente = input("Quem está enviando? ")
            destinatario = input("Para quem? ")
            texto = input("Escreva sua mensagem: ")
            enviar_mensagem(remetente, destinatario, texto)

        elif opcao == "2":
            entregar_mensagem()

        elif opcao == "3":
            nome = input("Listar recebidas de quem? ")
            listar_recebidas(nome)

        elif opcao == "4":
            nome = input("Listar enviadas por quem? ")
            listar_enviadas(nome)

        elif opcao == "5":
            termo = input("Pesquisar por nome: ")
            pesquisar_mensagens(termo)

        elif opcao == "6":
            mostrar_historico()

        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")
def menu_extras():
    while True:
        print("\n--- 🏆 EXTRAS ---")
        print("""
        1. 💞 Ranking dos mais românticos
        0. 🔙 Voltar
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ranking_romanticos()

        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")



if __name__ == "__main__":
    apresentacao()
    menu_principal()
