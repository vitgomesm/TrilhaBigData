idd1 = 16
idd2 = 17
idd3 = 18

if idd1  <= 16:
    print('Não é permitido a entrada, pois você é menor de idade')

elif idd1 >= 18 :
    print('Tá liberado a sua entrada')

if idd2  <= 16:
    print('Não é permitido a entrada, pois você é menor de idade')
elif idd2==17 :
    print('Não é permitido a entrada, porém só falta 1 ano para ser permitido')
elif idd2 >= 18 :
   print('Tá liberado a sua entrada')

if idd3  <= 16:
    print('Não é permitido a entrada, pois você é menor de idade')
elif idd3 ==17 :
    print('Não é permitido a entrada, porém só falta 1 ano para ser permitido')
elif idd3 >= 18 :
    print('Tá liberado a sua entrada')   


if idd1  <= 16 or idd1 >=18:
    print('Não é permitido a entrada, pois você é menor de idade') 
else : 
    print('Tá liberado a sua entrada')   

if idd2 >=18 :
    print('Tá liberado a sua entrada') 
else : 
    print('Não é permitido a entrada, pois você é menor de idade') 

if idd3  <= 16 and idd3 >=18:
    print('Não é permitido a entrada, pois você é menor de idade') 
else : 
  print('Tá liberado a sua entrada')
