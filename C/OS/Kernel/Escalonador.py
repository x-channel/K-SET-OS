import threading
import time
import sys

class Escalonador(threading.Thread):
    def __init__(self, kernel, quantum):
        threading.Thread.__init__(self, name="Escalonador")
        self.nome = "Escalonador"
        self.usuario = "SISTEMA"
        self.identidade = 2 # A identidade desse processo

        self.kernel = kernel
        self.quantum = quantum
        
        self.contador = 3 # Vai garantir que haja um PID unico

        self.tabela = []
        self.fila = []

    def run(self):
        ##O escalonador eh um loop infinito
        while 1:
            self.ordenar()
            for i in self.fila:
                ##O escalonador escolhe o Processo
                ##O escalonador reorganiza a fila
                ##Inicia o timer
                ##print(time.monotonic())
                s0 = time.monotonic()
                se = s0
                ##print(i.nome, i.identidade)
                try:
                    ##loop while, com as condicoes de tempo < self.quantum and falta de excecao and not end
                    while (s0 + self.quantum) > se and i.chamada.is_set():
                        ##Dentro do loop eh verificado se o processo.pause()
                        if i.pause():
                            ##Caso processo.pause() == True, o escalonador chama processo.passo()
                            i.passo()
                        ##Finalmente o escalonador atualiza o tempo.
                        se = time.monotonic()
                    i.tempoTotal += (se - s0)
                except:
                    print("Houve um erro")
                    e = sys.exc_info()
                    print(e)
                    time.sleep(5)
                ##Finalmente o escalonador atualiza o tempo decorrido dentro do Processo
        pass

    def novo(self, processo):
        self.contador += 1
        self.tabela.append(processo)
        processo.start()

    def fim(self, processo):
        if processo in self.tabela:
            #print(processo.name, processo.identidade, processo.tempoTotal)
            self.tabela.remove(processo)

    def ordenar(self, algoritmo = None):
        self.fila = []
        for i in self.tabela:
            self.fila.append(i)
