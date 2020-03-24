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
self.saidaT(tempo)"""
}
