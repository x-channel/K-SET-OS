#start
from Config import *

print(usuario)

print(software)

exec(software["printN"]%5)

import Kernel

def varius(*arg):
    st = "a "
    for i in arg:
        st = st + "%i "
    print(st%arg)

varius(1, 2, 4, 5, 6)

kn = Kernel.Kernel(usuario, quantum)

kn.novoProcesso("printN", software["printN"], 5)
