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
            self.escalonar()
            for i in self.fila:
                ##O escalonador escolhe o Processo
                ##O escalonador reorganiza a fila
                ##Inicia o timer
                print(time.monotonic())
                ##loop while, com as condicoes de tempo < self.quantum and falta de excecao
                    ##Dentro do loop eh verificado se o processo.pause()
                        ##Caso processo.pause() == True, o escalonador chama processo.passo()
                    ##Finalmente o escalonador atualiza o tempo.
                ##Finalmente o escalonador atualiza o tempo decorrido dentro do Processo
        pass

    def novo(self, processo):
        pass

    def fim(self, processo):
        ##Todas as referencias sao apagadas das listas tabela e fila
        pass

    def escalonar(self, algoritmo = None):
        pass
