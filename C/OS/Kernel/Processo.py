####Isso eh importante para evitar confusoes sobre variaveis locais
import threading


####Definida a classe que representa 1 processo.
##Ele compreende o cabecalho que o SO leh
##Tambem compreende o codigo do software que esta executando
class Processo(threading.Thread):
    def __init__(self, nome, usuario, identidade, kernel, programa, *args):
        threading.Thread.__init__(self, name=texto)
        self.nome = nome
        self.usuario = usuario
        self.identidade = identidade #id unico do processo
        self.kernel = kernel #kernel do SO
        self.programa = programa #codigo fonte do programa em python
        self.args = args #argumentos para o processo
        self.__evento = threading.Event() #o evento que vai pausar a tread

        self.__deltaTime = 0.0
        self.__tempoTotal = 0.0

    def run(self):
        linha = 0
        #Este loop varre o programa linha a linha
        #TODO montar o try and catch
        while 1:
            exec(self.programa[linha])
            linha += 1
            self.evento.clear()
            self.kernel.passo()
            self.evento.wait()
            #TODO uma possibilidade do programa acabar.
        pass

    def passo(self):
        self.evento.set()


# exemplo de argumentos infinitos
def soma(*args):
    total = 0
    print(args)
    for i in args:
        total += i
    return total
