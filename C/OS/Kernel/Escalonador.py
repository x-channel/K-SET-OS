import threading
import time

class Escalonador(threading.Thread):
    def __init__(self, kernel):
        threading.Thread.__init__(self, name="Escalonador")
        self.nome = "Escalonador"
        self.usuario = "SISTEMA"
        self.identidade = 2 # A identidade desse processo

        self.kernel = kernel
        self.quantum = quantum
        
        self.contador = 2 # Vai garantir que haja um PID unico

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
                try:
                    ##loop while, com as condicoes de tempo < self.quantum and falta de excecao and not end
                    while (s0 + self.quantum) > se:
                        ##Dentro do loop eh verificado se o processo.pause()
                        if i.pause():
                            ##Caso processo.pause() == True, o escalonador chama processo.passo()
                            i.passo()
                        ##Finalmente o escalonador atualiza o tempo.
                        se = time.monotonic()
                except:
                    print("Houve um erro")
                ##Finalmente o escalonador atualiza o tempo decorrido dentro do Processo
        pass

    def novo(self, processo):
        pass

    def fim(self, processo):
        ##Todas as referencias sao apagadas das listas tabela e fila
        pass

    def ordenar(self, algoritmo = None):
        pass
