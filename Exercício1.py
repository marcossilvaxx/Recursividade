def imprimirRec(x,y):
   print(x)
   if x == y:
       return y
   return imprimirRec(x + 1, y)
   
x = eval(input("Informe o número x:\n"))
y = eval(input("Informe o número y:\n"))

imprimirRec(x,y)
