import threading

class Escalonador(threading.Thread):
    def __init__(self, kernel):
        threading.Thread.__init__(self, name="Escalonador")
        self.nome = "Escalonador"
        self.usuario = "SISTEMA"
        self.identidade = 2 # A identidade desse processo

        self.kernel = kernel
        
        self.contador = 2 # Vai garantir que haja um PID unico

        self.tabela = []
        self.fila = []

    def run(self):
        pass
