
ListaPrimos = []
ListaNumeros = []
contadorPrimos = 0
contadorMCD = 0
repeticion = 0
MCD = 1
ingreso = int(input("Cuantos numeros va a ingresar\t"))

for i in range(ingreso):
  x=int(input("Digite el numero\t"))
  ListaNumeros.append(x)
  
numero=max(ListaNumeros)

for i in range (numero+1):
  contador=0
  for aux in range (2,i+1):
    if (i>=2  and i%aux==0 ):
      contador = contador + 1
    if aux==i and contador == 1:
      contador=0;
      ListaPrimos.append(i)


for elemento in ListaPrimos:
    contadorPrimos = contadorPrimos + 1
  
for indice in range(0,contadorPrimos):
  contadorMCD = 0
  repeticion = 1
  while (repeticion == 1):
    for indiceNumeros in range(0,ingreso):      
        if (ListaNumeros[indiceNumeros]%ListaPrimos[indice]==0):
          contadorMCD = contadorMCD + 1
    if contadorMCD==ingreso:
      ListaNumeros = [ x / ListaPrimos[indice] for x in ListaNumeros]
      repeticion=1
      contadorMCD=0
      MCD = MCD * ListaPrimos[indice]
    else:
      repeticion=0
      


print(f"Su máximo comun divisor es:\t {MCD}")