# Sistema de Gestão de Atendimento em Python

Este projeto é um sistema de gestão de atendimento desenvolvido em **Python**, orientado para lojas de assistência técnica que realizam **reparações** e **entregas**.  
O programa funciona através da linha de comandos e permite registar pedidos, gerir tickets e gerar relatórios por data.

---

## 🚀 Funcionalidades Principais

### 🔧 Reparações
- Geração automática de senha
- Registo da hora de chegada e atendimento
- Nome do cliente
- Produto e anomalia
- Custo inicial
- Observações
- Cálculo automático do tempo de espera
- Guarda tudo no ficheiro `meu_arquivo.txt`

### 📦 Entregas
- Geração automática de senha  
- Registo de hora  
- Nome do cliente  
- Custo  
- Observações  
- Cálculo do tempo de espera  
- Registo no ficheiro `meu_arquivo.txt`

---

## 📊 Menu de Gestão

Através de um código de acesso (2222), é possível consultar:

1. **Tickets atendidos por data**  
2. **Média de espera por data**  
3. **Atendimentos por balcão**  
4. **Receitas totais por data**  
5. **Mapa completo de todos os tickets registados**  
6. **Encerrar o programa**  
7. **Voltar ao menu inicial**

---

## 📁 Estrutura de Dados

Todos os registos são guardados no ficheiro:

meu_arquivo.txt

yaml
Copiar código

Cada linha contém um ticket completo com:
- Tipo (Reparação/Entrega)
- Número da senha
- Data de chegada
- Data de atendimento
- Cliente
- Balcão
- Custo
- Observações
- Tempo de espera

---

## 🕒 Horário de Funcionamento

O sistema só permite utilização dentro do período definido:
- **Das 00:00 às 23:00**  
(Código facilmente ajustável no futuro.)

---

## ▶️ Como Executar

1. Certifica-te de que tens Python 3 instalado.
2. Corre o script principal:

```bash
python nome_do_ficheiro.py
O menu inicial será apresentado automaticamente.

🛠️ Tecnologias Utilizadas
Python 3

Biblioteca datetime

Manipulação de ficheiros .txt

Sistema de menus interactivo

📌 Objetivo do Projeto
Este sistema foi criado com fins académicos, focando-se no uso de:

Controlo de fluxo

Funções

Modularidade

Manipulação de ficheiros

Tratamento de exceções

Registo temporal de operações

📜 Licença
Este projeto é livre para uso académico e pessoal.

