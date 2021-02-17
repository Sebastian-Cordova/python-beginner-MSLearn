#if staments
tengo_hambre = True
if tengo_hambre :
    print("Sebastian tiene hambre")

#if & else staments
if tengo_hambre :
    print("Deberias prepararte una hamburguesa :)")
else :
    print("No es necesario que comas algo, puedes esperar hasta mañana")

#if, else & elif staments
billetera = 10
if billetera < 10:
    print("Debes ahorrar más dinero para almorzar algo mas decente")
elif billetera == 10:
    print("Te alcanza para comprarte un buen menu") 
else: 
    print("Puedes pedir mas de un plato")

#extended version
juanWallet = 170
theShow = 200
rosatelSurprise = 150
novia1 = 'Caroline'
novia2 = 'Romina'
if juanWallet >= theShow + rosatelSurprise:
    print(f"Juan puede satisfacer tanto a {novia1} como a {novia2}")
elif juanWallet>= theShow:
    print(f"Juan puede asistir a The Show con {novia1}")
elif juanWallet>= rosatelSurprise:
    print(f"Juan le puede mandar un arreglo de Rosatel a {novia2}")
else:
    print("Juan no tiene mucho dinero, debe ponerse a trabajar")
    
#Nested if code blocks
first_value = True
second_value = 69
if first_value:
    if second_value == 69:
        print('Got here!')

