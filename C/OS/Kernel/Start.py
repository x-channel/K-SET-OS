#start
from Config import *

print(usuario)

print(software)

exec(software["printN"]%5)

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

kn.novoProcesso("printN", software["printN"], 50)
kn.novoProcesso("printN", software["printN"], 40)
kn.novoProcesso("printN", software["printN"], 30)
kn.novoProcesso("printN", software["printN"], 20)
