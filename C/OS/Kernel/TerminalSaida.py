import threading

class SaidaT(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="Terminal Saida")
        self.nome = "Terminal Saida"