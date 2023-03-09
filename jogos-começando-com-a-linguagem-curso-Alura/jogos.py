#importo os arquivos - já quero anexar eles a esse codigo
import forca
import adivinhacao

#definir o nome da função
def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        #inicia o jogo, com a função jogar() = de acordo com o jg q eu escolhi = chamando uma função
        #nome da class + def + ()
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
#definir o arquivo/class jogos como principal, e define a função escolher_jogo como principal (def)
if(__name__ == "__main__"):
    escolhe_jogo()
