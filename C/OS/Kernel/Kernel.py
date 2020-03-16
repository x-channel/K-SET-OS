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

    def globais(self, variavel, valor, processo, sincronizada = -1):
        if variavel in self.__globais:
            if self.__globais[variavel][1] in [-1, processo.identidade] or processo.usuario in ["SISTEMA", "ADM"]:
                self.__globais[variavel] = (valor, sincronizada)
        else:
            self.__globais[variavel] = (valor, sincronizada)

    def novoProcesso(self):
        pass


kn = Kernel()
