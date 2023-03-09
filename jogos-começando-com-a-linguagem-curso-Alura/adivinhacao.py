#tenho q importar o random se quiser usar
import random

#definir o nome da função
def jogar():

    #apresentação
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    
    #variavel do numero secreto - importo o ramdom e uso a propriedade .randrange = 1 a 100
    numero_secreto = random.randrange(1,101)
    #variavel do total de tentativas
    total_de_tentativas = 0
    #pontos maximos
    pontos = 1000

    #configurando dificuldades 
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    #input = aonde o usuario digita - Definir o input com int, pq eh string
    nivel = int(input("Defina o nível: "))

    #colocando valor da variavel em total de tentativas de acordo com o nivel
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    #se n for nenhuma das opções em cima
    else:
        total_de_tentativas = 5
        
    #config das tentativas
    #1 a 10 tentativas = para cada rodada terá 10 tentativas 
    for rodada in range(1, total_de_tentativas + 1):
    #String interpolation = {} = mostro para meu codigo aonde que quero que minha "fomat" vá parar na minha string = Vai seguir a ordem da format
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        #chute - transformar me variavel 
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        #avisar quais numeros q a pessoa tem q jogar
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        #criando variaveis do CHUTE
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        #se - acertou o numero - da um break e fala qauntos potnso fez = PONTOS TT - OQ EU CHUTEI = PONTOS Q FZ
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        
        #se a pessoa n acertou mas se o numero eh maior ou menor
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                
            #chute
            pontos_perdidos = abs(numero_secreto - chute) #40-20 = 20pontos - uso o abs para arredondar
            #pontuação atual = pontos perdidos de acordo com o chute
            pontos = pontos - pontos_perdidos

    #fim - se executou td certinho
    print("Fim do jogo")
    
#definir o arquivo/class jogos como principal, msm se eu iniciar outro arquivo ele vai começar por esse
if(__name__ == "__main__"):
    jogar()
    