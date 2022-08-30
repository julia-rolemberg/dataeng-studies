#3. Utilizando o paradigma funcional. 
# Faça uma função que calcule a progressão aritimetica de 0-n com constante r = 1
from functools import reduce
n=5

PA = reduce(lambda x, elemento: x + elemento, range(0,n+1)) 
print(PA)