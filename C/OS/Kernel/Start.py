#start
from Config import *

print(usuario)

#print(software)

#exec(software["printN"]%5)

import Kernel
import Processo
import time

def varius(*arg):
    st = "a "
    for i in arg:
        st = st + "%i "
    print(st%arg)

varius(1, 2, 4, 5, 6)


kn = Kernel.Kernel(usuario, quantum, escalonador[0])
kn.start()

def recuperar(nome, identidade):
    global kn
    return kn.encontrar(nome, identidade)

##print(software["fibonacciN"])

##Processos com busy wait Peterson
kn.novoProcesso("mulB", 2, software["mulB"], 2.4, 20, "A")
kn.novoProcesso("mulB", 2, software["mulB"], 2.1, 21, "A")

kn.novoProcesso("adB", 2, software["adB"], 2.4, 20, "B")
kn.novoProcesso("adB", 2, software["adB"], 2.1, 21, "B")

##Procesos sem busy wait
kn.novoProcesso("mul", 2, software["mul"], 2.4, 20, "C")
kn.novoProcesso("mul", 2, software["mul"], 2.1, 21, "C")

kn.novoProcesso("ad", 2, software["ad"], 2.4, 20, "D")
kn.novoProcesso("ad", 2, software["ad"], 2.1, 21, "D")

##kn.novoProcesso("printN", 4, software["printN"], 50)
##kn.novoProcesso("printN", 3, software["printN"], 40)
##kn.novoProcesso("printN", 2, software["printN"], 30)
kn.novoProcesso("printN", 2, software["printN"], 20)

##kn.novoProcesso("Fibonacci", 1, software["fibonacciN"], 1)
kn.novoProcesso("Fibonacci", 1, software["fibonacciN"], 10)
##kn.novoProcesso("Fibonacci", 1, software["fibonacciN"], 200)
##kn.novoProcesso("Fibonacci", 1, software["fibonacciN"], 100)

#print("teste")
#print(recuperar("printN", 3))

#print(kn.globais)

time.sleep(5)
print("Tempo medio turnaround")
print(kn.escalonador.turnaround())

##while len(kn.escalonador.tabela) != 1:
    ##time.sleep(3)

print("Tempo medio turnaround")
print(kn.escalonador.turnaround())
