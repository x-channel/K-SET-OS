import threading

class Saida(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="Terminal Saida")
        self.nome = "Terminal Saida"
    
    def saida(self, processo, id, valor):
        print(processo, id, ":", valor)