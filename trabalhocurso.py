#Gabriel Mendes  Silva
#Turma: 2M
#O  código possibilita ao garçom  anotar o pedido, mostra o total a pagar e aplica descontos

#var
import random
opcao1 = 0
fechar = "b"
pix = "pix"
dinheiro = "dinheiro"
quantidade_espeto_boi = 0
preco_espeto_boi = 9
quantidade_porcao = 0
preco_porcao = 37
quantidade_espeto_coracao = 0
preco_espeto_coracao = 9
quantidade_espeto_porco = 0
preco_espeto_porco = 8
quantidade_espeto_frango = 0
preco_espeto_frango = 7
quantidade_refri = 0
preco_refri = 10
quantidade_suco = 0
preco_suco = 12


finalizar = "a"
carnes = []
nsorteado = 0
total = int

while finalizar != fechar:
    print("<><><><><><> [\OPÇÕES/] <><><><><><>")
    print("<><><><><><><> Comidas <><><><><><><>")
    print("<><><> 1- Espeto de boi          R$9,00<><><>")
    print("<><><> 2- Espeto de porco        R$8,00<><><>")
    print("<><><> 3- Espeto de frango       R$7,00<><><>")
    print("<><><> 4- Espeto de coração      R$9,00<><><>")
    print("<><><> 5- porção 3 carnes+fritas R$37,00<><><>")
    print
    print("<><><><><><><> Bebidas <><><><><><><>")
    print("<><><> 6- Refrigerante 1L     R$10,00<><><>")
    print("<><><> 7- Jarra de suco 750ml R$12,00<><><>")
    print
    print("<><><><><><> 8- Finalizar <><><><><><>")
    print
    opcao1 = int(input("O que o cliente deseja(digite o codigo do produto): "))
    match opcao1:
        case 1:
            quantidade_espeto_boi = quantidade_espeto_boi + 1
        case 2:
            quantidade_espeto_porco = quantidade_espeto_porco + 1
        case 3:
            quantidade_espeto_frango = quantidade_espeto_frango + 1
        case 4:
            quantidade_espeto_coracao = quantidade_espeto_coracao + 1
        case 5:
            quantidade_porcao = quantidade_porcao + 1
            print("<><><> Boi <><><>")
            print("<><><> Porco <><><>")
            print("<><><> Frango <><><>")
            print("<><><> Coração <><><>")
            for con in range(3):
                print
                carne = input("Qual opção de carne o cliente deseja: ")
                carnes.append(carne)
                print(carnes)
        case 6:
                            quantidade_refri = quantidade_refri+1
        case 7:
                            quantidade_suco = quantidade_suco+1
        case 8:
                    total = (quantidade_porcao * preco_porcao) + (quantidade_suco * preco_suco) + (quantidade_refri * preco_refri) + (quantidade_espeto_porco * preco_espeto_porco) + (quantidade_espeto_boi * preco_espeto_boi) + (quantidade_espeto_frango * preco_espeto_frango)
                    if total >= 150:
                        print ("Esse cliente atende aos requisito e ganhou 3% de desconto!!!")
                        porcentagem = (total * 3) / 100
                        print("Total",total,"reais")
                        total = total - porcentagem
                        print("Total a ser pago",total,"reais")
                        finalizar = fechar
                    elif total == total:
                        print ("Esse cliente não atende ao requisito e não ganhou os 3% de desconto!")
                        print("Total a ser pago", total, "reais")
                        finalizar = fechar
else:
    if total >= 150:
        x = random.randint(1, 10)
        nsorteado = input("digite um numero de 1 a 10: ")
        if nsorteado == x and total >=150:
            porcentagem = (total * 3) / 100
            print ("total R$",total)
            total = total - porcentagem
            print ("Total a ser pago R$",total)
            print(x)
    forma_de_pagamento = input("Qual a forma de pagamento:")
    if forma_de_pagamento == pix and total>=120 or dinheiro and total >=120:
        porcentagem = (total * 3) / 100
        total = total - porcentagem

print("<><><><><><><> COMIDAS <><><><><><><>")
print("<><><> 1- Espeto de boi          R$9,00<><><>")
print("<><><> 2- Espeto de porco        R$8,00<><><>")
print("<><><> 3- Espeto de frango       R$7,00<><><>")
print("<><><> 4- Espeto de coração      R$9,00<><><>")
print("<><><> 5- porção 3 carnes+fritas R$37,00<><><>")
print
print("<><><><><><><> BEBIDAS <><><><><><><>")
print("<><><> 1- Refrigerante 1L     R$10,00<><><>")
print("<><><> 2- Jarra de suco 750ml R$12,00<><><>")
print
print("Espeto de boi", "[",quantidade_espeto_boi,"]")
print("Espeto de porco", "[",quantidade_espeto_porco,"]")
print("Espeto de frango", "[",quantidade_espeto_frango,"]")
print("Espeto de coração", "[",quantidade_espeto_coracao,"]")
print("Porção de",carnes, "[",quantidade_porcao,"]")
print("Jarra de suco 750ml", "[",quantidade_suco,"]")
print("Refrigerante 1L", "[",quantidade_refri,"]")
print("Total a ser pago", total, "reais")