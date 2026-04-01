import os
import time
os.system("cls")

total_pag = 0
ACRESCIMO = 8
DESCONTO = 15
lista = []
total = 0
sair = False

while True:
    Vida_Plena = {
        1: ("Hemograma Completo", 2500.00),
        2: ("Raio-X", 2000.00),
        3: ("Ultrassonografia", 1800.00),
        4: ("Eletrocardiograma", 1000.00),
        5: ("Tomografia", 4000.00),
        6: ("Ressonância Magnética",900.00),
        7: ("Exame de próstrata", 800.00),
    }


    print("\n-----------HOSPITAL VIDA PLENA -----------")
    for codigo, (nome, preco) in Vida_Plena.items():
        print(f"{codigo} - {nome} | R${preco:.2f}")

    print("Digite 0 caso não queria mais adicionar exames")

    codigo = int(input("\nDigite o código do exame desejado: "))
    
    if codigo in Vida_Plena :
        nome, preco = Vida_Plena[codigo]
        total += preco
        print(f"{nome} adicionado!")
        time.sleep(2)
        os.system("cls")
        exames = {
            "nome": nome,
            "preco": preco
}
        lista.append(exames)
        opcao = input("Deseja agendar mais exames ? Digite S ou N: ").lower()
        if opcao != "s":
            break
                
    elif codigo == 0:
            print("Indo para pagina de pagamento")
            time.sleep(2)
            os.system("cls")
            break
    
    else:
        print("Código inválido!, Digite novamente com as OPÇÕES numeradas acima")
        time.sleep(2)
        os.system("cls")
        continue

if not lista:
    print("O senhor não escolheu nenhum exame")
    print("Não exite nenhum valor para pagamento")
    exit()
    
while True:
    print("---Selecione o Plano Hospitalar Desejado---")
    pagamento = input("""1 - Convênio | Desconto de 15% do valor total
2 - Particular | Sem desconto ou acréscimo
3 - Cartão de Crédito | Acréscimo de 8% do valor total
""")

    match pagamento:
        case "1":
            total_pag = total * (1 - DESCONTO / 100)
            break
        case "2":
            total_pag = total
            break
        case "3":
            total_pag += total * (1 + ACRESCIMO / 100)
            break
        case _: 
            os.system("cls")
            print("Opão Inválida")
            print("Tente Novamente")
            time.sleep(2)
            os.system("cls")
            continue
    
print("\n----- VALOR A SER COBRADO-----")

for i, exame in enumerate(lista, start=1):
    print(f"{i} - {exame['nome']} = R${exame['preco']:.2f}")
    print("-" * 20)

print(f"\nValor Total: R${total_pag:.2f}")