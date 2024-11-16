print("*** DEFINIR SI IN NUMERO ES PAR O NO ")

num = int(input("digite un numero entero "))
rta = num % 2
if (rta == 0):
  print(f"  {num} ES PAR")
else:
  print(f"  {num} ES IMPAR")