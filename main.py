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

# TESTE

if __name__ == "__main__":
    cadastrar_pessoa("remetente", "Ana")
    cadastrar_pessoa("destinatario", "João")
    cadastrar_pessoa("destinatario", "Maria")

    enviar_mensagem("Ana", "João", "Oi João 💖")
    enviar_mensagem("Ana", "Maria", "Olá Maria 💌")

    entregar_mensagem()
    entregar_mensagem()

    listar_recebidas("João")
    listar_recebidas("Maria")
    listar_enviadas("Ana")
    mostrar_historico()
