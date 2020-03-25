####Isso eh importante para evitar confusoes sobre variaveis locais
import threading
import time
import sys
from Config import *

####Definida a classe que representa 1 processo.
##Ele compreende o cabecalho que o SO leh
##Tambem compreende o codigo do software que esta executando
class Processo(threading.Thread):
    def __init__(self, nome, usuario, identidade, kernel, prioridade, programa, *args):
        threading.Thread.__init__(self, name=nome)
        self.nome = nome
        self.usuario = usuario
        self.identidade = identidade #id unico do processo
        self.kernel = kernel #kernel do SO
        self.prioridade = prioridade

        ## TODO preprocessamento
        #print(args)
        self.programa = self.formatar(programa)
        #print(self.programa)
        self.programa = self.programa%args
        #print(self.programa)
        #self.programa = programa.split("\n") #codigo fonte do programa em python
        self.args = args #argumentos para o processo

        
        self.__evento = threading.Event() #o evento que vai pausar a tread
        self.chamada = threading.Event() #tambem vai pausar a tread, mas pela syscall
        self.chamada.set()
        self.retorno = None

        self.entrada = []
        self.saida = []
        
        self.tempoTotal = 0.0
    
    def run(self):
        try:
            exec(self.programa)
        except:
            print("Houve um erro doloroso")
            print("Fim do processo: %s"%self.nome)
            e = sys.exc_info()
            print(e)
        self.fim()

    def runn(self):
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
        
    def saidaT(self, valor):
        ## adiciona a chamada a lista de chamadas do kernel
        self.kernel.chamadas.append(("saidaT", self.nome, self.identidade, valor))
        
        # Espera a execucao da chamada
        self.chamada.clear()
        self.chamada.wait()
        
        return self.retorno
        
    ##Esse metodo permite que o processo execute a proxima linha
    def formatar(self, programa):
        programa = programa.replace("    ", "\t")
        programa = programa.split("\n")
        saida = ""
        for i in range(len(programa)-1, -1, -1):
            if "else" in programa[i] or "elif" in programa[i]:
                saida = programa[i] + "\n" + saida
            else:
                saida = "\t"*programa[i].count("\t") + "self.esperar()" + "\n" + programa[i] + "\n" + saida
        ##cabecalho = "kernel = recuperar(%s, %i)\n"%(self.nome, self.identidade)
        ##cabecalho = "global kn\nkernel = kn.recuperar(%s, %i)\n"%(self.nome, self.identidade)
        ##saida = cabecalho + saida
        ##print("huummmmm")
        ##print(saida)
        ##print(self)
        return saida
        
    def passo(self):
        self.__evento.set()

    def esperar(self):
        self.__evento.clear()
        self.__evento.wait()

    ##Pausado?
    def pause(self):
        return not (self.__evento.is_set())

    
    def fim(self):
        self.kernel.fim(self) ##TODO
    
    def variavelInsta(self, vari, valor, act = "pegar"):
        pr = "%s %i"%(self.nome, self.identidade)
        return self.kernel.variavel(self, vari, valor, act)
    
    def bandeira(self, vari):
        self.kernel.bandeira(self, vari)
    
    def turno(self, vari):
        self.kernel.turno(vari)
    
    def verde(self, vari):
        pr = "%s %i"%(self.nome, self.identidade)
        return self.kernel.verde(pr, vari)
    
    def liberar(self, vari):
        pr = "%s %i"%(self.nome, self.identidade)
        self.kernel.globais[vari][2][pr] = False
        self.kernel.turno(vari)
    
    def quem(self, vari):
        pr = "%s %i"%(self.nome, self.identidade)
        if (self.kernel.globais[vari][1] == pr):
            return True
        else:
            return False


# exemplo de argumentos infinitos
def soma(*args):
    total = 0
    print(args)
    for i in args:
        total += i
    return total

if False:
    # exemplo de objeto da classe Processo()
    prog0 = """print("Oi")
    print("Ai")
    print("Ui")"""

    prog = """print(self)
    print("Oi")
    print("Ai")
    print("Ui")"""

    processinho = Processo("Alexandre Frota", "SYSTEMA", "21", None, prog)

    # botando ele para funcionar na manivela
    processinho.start()
    time.sleep(0.1)
    print(processinho.pause())
    processinho.passo()
    time.sleep(0.1)
    processinho.passo()
    time.sleep(0.1)
    #processinho.passo()
