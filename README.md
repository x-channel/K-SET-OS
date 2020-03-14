# K SET OS
Repositório do simulador produzido para a disciplina de Sistemas Operacionais em 2020.1 na UFRPE


## Observações

Devido a implementação, o simulador provavelmente não será compatível com classes.

Os SCRIPTS deverão usar self.FUNCAO(PARAMETRO) para fazer chamadas ao sistema.

Os scripts serão preprocessados para poderem rodar dentro da classe Processo. Uma das caracteristicas é a declaração do objeto chamado kernel. Apagar todos os comentários; Apagar linhas em branco; Adicionar evento.clear() e evento.wait() entre todas as linhas para permitir a preempção; Substituir algumas chamadas como print() por kernel.print(); Adicionar kernel.fim() na última linha.


## Chamadas do sistema

### kernel.global(variavel, *args)
Cria ou altera uma variável global.

### kernel.sincronizar(variavel)
Avisa ao SO que o script chegou a um ponto crítico e quer este recurso.

### kernel.liberar(variavel)
Avisa ao SO que o recurso já está disponível.

### kernel.input()
Pede uma entrada do teclado para o kernel.
Está em inglês por fazer a mesma coisa que a função build in.

### kernel.print(texto)
Envia um texto para o kernel imprimir na tela.
Isso pode parecer desnecessário, mas o simulador todo é desnecessário. Então vamos apenas abrir um sorriso e se divertir com esses detalhes.

### kernel.fim()
Avisa ao SO que o processo foi concluído.
