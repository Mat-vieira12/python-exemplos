valor_uni = 12.5
quanti = int(input('Quantidade de camisa: '))
valor_total = valor_uni*quanti
if quanti <= 5: 
    valor_total=valor_total*0.97
else :
    if quanti <=10:
        valor_total=valor_total*0.95
    else: 
        valor_total=valor_total*93
print(f'Valor total: R$ {valor_total:.01f}')