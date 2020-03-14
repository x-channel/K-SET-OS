####Isso eh importante para evitar confusoes sobre variaveis locais
import threading
import time
import sys


####Definida a classe que representa 1 processo.
##Ele compreende o cabecalho que o SO leh
##Tambem compreende o codigo do software que esta executando
class Processo(threading.Thread):
    def __init__(self, nome, usuario, identidade, kernel, programa, *args):
        threading.Thread.__init__(self, name=nome)
        self.nome = nome
        self.usuario = usuario
        self.identidade = identidade #id unico do processo
        self.kernel = kernel #kernel do SO

        ## TODO preprocessamento
        self.programa = programa.split("\n") #codigo fonte do programa em python
        self.args = args #argumentos para o processo
        self.__evento = threading.Event() #o evento que vai pausar a tread

        self.entrada = []
        self.saida = []
        
        self.__deltaTime = 0.0
        self.__tempoTotal = 0.0

    def run(self):
        linha = 0
        #Este loop varre o programa linha a linha
        try:
            #### TODO isso precisa ser reformulado
            ## Talvez a melhor forma seja inserir clear wait no programa.
            ## Porem no momento eh valido os programas da forma que estao.
            ## Porem dessa nova forma a avaliacao eh atomica.
            while linha != len(self.programa):
                #TODO contar o tempo de cada operacao
                self.__evento.clear()
                exec(self.programa[linha])
                linha += 1
                #self.kernel.passo(self.identidade) ##TODO
                self.__evento.wait()
                #TODO uma possibilidade do programa acabar.
        except:
            print("Houve um erro doloroso")
            e = sys.exc_info()
            print(e)
        #Apos a conclusao, eh necessario fazer a chamada end
        self.fim()

    ##Esse metodo permite que o processo execute a proxima linha
    def passo(self):
        self.__evento.set()

    
    def fim(self):
        #self.kernel.fim(self.identidade) ##TODO
        pass


# exemplo de argumentos infinitos
def soma(*args):
    total = 0
    print(args)
    for i in args:
        total += i
    return total


# exemplo de objeto da classe Processo()
prog0 = """print("Oi")
print("Ai")
print("Ui")"""

prog = """print("Oi")
print("Ai")
print("Ui")
print(self.args[0])"""

processinho = Processo("Alexandre Frota", "SYSTEMA", "21", None, prog, "aaa", "bbb")

# botando ele para funcionar na manivela
processinho.start()
time.sleep(0.1)
processinho.passo()
time.sleep(0.1)
processinho.passo()
time.sleep(0.1)
processinho.passo()
