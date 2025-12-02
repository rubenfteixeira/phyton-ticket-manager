from datetime import datetime
import sys

contRep = 0
contEnt = 0
arquivo = []
arrayBalcao = [0, 0, 0, 0]
array = []
n = 0
balcao = 0


#Função para escolher entre reparação, entrega ou aceder à gestão.
def opcoes():
  global contRep, contEnt, n, data1

  while True:
    verificarOpção()

    if n == 1:
      contRep += 1
      arquivo.append("Reparação")
      arquivo.append(contRep)
      data1 = datetime.now()
      data1 = data1.strftime("%d/%m/%Y %H:%M:%S")
      arquivo.append(data1)

      print("Reparação \nSenha", contRep, data1)
      reparação(data1)

    elif n == 2:
      contEnt += 1
      arquivo.append("Entrega")
      arquivo.append(contEnt)
      data1 = datetime.now()
      data1 = data1.strftime("%d/%m/%Y %H:%M:%S")
      arquivo.append(data1)

      print("Entrega \nSenha:", contEnt, data1)
      entrega(data1)

    elif n == 3:

      while True:

        try:
          código = int(input("Insira o código:\n"))
          if código == 2222:
            print("Bem vindo ao menu de gestão!")
            gestão()
            break
          else:
            print("Código errado")
            opcoes()
        except ValueError:
          print("Código errado")
          opcoes()


#Função para preencher informações relacionadas à reparação.
def reparação(data1):
  global data, array

  while True:
    verificarBalcão()
    if balcao == 4:
      print("Não são feitas reparações no balcão 4")
    elif balcao == 1 or balcao == 2 or balcao == 3:
      data2 = datetime.now()
      data2 = data2.strftime("%d/%m/%Y %H:%M:%S")
      arquivo.append(data2)
      verificarNome()
      produto = input("Qual o produto? \n")
      anomalia = input("Anomalia identificada \n")
      verificarValor()
      obs = input("Outras observações \n")
      print("Pedido Finalizado com Sucesso!")
      arquivo.append(nome)
      arquivo.append(balcao)
      arquivo.append(produto)
      arquivo.append(anomalia)
      arquivo.append(custo)
      arquivo.append(obs)

      hora1 = datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")
      hora2 = datetime.strptime(data2, "%d/%m/%Y %H:%M:%S")
      espera = (hora2 - hora1)

      arquivo.append(str(espera))

      with open("db.txt", 'a') as f:
        f.write(str(arquivo))
        f.write("\n")

      break
    else:
      print("Opção inválida!")


#Função para preencher informações relacionadas à entrega.
def entrega(data1):

  global data, array

  while True:

    verificarBalcão()
    if balcao == 1 or balcao == 2 or balcao == 3 or balcao == 4:
      data2 = datetime.now()
      data2 = data2.strftime("%d/%m/%Y %H:%M:%S")
      arquivo.append(data2)
      verificarNome()
      verificarValor()
      obs = input("Outras observações \n")
      print("Entrega realizada com sucesso!")
      arquivo.append(nome)
      arquivo.append(balcao)
      arquivo.append(custo)
      arquivo.append(obs)

      hora1 = datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")
      hora2 = datetime.strptime(data2, "%d/%m/%Y %H:%M:%S")
      espera = (hora2 - hora1)

      arquivo.append(str(espera))

      with open("db.txt", 'a') as f:
        f.write(str(arquivo))
        f.write("\n")
      break
    else:
      print("Opção inválida!")


#Função para aceder a opções relacionadas à gestão.
def gestão():
  while True:
    print("1- Tickets atendidos por data")
    print("2- Média de espera por data")
    print("3- Balcões por data")
    print("4- Receitas por data")
    print("5- Mapa total de tickets")
    print("6- Encerrar Programa")
    print("7- Sair")

    verificarOpção2()

    if x == 1 or x == 2 or x == 3 or x == 4:
      while True:
        data = input("Digite a data no formato dd/mm/aaaa \n")
        if len(data) == 10 and data[2] == "/" and data[5] == "/":
          if x == 1:
            dataTicket(data)
            break
          elif x == 2:
            mediaEspera(data)
            break
          elif x == 3:
            balcão(data)
            break
          elif x == 4:
            receitas(data)
            break
        else:
          print("Formato ou valor inválido")
    elif x == 5:
      mapaTickets()
    elif x == 6:
      sys.exit()
    elif x == 7:
      opcoes()
    else:
      print("Opção inválida")


#Função de gestão de tickets na respectiva data.
def dataTicket(data):

  with open("db.txt", "r") as arquivo:
    for linha in arquivo:
      array = linha.split(',')
      if data in array[2]:
        print(linha)


#Função de gestão para calcular a média de espera por data.
def mediaEspera(data):
  total = 0
  contador = 0
  num = []
  horas = 0
  minutos = 0
  segundos = 0
  hr = 0
  min = 0
  seg = 0

  with open("db.txt", "r") as arquivo:
    for linha in arquivo:
      array = linha.split(',')
      if data in array[2]:
        num = array[-1].split(':')
        horas = int(num[0][2])
        minutos = int(num[1])
        segundos = (int(num[2][0]) * 10) + (int(num[2][1]))
        total += horas * 3600
        total += minutos * 60
        total += segundos
        contador += 1

  if contador > 0:
    media = total / contador
    hr = media // 3600
    media = media - (horas * 3600)
    min = media // 60
    seg = media - (min * 60)
    print("horas:", hr, "minutos:", min, "segundos:", seg)
  else:
    print("Não há tickets nessa data")


#Função de gestão de atendimentos por balcão na respectiva data.
def balcão(data):

  with open("db.txt", "r") as arquivo:
    for linha in arquivo:
      array = linha.split(',')
      if data in array[2]:
        if array[5] == " 1":
          arrayBalcao[0] += 1
        elif array[5] == " 2":
          arrayBalcao[1] += 1
        elif array[5] == " 3":
          arrayBalcao[2] += 1
        elif array[5] == " 4":
          arrayBalcao[3] += 1

  if arrayBalcao[0] < 1 and arrayBalcao[1] < 1 and arrayBalcao[
      2] < 1 and arrayBalcao[3] < 1:
    print("Não teve nenhum atendimento nessa data!")
  else:
    print("balcão 1:", arrayBalcao[0])
    print("balcão 2:", arrayBalcao[1])
    print("balcão 3:", arrayBalcao[2])
    print("balcão 4:", arrayBalcao[3])


#Função de gestão das receitas na respectiva data.
def receitas(data):
  contador = 0
  totalReceitas = 0
  with open("db.txt", "r") as arquivo:
    for linha in arquivo:
      array = linha.split(',')
      if data in array[2]:
        valor = float(array[-3])
        totalReceitas += valor
        contador += 1
  if contador > 0:
    print("Total de receitas", totalReceitas, "€")
  else:
    print("Não há receitas nessa data")


#Função de gestão de informações dos tickets.
def mapaTickets():
  with open("db.txt", "r") as arquivo:
    for linha in arquivo:
      print(linha)


#Função para abrir/fechar o sistema ás horas selecionadas.
def abertoFechado():

  agora = datetime.now()
  if agora.hour >= 0 and agora.hour < 23:
    opcoes()
  else:
    print("O sistema não está disponível")
    print("Tente novamente entre as 8:00 e 23:00")


#Função para perguntar e verificar se o input é com letras. Caso não seja, repetir.
def verificarNome():
  global nome
  while True:
    nome = input("Qual é o nome do proprietário? \n")
    if nome.isalpha():
      break
    else:
      print("Por favor, digite apenas letras para o nome.")


#Função para perguntar e verificar se o input é com números. Caso não seja, repetir.
def verificarValor():
  global custo
  while True:
    try:
      custo = float(input("Qual o custo inicial? \n"))
      break
    except ValueError:
      print("Valor inválido")


#Função para escolher a opcção e verificar se é com números. Caso não seja, repetir.
def verificarOpção():
  global n
  while True:
    try:
      n = int(
          input(
              "Digite a opção desejada: \n 1- Reparação \n 2- Entrega \n 3- Gestão \n"
          ))
      break
    except ValueError:
      print("Valor errado")


#Função para perguntar o balcão e verificar se é com números. Caso não seja, repetir.
def verificarBalcão():
  global balcao
  while True:
    try:
      balcao = int(input("Qual o balcão?"))
      break
    except ValueError:
      print("Valor Errado")

#Função para escolher a opcção e verificar se é com números. Caso não seja, repetir.
def verificarOpção2():
  global x
  while True:
    try:
      x = int(input("Digite a opção desejada: "))
      break
    except ValueError:
      print("Valor errado")


abertoFechado()
