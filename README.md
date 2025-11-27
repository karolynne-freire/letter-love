# 💌 Letter-Love – O Correio do Amor com Estrutura de Dados

O Letter-Love é um sistema romântico e interativo desenvolvido como projeto da disciplina de Estrutura de Dados, utilizando filas, listas e dicionários para simular um correio digital onde usuários podem enviar declarações, bilhetes e mensagens especiais.

Aqui, o amor acontece na lógica, nos ponteiros do coração e na fila de mensagens! 💖

---

## 🔍 Sobre o Projeto

O **Letter-Love** simula a troca de mensagens.
Remetentes pode interagir enviando cartas personalizadas ou escolhendo mensagens prontas, enquanto o sistema gerencia tudo utilizando estruturas de dados clássicas.

O projeto tem como objetivos principais:

* Exercitar filas (FIFO), dicionários e listas
* Desenvolver lógica de organização e processamento
* Criar menus interativos e navegação via terminal
* Simular um fluxo real de envio, rascunho e entrega de mensagens

---

## 💡 Como o Sistema Funciona

### 📝 1. Cadastro

O usuário pode se cadastrar.

### 💌 2. Criação de Mensagem

Ao escrever uma carta, o usuário pode:

* digitar uma mensagem personalizada
* **ou escolher um modelo pronto** salvo no dicionário de cartas

A mensagem criada entra na **fila de envio**, funcionando também como **rascunho**.

### 📬 3. Entrega

Quando o sistema entrega a próxima mensagem:

* a carta é retirada da fila (FIFO)
* é adicionada à caixa de entrada do destinatário
* entra para o **histórico geral**

### 🔍 4. Consultas

O usuário pode consultar:

* mensagens enviadas
* mensagens recebidas
* histórico geral
* mensagens relacionadas a um nome específico

### 🏆 5. Ranking dos Mais Românticos

O sistema calcula automaticamente quem mais enviou mensagens.

---

## 🛠️ Tecnologias e Conceitos Utilizados

* Python 3
* Estruturas de Dados (fila, lista, dicionário)
* Classe `Queue` implementada manualmente
* Modularização de funções
* Loops e estruturas condicionais
* Códigos ANSI para cores e estilo
* Animações com `time.sleep()`
* Menus interativos no terminal

---
### Pré-requisitos

* Python 3.8 ou superior
---

### ▶️ Como Executar o Projeto

#### 1. Clone o repositório
```bash
git clone https://github.com/karolynne-freire/letter-love.git
```
#### 2. Acesse a pasta do projeto
```bash
cd letter-love
```
#### 3. Entre na subpasta back
```bash
cd back
```
#### 4. Execute o jogo principal
```bash
python main.py
```
Obs: No Windows, use python ou py, dependendo da sua configuração.


### 👥 Equipe de Desenvolvimento

Projeto desenvolvido por:

* **Karolynne Freire**
* **Fábio Cunha**
* **Cayo Roberto**

---

### 🚧 Status do Projeto

🔧 Em desenvolvimento ativo.
Novas funcionalidades continuam sendo adicionadas ao sistema.

---

### 📜 Licença

Projeto acadêmico criado para fins educacionais na disciplina de Estrutura de Dados.
Livre para estudo, adaptação e expansão.
Espalhe mensagens, espalhe amor… em Python! 💘

---
