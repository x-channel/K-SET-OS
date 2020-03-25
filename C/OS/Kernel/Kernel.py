import os
import threading
import Escalonador
import Processo
import Terminal
import random

class Kernel(threading.Thread):
    def __init__(self, usuario, quantum, algoritmo):
        threading.Thread.__init__(self, name = "Kernel")
        self.nome = "Kernel"
        self.usuario = "SISTEMA"
        self.usuario2 = usuario
        

        ##O escalonador.
        self.escalonador = Escalonador.Escalonador(self, quantum, algoritmo)
        
        self.terminalS = Terminal.Saida()

        ##Identidade do processo Kernel
        self.identidade = 1
        
        self.prioridade = 5
        
        self.__evento = threading.Event() #o evento que vai pausar a tread
        self.chamada = threading.Event() #tambem vai pausar a tread, mas pela syscall
        self.chamada.clear()

        ##Aqui estarao as variaveis globais
        self.globais = {} ##VARIAVEL: (VALOR, turno, flags)
        self.__globais = {}
        
        self.chamadas = []
        
        self.tempoTotal = 0.0
    
    def run(self): #Ha um erro aqui
        self.escalonador.tabela.append(self)
        self.escalonador.start()
        while 1:
            if len(self.chamadas) > 0:
                self.chamada.set()
                self.esperar()
                caso = self.chamadas[0][0]
                if (caso == "saidaT"):
                    self.saidaT(self.chamadas[0][1], self.chamadas[0][2], self.chamadas[0][3])
                elif (caso == "variavel"):
                    pass
                elif (caso == "sincronizar"):
                    pass
                elif (caso == "dessincronizar"):
                    pass
            else:   self.chamada.clear()
            

    def globais(self, variavel, valor, processo, sincronizada = -1):
        if variavel in self.__globais:
            if self.__globais[variavel][1] in [-1, processo.identidade] or processo.usuario in ["SISTEMA", "ADM"]:
                self.__globais[variavel] = (valor, sincronizada)
        else:
            self.__globais[variavel] = (valor, sincronizada)

    def novoProcesso(self, nome, prioridade, software, *arg):
        novo = Processo.Processo(nome, self.usuario2, self.escalonador.contador, self, prioridade, software, *arg)
        self.escalonador.novo(novo)
    
    def fim(self, processo):
        self.escalonador.fim(processo)
    
    def saidaT(self, nome, identidade, valor):
        processo = self.encontrar(nome, identidade)
        try:
            if (not processo.chamada.is_set()):
                processo.retorno = 1
                processo.chamada.set()
                self.chamadas.pop(0)
                self.terminalS.saida(nome, identidade, valor)
        except:
            print("erro na chamada do sistema")
            self.chamadas.pop(0)
    
    def variavel(self, nome, identidade, vari, valor, act):
        processo = self.encontrar(nome, identidade)
        pass
    
    def sincronizar(self, nome, identidade, vari):
        processo = self.encontrar(nome, identidade)
        self.chamada.clear()
    
    def dessincronizar(self, nome, identidade, vari):
        processo = self.encontrar(nome, identidade)
        pass
    
    def encontrar(self, nome, identidade):
        tabela = self.escalonador.tabela
        for i in tabela:
            if (i.nome == nome):
                if (i.identidade == identidade):
                    return i
        return None
    
    ##Pausado?
    def pause(self):
        return not (self.__evento.is_set())
    
    def passo(self):
        self.__evento.set()

    def esperar(self):
        self.__evento.clear()
        self.__evento.wait()
    
    def variavelInsta(self, processo, vari, valor, act = "pegar"): #pegar ou sobrescrever
        pr = "%s %i"%(processo.nome, processo.identidade)
        if act == "pegar" and vari in self.globais:
            pass
        elif not vari in self.globais:
            self.globais[vari] = (valor, pr, {pr:False})
        else:
            dc = self.globais[vari][2]
            if not pr in dc:
                dc[pr] = False
            vez = self.globais[vari][1]
            self.globais[vari] = (valor, vez, dc)
        return self.globais[vari][0]
    
    def bandeira(self, processo, vari):
        pr = "%s %i"%(processo.nome, processo.identidade)
        self.globais[vari][2][pr] = True
    
    def verde(self, pr, vari):
        j = self.globais[vari][2]
        for i in j:
            if i != pr:
                if j[i] == True:
                    return False
        return True
    
    def turno(self, vari):
        j = self.globais[vari][2]
        t = False
        for i in j:
            t = t or j[i]
        if t:
            i = random.choice(list(j))
            while not j[i]:
                i = random.choice(list(j))
            valor = self.globais[vari][0]
            self.globais[vari] = (valor, i, j)
        

#kn = Kernel()
