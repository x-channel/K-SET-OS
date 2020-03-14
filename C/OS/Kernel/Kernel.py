import os
import threading

class Kernel(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name = "Kernel")
        self.nome = "Kernel"
        self.usuario = "SISTEMA"
        self.identidade = 1
        
        ##Aqui estarao as variaveis globais
        self.globais = {} ##VARIAVEL: (VALOR, SINCR)
        
