##Imports
import math

##Variáveis
p1 = float
p2 = float
smaug = float
a1 = float
a2 = float
notaDesconhecida = float
media = float


##Funções
def mediaCalculo(p1, p2, smaug, a1, a2):
    p1 = float(input("Qual foi sua nota na P1?"))
    p2 = float(input("Qual foi sua nota na P2?"))
    smaug = float(input("Qual foi sua nota de apresentação?"))
    a1 = float(input("Qual foi sua nota de Atividades 1?"))
    a2 = float(input("Qual foi sua nota de Atividades 2?"))
    media = float(0.15 * a1 + 0.25 * p1 + 0.2 * a2 + 0.3 * p2 + 0.1 * smaug)
    mediaRedonda = "{:.2f}".format(media)
    print("Sua média de Cálculo é: " + str(mediaRedonda))

def iniciarPrograma():
    print("Olá Aluno!\nQuer saber a média de qual disciplina?")
    x = int(input("1 - Cálculo\n"
                  "2 - Português\n"
                  "3 - Programação\n"
                  "4 - Redes\n"
                  "5 - Sistemas Operacionais\n"
                  "6 - Tecnologia da informação\n"
                  "7 - Ajuda/Como funciona\n"
                  "8 - Sair\n"))
    if x == 1:
        mediaCalculo(p1, p2, smaug, a1, a2)
    elif x == 2 or 3 or 4 or 5 or 6:
        print("Não temos a média dessas matérias")
        iniciarPrograma()
    elif x == 7:
        print("Insira ajuda aqui... (WIP)")
        iniciarPrograma()
    elif x == 8:
        exit()
    else:
        print("Número inválido, tente novamente")
        iniciarPrograma()


##Código
iniciarPrograma()
