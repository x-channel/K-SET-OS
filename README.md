# K SET OS
Repositório do simulador produzido para a disciplina de Sistemas Operacionais em 2020.1 na UFRPE


## Observações

Devido a implementação, o simulador provavelmente não será compatível com classes.
Os SCRIPTS deverão usar self.FUNCAO(PARAMETRO) para fazer chamadas ao sistema.



## SYSCALL

### self.global(variavel, *args)
Cria ou altera uma variável global.

### self.sincronizar(variavel)
Avisa ao SO que o script chegou a um ponto crítico e quer este recurso.

### self.liberar(variavel)
Avisa ao SO que o recurso já está disponível.

### self.input()
Pede uma entrada do teclado para o kernel.
Está em inglês por fazer a mesma coisa que a função build in.

### self.print(texto)
Envia um texto para o kernel imprimir na tela.
Isso pode parecer desnecessário, mas o simulador todo é desnecessário. Então vamos apenas abrir um sorriso e se divertir com esses detalhes.

### self.fim()
Avisa ao SO que o processo foi concluído.
