dirnome = str(input("Dígite o nome do cliente: "))
compras = int(input("Dígite o total de compras realizadas pelo cliente: "))
valor = float(input("Dígite o total gasto pelo cliente: "))
dias = int(input("Dígite há quantos dias o cliente não fez uma compra: "))
classificação = str(0) 
inatividade= str(0) 

#-------CALCULANDO A CLASSIFICAÇÃO-------
if compras > 50 and valor > 10000:
    classificação = "Diamante"
elif compras > 20 and compras < 50 and valor > 5000 and valor  < 10000:
    classificação = "ouro"
elif (compras > 10 and compras < 19) or (valor > 1000 and valor < 4999):
    classificação ="Prata"
elif ( compras > 1 and compras < 9) or (valor > 100 and valor < 999):
    classificação = "Bronze"
else:
    classificação = "Iniciante"

#-----CALCULANDO A INATIVIDADE------

if dias > 180:
    inatividade = "CLiente inativo, envie promoçoes urgentes!"
elif dias > 90 and  dias < 179:
    inatividade = "Cliente quase inativo, incentive novas compras!"
else:
    inatividade = "Cliente ativo, continue vom boas ofertas!"

print(f"Nome do cliente: {nome}\nTotal de compras: {compras}\nTotal gasto: {valor:.2f}\nClassificação: {classificação} \nStatus de inatividade: {inatividade}")
