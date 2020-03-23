#start
from Config import *

print(usuario)

print(software)

#exec(software["printN"]%5)

import Kernel
import Processo

def varius(*arg):
    st = "a "
    for i in arg:
        st = st + "%i "
    print(st%arg)

varius(1, 2, 4, 5, 6)


kn = Kernel.Kernel(usuario, quantum)
kn.start()

def recuperar(nome, identidade):
    global kn
    return kn.encontrar(nome, identidade)

##print(software["fibonacciN"])

kn.novoProcesso("printN", software["printN"], 50)
kn.novoProcesso("printN", software["printN"], 40)
kn.novoProcesso("printN", software["printN"], 30)
kn.novoProcesso("printN", software["printN"], 20)

kn.novoProcesso("Fibonacci", software["fibonacciN"], 1)
kn.novoProcesso("Fibonacci", software["fibonacciN"], 10)
kn.novoProcesso("Fibonacci", software["fibonacciN"], 200)
kn.novoProcesso("Fibonacci", software["fibonacciN"], 100)

#print("teste")
#print(recuperar("printN", 3))
