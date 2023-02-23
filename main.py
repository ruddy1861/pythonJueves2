#Condicionales con python
nivelAgua=int(input("Digita el nivel de agua: "))
if nivelAgua>=0 and nivelAgua<=250:
    print(f"El nivel de agua es muy bajo {nivelAgua} U")
elif nivelAgua>250 and nivelAgua<=450:
    print(f"El nivel de agua es optimo {nivelAgua} U")
elif nivelAgua>450:
    print(f"El nivel de agua es crictico, evacuen {nivelAgua} U")
else:
    print("revise el censor")
