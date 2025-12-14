
# 💌 Letter Love - Sistema Romântico em Python

O **Letter Love** é um sistema romântico desenvolvido como trabalho prático da disciplina de Estrutura de Dados.

A ideia mistura lógica, algoritmos e um toque de paixão:
um *Correio do Amor Digital* onde usuários podem enviar:

* 💖 Mensagens personalizadas
* 💝 Mensagens prontas
* 👤 Bilhetes anônimos

Tudo isso utilizando estruturas de dados como **árvore binária**, **fila**, **pilha**, **listas**, **dicionários** e **grafos** — como se Cupido tivesse aprendido Python. 🏹✨

---

## ✨ Funcionalidades

### 👤 Cadastro e Login

* Sistema de usuários estruturado com **Árvore Binária de Busca (BST)**
* Inserção, busca e listagem ordenada dos usuários

### 💌 Envio de Mensagens

O usuário pode escolher entre:

* ✍️ Mensagem personalizada
* 💝 Modelo pronto
* 🕶️ Mensagem anônima

E também decidir:

* 📤 Enviar imediatamente
* 📝 Salvar na fila de rascunhos (Queue – FIFO)

### 📧 Envio por E-mail (SMTP) - em desenvolvimento

* Caso o destinatário seja um e-mail válido
* Envio real usando SMTP (Gmail)
* Opcional, escolhido pelo usuário

### 📥 Caixa de Entrada

* Cada usuário possui uma lista própria de mensagens recebidas

### 🔙 Desfazer Última Entrega (Undo)

* Implementado com **Stack (LIFO)**
* Um verdadeiro *voltar no tempo do amor* 💔➡️💘

### 🕸️ Grafo de Conexões Amorosas

* Cada mensagem enviada cria uma aresta entre remetente → destinatário
* Mostra as relações amorosas ou de amizade 👀


### 🏆 Ranking dos Românticos

* Conta quantas mensagens cada usuário enviou
* Mostra os maiores “cupidos” do sistema

---

## 🧠 Estruturas de Dados Utilizadas

O sistema inteiro foi construído com base em estruturas clássicas estudadas na disciplina.

| Estrutura                       | Conceito                    | Aplicação                                 |
| ------------------------------- | --------------------------- | ----------------------------------------- |
| **Queue (Fila)**                | FIFO                        | Rascunhos de mensagens que aguardam envio |
| **Stack (Pilha)**               | LIFO                        | Undo das últimas mensagens enviadas       |
| **Árvore Binária (BST)**        | Busca, inserção e ordenação | Cadastro e listagem de usuários           |
| **Grafo (Lista de Adjacência)** | Relações entre vértices     | Conexões remetente → destinatário         |
| **Listas Simples**              | Estrutura linear            | Caixa de entrada e histórico              |
| **Dicionário (Hash Map)**       | Chave → valor               | Armazenamento das mensagens prontas       |

---

### 📚 Dicionário de Mensagens Prontas

Além das estruturas principais, o sistema usa um **dicionário** para armazenar frases românticas prontas:

```python
mensagens_prontas = {
    1: "Você ilumina meus dias de um jeito especial.",
    2: "Mesmo longe, penso em você com carinho.",
    3: "Queria que soubesse o quanto admiro você."
}
```

Assim, basta escolher o número da mensagem para usá-la instantaneamente.

---

## 🌸 Como Executar

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/karolynne-freire/letter-love
```

### 2️⃣ Acessar a pasta do projeto

```bash
cd letter-love
```

### 3️⃣ Abrir no editor de sua preferência

Exemplos:

* VS Code: `code .`
* PyCharm: abrir a pasta pelo menu "Open"

### 4️⃣ Ter o **Python 3** instalado

Certifique-se de que o comando abaixo funciona:

```bash
python --version
```

### 5️⃣ Executar o sistema

````bash
python main.py
```bash
python main.py
````

### (Em desenvolvimento) Envio de e-mails reais

* Ter uma conta Gmail
* Gerar um **App Password** (senha de aplicativo)

---

## 🌼 Exemplos de Uso

* Criar usuários e enviar bilhetes fofos
* Deixar mensagens acumuladas na fila de rascunhos
* Mandar e-mail real para surpreender alguém
* Desfazer um envio precipitado 😅
* Ver quem é o maior romântico da turma
* Analisar o grafo das conexões amorosas ❤️🕸️

---

## 👥 Colaboradores

* **Karolynne Freire**
* **Fábio Cunha**
* **Cayo Roberto**

---

## ❤️ Mensagem da Equipe

*"Nem sempre o amor segue lógica…
mas no nosso caso, segue árvores, filas, pilhas e grafos."*
— Equipe Letter Love 💕

---

## 📜 Licença

Uso acadêmico — livre para consulta e aprimoramento.

---









