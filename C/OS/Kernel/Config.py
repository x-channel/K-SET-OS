import Kernel

usuario = "Afeto"
senha = "aaaa"

quantum = 0.2

escalonador = ["Round Robin", "Loteria"]

software = {
"printN":
"""N = %i
for i in range(N):
    self.saidaT(i)
tempo = "tempo total: " + str(self.tempoTotal)
self.saidaT(tempo)""",

"fibonacciN":
"""N = %i
if N > 1:
    a1 = 1
    a2 = 1
    for i in range(N):
        valor = a1+a2
        a1 = a2
        a2 = valor
else:
    valor = 1
self.saidaT(valor)
tempo = "tempo total: " + str(self.tempoTotal)
self.saidaT(tempo)""",

"mulB":
"""N = %f
M = %i
V = "%s"
at = self.variavelInsta(V, 1.0)
self.bandeira(V)
self.turno(V)
while(not self.verde(V)):
    pass
at = self.variavelInsta(V, 0.0)
for i in range(M):
    at *= N
    at = self.variavelInsta(V, at, "sobrescrever")
self.saidaT(at)
self.liberar(V)
tempo = "tempo total: " + str(self.tempoTotal)
self.saidaT(tempo)""",

"adB":
"""N = %f
M = %i
V = "%s"
at = self.variavelInsta(V, 0.0)
self.bandeira(V)
self.turno(V)
while(not self.verde(V)):
    pass
at = self.variavelInsta(V, 0.0)
for i in range(M):
    at += N
    at = self.variavelInsta(V, at, "sobrescrever")
self.saidaT(at)
self.liberar(V)
tempo = "tempo total: " + str(self.tempoTotal)
self.saidaT(tempo)"""
}
