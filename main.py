import os
import time
import smtplib
from email.message import EmailMessage

# -----------------------------
# Estruturas de Dados
# -----------------------------

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

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0

class Nodo:
    def __init__(self, nome):
        self.nome = nome
        self.esq = None
        self.dir = None

class ArvoreUsuarios:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome):
        if self.raiz is None:
            self.raiz = Nodo(nome)
        else:
            self._inserir(self.raiz, nome)

    def _inserir(self, nodo, nome):
        if nome == nodo.nome:
            return  # já existe
        if nome < nodo.nome:
            if nodo.esq is None:
                nodo.esq = Nodo(nome)
            else:
                self._inserir(nodo.esq, nome)
        else:
            if nodo.dir is None:
                nodo.dir = Nodo(nome)
            else:
                self._inserir(nodo.dir, nome)

    def buscar(self, nome):
        return self._buscar(self.raiz, nome)

    def _buscar(self, nodo, nome):
        if nodo is None:
            return None
        if nome == nodo.nome:
            return nodo
        if nome < nodo.nome:
            return self._buscar(nodo.esq, nome)
        else:
            return self._buscar(nodo.dir, nome)

    def listar_in_order(self):
        res = []
        self._in_order(self.raiz, res)
        return res

    def _in_order(self, nodo, res):
        if nodo is None:
            return
        self._in_order(nodo.esq, res)
        res.append(nodo.nome)
        self._in_order(nodo.dir, res)

class GrafoConexoes:
    def __init__(self):
        # dicionário: remetente -> {destinatario: contador}
        self.adj = {}

    def adicionar_aresta(self, remetente, destinatario):
        if remetente not in self.adj:
            self.adj[remetente] = {}
        self.adj[remetente][destinatario] = self.adj[remetente].get(destinatario, 0) + 1

    def conexoes_de(self, nome):
        return self.adj.get(nome, {})

# -----------------------------
# Banco de dados em memória
# -----------------------------
usuarios = ArvoreUsuarios()        # árvore de usuários cadastrados
fila_mensagens = Queue()           # rascunhos / fila de envio
caixas_entrada = {}                # nome -> [mensagens]
historico_geral = []               # lista de mensagens entregues
pilha_acoes = Stack()              # para undo (últimas entregas)
grafo = GrafoConexoes()            # conexões remetente->destinatario

# Modelos prontos
modelos_prontos = {
    1: "Desde que te conheci, meu coração bate mais forte. 💖",
    2: "Você ilumina meus dias como o sol ilumina o amanhecer. ☀️",
    3: "Se eu fosse um poeta, todas as minhas rimas seriam sobre você. ✨",
}

# -----------------------------
# Utilitários UI
# -----------------------------
RED = "\033[31m"
CORAL = "\033[38;5;209m"
RESET = "\033[0m"

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def apresentacao():
    limpar()
    title = [
"██╗     ███████╗████████╗████████╗███████╗██████╗       ██╗      ██████╗ ██╗   ██╗███████╗",
"██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗      ██║     ██╔═══██╗██║   ██║██╔════╝",
"██║     █████╗     ██║      ██║   █████╗  ██████╔╝      ██║     ██║   ██║██║   ██║█████╗  ",
"██║     ██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗      ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ",
"███████╗███████╗   ██║      ██║   ███████╗██║  ██║      ███████╗╚██████╔╝ ╚████╔╝ ███████╗",
"╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝      ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝",
    ]
    print()
    for linha in title:
        linha_colorida = linha.replace("V", f"{CORAL}V{RED}")
        print(RED + linha_colorida + RESET)
        time.sleep(0.02)
    print("\n" + RED + "Carregando o sistema romântico..." + RESET, end="")
    for _ in range(3):
        print("💕", end="", flush=True)
        time.sleep(0.3)
    time.sleep(0.6)
    limpar()

# -----------------------------
# Envio de e-mail REAL (SMTP)
# -----------------------------
smtp_cache = {
    "server": None,
    "email": None,
    "senha": None
}

def enviar_email_smtp(remetente_envio, senha_envio, destino_email, assunto, corpo):
    """Envia um email real via Gmail SMTP SSL. Retorna True se enviado com sucesso."""
    try:
        msg = EmailMessage()
        msg["From"] = remetente_envio
        msg["To"] = destino_email
        msg["Subject"] = assunto
        msg.set_content(corpo)

        # detecta servidor pelo domínio do remetente - por enquanto foco em Gmail
        servidor = "smtp.gmail.com"
        porta = 465

        with smtplib.SMTP_SSL(servidor, porta) as smtp:
            smtp.login(remetente_envio, senha_envio)
            smtp.send_message(msg)

        print("✅ E-mail REAL enviado via SMTP.")
        return True
    except Exception as e:
        print("❌ Falha ao enviar e-mail real:", e)
        return False

# -----------------------------
# Funções principais do sistema
# -----------------------------
def cadastrar_usuario_interativo():
    nome = input("Digite seu nome para cadastro: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    if usuarios.buscar(nome):
        print("Esse usuário já existe. Faça login.")
        return
    usuarios.inserir(nome)
    print(f"Usuário '{nome}' cadastrado com sucesso!")

def login_interativo():
    while True:
        nome = input("Digite seu nome para entrar (ou 'sair' para cancelar): ").strip()
        if nome.lower() == "sair":
            return None
        if usuarios.buscar(nome):
            print(f"Bem-vindo(a), {nome} 💖")
            return nome
        print("Usuário não encontrado. Cadastre-se primeiro!")

def entregar_mensagem_obj(mensagem, enviar_real=False, remetente_envio_email=None, senha_envio=None):
    """Entrega a mensagem no sistema (caixa do destinatário) e atualiza estruturas.
       Se enviar_real for True, tenta enviar e-mail real (destinatário será tratado como endereço)."""
    dest = mensagem["destinatario"]
    remet = mensagem["remetente"]

    # Adiciona à caixa de entrada local
    if dest not in caixas_entrada:
        caixas_entrada[dest] = []
    caixas_entrada[dest].append(mensagem)
    historico_geral.append(mensagem)
    pilha_acoes.push(mensagem)  # empilha para permitir undo
    grafo.adicionar_aresta(remet, dest)

    # Tenta envio real caso solicitado
    if enviar_real and remetente_envio_email and senha_envio:
        assunto = f"Você recebeu uma mensagem de {remet}"
        corpo = f"De: {remet}\n\n{mensagem['texto']}"
        success = enviar_email_smtp(remetente_envio_email, senha_envio, dest, assunto, corpo)
        if not success:
            print("➡️ A entrega no sistema foi feita, mas o envio SMTP falhou.")
    else:
        print(f"💖 Mensagem entregue de {remet} para {dest} (sistema).")

def entregar_proxima_da_fila(enviar_real=False):
    if fila_mensagens.isEmpty():
        print("Não há mensagens na fila (rascunhos).")
        return
    mensagem = fila_mensagens.dequeue()
    # Se o destinatário parece um e-mail (contém @), e quiser enviar_real, será usado
    if enviar_real and "@" in mensagem["destinatario"]:
        # requisitar credenciais SMTP do remetente (cache)
        if smtp_cache["email"] is None:
            smtp_cache["email"] = input("Digite seu e-mail (para SMTP, ex: seu@gmail.com): ").strip()
            smtp_cache["senha"] = input("Digite sua senha de app (App Password): ").strip()
            smtp_cache["server"] = "smtp.gmail.com"
        entregar_mensagem_obj(mensagem, enviar_real=True, remetente_envio_email=smtp_cache["email"], senha_envio=smtp_cache["senha"])
    else:
        entregar_mensagem_obj(mensagem)

def listar_recebidas(nome):
    if nome not in caixas_entrada or not caixas_entrada[nome]:
        print(f"{nome} não tem mensagens recebidas.")
        return
    print(f"\n📥 Mensagens recebidas por {nome}:")
    for i, msg in enumerate(caixas_entrada[nome], 1):
        print(f"{i}. De: {msg['remetente']} - Texto: {msg['texto']}")

def listar_enviadas(nome):
    enviadas = [m for m in historico_geral if m["remetente"] == nome]
    if not enviadas:
        print(f"{nome} não enviou nenhuma mensagem ainda.")
        return
    print(f"\n📤 Mensagens enviadas por {nome}:")
    for i, msg in enumerate(enviadas, 1):
        print(f"{i}. Para: {msg['destinatario']} - Texto: {msg['texto']}")

def mostrar_historico():
    if not historico_geral:
        print("Nenhuma mensagem foi entregue ainda.")
        return
    print("\n📜 Histórico geral:")
    for i, msg in enumerate(historico_geral, 1):
        print(f"{i}. {msg['remetente']} → {msg['destinatario']} | {msg['texto']}")

def pesquisar_mensagens(nome):
    resultados = [m for m in historico_geral if m["remetente"] == nome or m["destinatario"] == nome]
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

def desfazer_ultima_entrega():
    if pilha_acoes.isEmpty():
        print("Nada para desfazer.")
        return
    msg = pilha_acoes.pop()
    dest = msg["destinatario"]
    # Remove da caixa de entrada (primeira ocorrência igual)
    if dest in caixas_entrada:
        for i, m in enumerate(caixas_entrada[dest]):
            if m is msg:
                caixas_entrada[dest].pop(i)
                break
    # Remove do histórico (primeira ocorrência igual)
    for i, m in enumerate(historico_geral):
        if m is msg:
            historico_geral.pop(i)
            break
    print("✅ Última entrega desfeita com sucesso.")

# -----------------------------
# Menus e fluxos
# -----------------------------
def enviar_mensagem_menu(usuario_logado):
    print("\n--- ✉️ ENVIAR MENSAGEM ---")
    destinatario = input("Para quem deseja enviar? (coloque nome ou e-mail): ").strip()
    if not destinatario:
        print("Destinatário inválido.")
        return

    print("""
    1. ✍️ Escrever texto próprio
    2. 💝 Usar mensagem pronta
    3. 👤 Enviar como ANÔNIMO
    """)
    escolha = input("Opção: ").strip()

    if escolha == "1":
        texto = input("Escreva sua mensagem: ").strip()
        remetente = usuario_logado

    elif escolha == "2":
        print("\n💌 Modelos disponíveis:")
        for num, modelo in modelos_prontos.items():
            print(f"{num}. {modelo}")
        try:
            num_escolhido = int(input("Escolha um modelo: ").strip())
            texto = modelos_prontos.get(num_escolhido, "Mensagem de amor 💖")
        except:
            texto = "Mensagem de amor 💖"
        remetente = usuario_logado

    elif escolha == "3":
        texto = input("Escreva sua mensagem anônima: ").strip()
        remetente = "Anônimo"

    else:
        print("❌ Opção inválida.")
        return

    print("""
    1. 📤 Enviar agora
    2. 📝 Salvar no rascunho (fila)
    """)
    destino = input("Escolha: ").strip()

    mensagem = {
        "remetente": remetente,
        "destinatario": destinatario,
        "texto": texto
    }

    if destino == "1":
        # Perguntar se quer enviar real via SMTP (se dest parecer e-mail)
        enviar_real = False
        if "@" in destinatario:
            resp = input("Deseja enviar também por e-mail real (SMTP)? (s/n): ").strip().lower()
            enviar_real = resp == "s"
        if enviar_real:
            if smtp_cache["email"] is None:
                smtp_cache["email"] = input("Digite seu e-mail (p.ex. seu@gmail.com): ").strip()
                smtp_cache["senha"] = input("Digite sua senha de app (App Password): ").strip()
                smtp_cache["server"] = "smtp.gmail.com"
            entregar_mensagem_obj(mensagem, enviar_real=True, remetente_envio_email=smtp_cache["email"], senha_envio=smtp_cache["senha"])
        else:
            entregar_mensagem_obj(mensagem)
    else:
        fila_mensagens.enqueue(mensagem)
        print("💾 Mensagem salva no rascunho (fila).")

def menu_mensagens(usuario_logado):
    while True:
        print("\n--- 💌 MENU DE MENSAGENS ---")
        print("""
        1. ✉️ Enviar mensagem
        2. 📬 Entregar próxima mensagem da fila (rascunhos)
        3. 📥 Listar recebidas
        4. 📤 Listar enviadas
        5. 🔍 Pesquisar mensagens
        6. 📜 Histórico geral
        7. ↶ Desfazer última entrega (undo)
        0. 🔙 Voltar
        """)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            enviar_mensagem_menu(usuario_logado)
        elif opcao == "2":
            # pergunta se envio real
            enviar_real = False
            if not fila_mensagens.isEmpty():
                prox = fila_mensagens.peek()
                if prox and "@" in prox["destinatario"]:
                    resp = input("Deseja tentar enviar por SMTP também? (s/n): ").strip().lower()
                    enviar_real = resp == "s"
                if enviar_real and smtp_cache["email"] is None:
                    smtp_cache["email"] = input("Digite seu e-mail (p.ex. seu@gmail.com): ").strip()
                    smtp_cache["senha"] = input("Digite sua senha de app (App Password): ").strip()
            entregar_proxima_da_fila(enviar_real=enviar_real)
        elif opcao == "3":
            listar_recebidas(input("Listar recebidas de quem? ").strip())
        elif opcao == "4":
            listar_enviadas(input("Listar enviadas por quem? ").strip())
        elif opcao == "5":
            pesquisar_mensagens(input("Pesquisar por nome: ").strip())
        elif opcao == "6":
            mostrar_historico()
        elif opcao == "7":
            desfazer_ultima_entrega()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")

def menu_extras():
    while True:
        print("\n--- 🏆 EXTRAS ---")
        print("""
        1. 💞 Ranking dos mais românticos
        2. 📋 Listar usuários cadastrados (in-order na árvore)
        3. 📈 Mostrar conexões (grafo)
        0. 🔙 Voltar
        """)
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            ranking_romanticos()
        elif opcao == "2":
            lista = usuarios.listar_in_order()
            print("\n👥 Usuários cadastrados (ordem alfabética):")
            for nome in lista:
                print("-", nome)
        elif opcao == "3":
            print("\n🔗 Conexões remetente -> destinatário (contadores):")
            for r, mapa in grafo.adj.items():
                print(f"{r}:")
                for d, c in mapa.items():
                    print(f"   -> {d} (x{c})")
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")

def menu_principal(usuario_logado):
    while True:
        print("\n" + "═" * 60)
        print(f"💗 C O R R E I O   D O   A M O R  (user: {usuario_logado}) 💗".center(60))
        print("═" * 60)
        print("""
        1. 💗 Mensagens
        2. 👥 Perfil / Conta
        3. 🏆 Extras
        0. ❌ Sair
        """)
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            menu_mensagens(usuario_logado)
        elif opcao == "2":
            print(f"\nPerfil: {usuario_logado}")
            resp = input("Deseja ver quantas mensagens recebeu? (s/n): ").strip().lower()
            if resp == "s":
                listar_recebidas(usuario_logado)
        elif opcao == "3":
            menu_extras()
        elif opcao == "0":
            print("Saindo... obrigada por espalhar amor 💘")
            break
        else:
            print("❌ Opção inválida.")

# -----------------------------
# Entrypoint
# -----------------------------
if __name__ == "__main__":
    apresentacao()

    # Loop inicial: cadastro obrigatório / login
    while True:
        print("1. Login")
        print("2. Cadastro")
        print("0. Sair")
        escolha = input("Escolha: ").strip()
        if escolha == "2":
            cadastrar_usuario_interativo()
        elif escolha == "1":
            usuario = login_interativo()
            if usuario:
                menu_principal(usuario)
                break
        elif escolha == "0":
            print("Até logo.")
            break
        else:
            print("Opção inválida.")