import os
import threading
import Escalonador
import Processo

class Kernel(threading.Thread):
    def __init__(self, usuario, quantum):
        threading.Thread.__init__(self, name = "Kernel")
        self.nome = "Kernel"
        self.usuario = "SISTEMA"
        self.usuario2 = usuario
        

        ##O escalonador.
        self.escalonador = Escalonador.Escalonador(self, quantum)
        self.escalonador.start()

        ##Identidade do processo Kernel
        self.identidade = 1
        
        self.__evento = threading.Event() #o evento que vai pausar a tread
        self.chamada = threading.Event() #tambem vai pausar a tread, mas pela syscall
        self.chamada.set()

        ##Aqui estarao as variaveis globais
        self.globais = {} ##VARIAVEL: (VALOR, SINCR)
        
        self.chamadas = []
        
        self.tempoTotal = 0.0

    def globais(self, variavel, valor, processo, sincronizada = -1):
        if variavel in self.__globais:
            if self.__globais[variavel][1] in [-1, processo.identidade] or processo.usuario in ["SISTEMA", "ADM"]:
                self.__globais[variavel] = (valor, sincronizada)
        else:
            self.__globais[variavel] = (valor, sincronizada)

    def novoProcesso(self, nome, software, *arg):
        novo = Processo.Processo(nome, self.usuario2, self.escalonador.contador, self, software, *arg)
        self.escalonador.novo(novo)
    
    def fim(self, processo):
        self.escalonador.fim(processo)


#kn = Kernel()
