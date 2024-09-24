# desafioTecnico


## Exercício 4: Descubra a lógica e complete o próximo elemento da sequência

a) 1, 3, 5, 7, ___  
**Resposta**: 9

b) 2, 4, 8, 16, 32, 64, ____  
**Resposta**: 128

c) 0, 1, 4, 9, 16, 25, 36, ____  
**Resposta**: 49

d) 4, 16, 36, 64, ____  
**Resposta**: 100

e) 1, 1, 2, 3, 5, 8, ____  
**Resposta**: 13

f) 2, 10, 12, 16, 17, 18, 19, ____  
**Resposta**: 20

---

## Exercício 5: Problema dos Interruptores e Lâmpadas

### Descrição do problema:

Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.  
Você não pode ver as lâmpadas da sala onde está, mas pode ligar e desligar os interruptores quantas vezes quiser.  
Seu objetivo é descobrir qual interruptor controla qual lâmpada.  
Você só pode visitar a sala das lâmpadas duas vezes. 

### Solução proposta:

1. **Ligue o primeiro interruptor e espere por alguns minutos**.
   - O objetivo é que a lâmpada ligada esquente.

2. **Desligue o primeiro interruptor e ligue o segundo**.

3. **Vá até a sala das lâmpadas**:
   - A lâmpada **que está acesa** será controlada pelo **segundo interruptor**.
   - A lâmpada **que está apagada mas quente** será controlada pelo **primeiro interruptor**.
   - A lâmpada **que está apagada e fria** será controlada pelo **terceiro interruptor**.

Com essa estratégia, você consegue determinar qual interruptor controla cada lâmpada com apenas **duas idas** até a sala das lâmpadas.
