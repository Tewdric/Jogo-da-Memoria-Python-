from time import sleep
def limpar ():
      print("\n"*20)
def verifica(m,mp):
    cont = 0
    for i in range (0,5):
        for c in range (0,5):
            if m[i][c] == mp:
                cont += 1
    if (cont > 2 ):
        return True

# INICIANDO O GAME

print("\033[1:31m=-=-=-=-= INSTRUÇÕES =-=-=-=-=\033[1:31m")
print("")
print("\033[1:33mSEJA HONESTO, NÃO TIRE PRINT!\033[1:33m")
print("")
print("\033[1:34mPARA CADA 3 ACERTOS CONSECUTIVOS, GANHE UMA VIDA,\n"
      "E OPORTUNIDADE DE OLHAR A TABELA POR MAIS DEZ SEGUNDOS! \033[1:34m")
print("")
print("\033[1:34mPARA CADA ERRO, PERCA UMA VIDA!\033[1:34m")
print("")
print("\033[1:34mVOCÊ COMEÇA COM 5 VIDAS! !\033[1:34m")
print("")


while True:
    iniciar = int(input("SE DESEJA INICIAR O JOGO DIGITE 1 | SE DESEJA SAIR DIGITE 0: "))
    print("")

    acerto = 0
    erro = 0
    rodada = 0
    vida = 5
    acerto_consecutivo = 0

    if iniciar == 1:
        print("O jogo será iniciado em 3 segundos ☺")
        for cont in range (3,0,-1):
            print(cont)
            sleep(1)
        print("")
        print("\033[1:33mVocê tem 10 SEGUNDOS para memorizar o tabuleiro! ")
        print("")

        # VARIÁVEIS CONTADORAS
        rodada = 0
        acerto = 0
        erro = 0
        vida = 5
        acerto_consecutivo = 0

        valores = []
        posicoes = []

        # TABELA ALEATÓRIA
        import random
        #até o \u2655 tem 84 icones
        aleatoria = [" \u00a9 ", " \u00a9 ", " \u2BC1 ", " \u2BC1 ", " \u2BC0 ", " \u2BC0 ",
                     " \u3007 ", " \u3007 ", " \u2727 ", " \u2727 ", " \u20DF ", " \u20DF ",  " \u2394 ",
                     " \u2394 ", " \u23F9 ", " \u23F9 "," \u2661  "," \u2661 "," \u2102 "," \u2102 ",
                     1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,"@","@"," # "," # "," $ "," $ "," & "," & "," + "," + "," { ",
                     " { "," } "," } ", " ? ", " ? ", " § ", "§"," A ", " A " ," E ", " E", " I ", " I ", " O ", " O ", " U ", " U ",
                     " % "," % ", " ¬ ", " ¬ ", " £ ", " £ "," ¢ ", " ¢ ", " ~ ", " ~ ", " \u2667 ", " \u2667 ",
                     " \u2654 ", " \u2654 ", " \u2655 ", " \u2655 "," \u2206 "," \u2206 ", " \u2207 "," \u2207",
                     " \u03B1 ", " \u03B1 ", " \u2135 ", " \u2135 ", " \u2132 ", " \u2132 ", " \u2104 ", " \u2104 ",
                     " \u2101 "," \u2101 ", " \u2763 ", " \u2763 "]

        random.shuffle(aleatoria)

        for x in range(0, 100, 10):
            print(aleatoria[x], aleatoria[x + 1], aleatoria[x + 2], aleatoria[x + 3], aleatoria[x + 4],
                   aleatoria[x + 5], aleatoria[x +6], aleatoria[x + 7], aleatoria[x + 8], aleatoria[x + 9])
        print("")

        # TABELA DE CARTAS FECHADAS
        fechada = ["\u2662"] * 100
        for x in range(0, 100, 10):
                    (fechada[x], fechada[x + 1], fechada[x + 2], fechada[x + 3],
                          fechada[x + 4], fechada[x + 5],fechada[x +6], fechada[x + 7],
                          fechada[x + 8], fechada[x + 9])

        sleep(10)
        limpar()

        #INICIANDO O JOGO

        while acerto < 8:
            print("")
            print("\033[1:37mESCOLHA UMA DAS POSIÇÕES ABAIXO:\033[1:37m")

            posicao = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                       20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,32,33,34,35,36,37,38,39,40,
                        41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,
                       65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,
                       90,91,92,93,94,95,96,97,98,99]

            for y in range(0, 100, 10):
                print(posicao[y], posicao[y + 1], posicao[y + 2], posicao[y + 3], posicao[y + 4],
                      posicao[y + 5], posicao[y + 6], posicao[y + 7], posicao[y + 8], posicao[y + 9])
            print("")

            # ESCOLHENDO UMA CARTA
            while True:
                q = int(input("\033[1:37mESCOLHA UMA CARTA: \033[1:37m"))
                if q >= 0 and q <= 100:
                    print("Ok!")
                    break
                else:
                    print("\033[1:31mESCOLHA INVÁLIDA! ESCOLHA UMA DAS POISÇÕES ACIMA...\033[1:31m")

            # ESCOLHENDO OUTRA CARTA
            while True:
                q2 = int(input("\033[1:37mESCOLHA MAIS UMA CARTA: \033[1:37m"))
                if q2 >= 0 and q2 <= 100:
                    print("Ok!")
                    break
                else:
                    print("\033[1:37mESCOLHA INVÁLIDA! ESCOLHA UMA DAS POISÇÕES ACIMA...")

            if q == q2:
                print("\033[1:31mERRO! VC ESCOLHEU A MESMA POSIÇÃO NAS DUAS PEDIDAS... TENTE NOVAMENTE!")
                print("")
                print("\033[1:37mRODADAS:", rodada)
                print("")
                for y in range(0, 100, 10):
                    print(fechada[y], fechada[y + 1], fechada[y + 2], fechada[y + 3], fechada[y + 4], fechada[y + 5]
                          , fechada[y + 6], fechada[y + 7], fechada[y + 8], fechada[y + 9])

            elif aleatoria[q] == aleatoria[q2]:

                # ACERTOS-----------------

                if fechada[q] == 0 and fechada[q2] == 0:
                    print("\033[1:31mERRO! VC JÁ ESCOLHEU ESSES VALORES... TENTE NOVAMENTE!")
                    print("")
                    print("\033[1:37mRODADAS:", rodada)
                    print("")
                    for y in range(0, 100, 10):
                        print(fechada[y], fechada[y + 1], fechada[y + 2], fechada[y + 3], fechada[y + 4], fechada[y + 5]
                              , fechada[y + 6], fechada[y + 7], fechada[y + 8], fechada[y + 9])
                else:
                    print("")
                    print("\033[1:33mVOCÊ ACERTOU!!!")
                    print("")

                    acerto += 1
                    rodada += 1



                    if acerto == 3:
                       vida += 1
                       acerto = 0*3
                       print(f"\033[1:33mVocê ganhou mais uma vida, agora você tem {vida} vidas! ☻")
                       print("\033[1:33mAlém da vida, pode olhar a tabela por 10 segundos. boa sorte ☻")
                       for x in range(0, 100, 10):
                           print(aleatoria[x], aleatoria[x + 1], aleatoria[x + 2], aleatoria[x + 3], aleatoria[x + 4],
                                 aleatoria[x + 5], aleatoria[x + 6], aleatoria[x + 7], aleatoria[x + 8],
                                 aleatoria[x + 9])
                       sleep(10)
                       print("")

                    print(f"Seus pontos atuais {acerto}. ")
                    print("")
                    posicoes.append(q)
                    posicoes.append(q2)
                    valores.append(aleatoria[q])

                    print("- Posições já escolhidas corretamente:", posicoes)
                    print("- Valores já escolhidos corretamente:", valores)
                    print("")
                    print("RODADAS:", rodada)
                    print("")

                    fechada[q] = 0
                    fechada[q2] = 0
                    for y in range(0, 100, 10):
                        print(fechada[y], fechada[y + 1], fechada[y + 2], fechada[y + 3], fechada[y + 4], fechada[y + 5]
                              , fechada[y + 6], fechada[y + 7], fechada[y + 8], fechada[y + 9])

            # ERROS ---------------------

            else:
                print("")
                print("\033[1:31mVOCÊ ERROU!!!")
                print("")

                erro += 1
                rodada += 1
                vida -= 1

                if erro == 1 and acerto > 1:
                    acerto -= 1
                else:
                    acerto = 0

                print("- Posições já escolhidas corretamente:", posicoes)
                print("-Valores já escolhidos corretamente:", valores)
                print("")
                print("RODADAS:", rodada)
                print(f"Você tem agora {vida} vidas. ")
                print(" ")
                print(f"Seus pontos atuais {acerto}. ")
                print("")
                for y in range(0, 100, 10):
                    print(fechada[y], fechada[y + 1], fechada[y + 2], fechada[y + 3], fechada[y + 4], fechada[y + 5]
                          , fechada[y + 6], fechada[y + 7], fechada[y + 8], fechada[y + 9])

        # FIM DO JOGO -----------------
            if vida == 0:
                print("")
                print("\033[0:31m-------------- GAME OVER --------------")
                print("")
                print("SEUS ACERTOS:", acerto)
                print("SEUS ERROS:", erro)
                print("TENTATIVAS:", rodada)
                print("")
                print("SUA TABELA...")
                for x in range(0, 100, 10):
                    print(aleatoria[x], aleatoria[x + 1], aleatoria[x + 2], aleatoria[x + 3], aleatoria[x + 4],
                          aleatoria[x + 5], aleatoria[x + 6], aleatoria[x + 7], aleatoria[x + 8], aleatoria[x + 9])
                print("")
                print("Fechando o programa...")
                break

        print("")
        print("\033[36m--- PARABÉNS, VOCE FINALIZOU O GAME ---")
        print("")






    elif iniciar == 0:
        print("Fechando o programa...")
        break
    else:
        print("Digito incorreto! Digite 1 para iniciar OU 0 para sair...")