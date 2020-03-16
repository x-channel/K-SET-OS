import os
import threading
import Escalonador
import Processo

class Kernel(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name = "Kernel")
        self.nome = "Kernel"
        self.usuario = "SISTEMA"

        ##O escalonador.
        self.escalonador = Escalonador.Escalonador(self)
        self.escalonador.start()

        ##Identidade do processo Kernel
        self.identidade = 1

        ##Aqui estarao as variaveis globais
        self.globais = {} ##VARIAVEL: (VALOR, SINCR)


kn = Kernel()

print(__name__)
