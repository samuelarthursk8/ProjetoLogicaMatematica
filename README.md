## Sistema Verificador de Descontos
Este é um script simples em Python que simula um sistema de verificação de descontos para uma loja. O programa interage com o usuário através do terminal para determinar se um cliente é elegível para um desconto com base em um conjunto de regras.

## 📖 Descrição

O objetivo principal deste script é aplicar regras de negócio para conceder um desconto a um cliente. A elegibilidade é baseada em três fatores:

    Se o cliente é VIP.

    Se o cliente possui um cupom de desconto.

    O valor total da compra.

O script foi projetado para ser interativo e amigável, com validações de entrada para garantir que o usuário forneça respostas válidas.

## ✨ Funcionalidades

    Interface de Linha de Comando: Interação simples e direta com o usuário.

    Verificação de Múltiplas Condições: O sistema avalia diferentes cenários para aprovar um desconto.

    Validação de Entrada: Garante que o usuário digite 's' ou 'n' para perguntas de sim/não e um valor numérico 
    para a compra.

    Loop de Execução: Permite verificar vários clientes em sequência sem precisar reiniciar o script.
  
## ⚙️ Regras de Negócio e Lógica

O desconto é aprovado se pelo menos uma das seguintes condições for verdadeira:

    O cliente é VIP.

    O cliente não é VIP, mas possui um cupom E o valor da sua compra é igual ou superior a R$ 100,00.

## 🖥️ Lógica Proposicional

A lógica do sistema pode ser representada usando as seguintes proposições, conforme sugerido no código (P, Q, R):

    P: O cliente é VIP.

    Q: O cliente tem um cupom.

    R: O valor da compra é igual ou superior a R$ 100,00.

O desconto será aprovado se a expressão lógica P ∨ (Q ∧ R) for verdadeira. Ou seja: "O cliente é VIP OU (tem cupom E a compra é >= R$ 100,00)".

## 🚀 Como Executar

    Pré-requisitos: Certifique-se de ter o Python instalado em seu sistema.

    Salve o Código: Salve o código-fonte em um arquivo chamado verificar_desconto.py.

    Abra o Terminal: Abra um terminal ou prompt de comando.

    Navegue até o Diretório: Use o comando cd para navegar até a pasta onde você salvou o arquivo.

    Execute o Script: Digite o seguinte comando e pressione Enter:
    Bash

    python verificar_desconto.py

    Siga as Instruções: O programa solicitará as informações necessárias para verificar o desconto.

## 💻 Exemplo de Uso

## Cenário 1: Cliente VIP

    ==================================================
    🎉 Bem-vindo ao Sistema Verificador de Descontos! 🎉
    ==================================================
    É Cliente VIP? (s/n): s

    Parabéns! Por ser cliente VIP, seu desconto foi aprovado!
    ============================================================
    Deseja verificar um novo cliente? (s/n): s

## Cenário 2: Cliente com Cupom e Compra Alta

    ==================================================
    🎉 Bem-vindo ao Sistema Verificador de Descontos! 🎉
    ==================================================
    É Cliente VIP? (s/n): n

    Cliente não VIP. Verificando outras condições...
    Tem Cupom? (s/n): s
    Digite o valor da compra: R$ 150

    Parabéns! Por ter um cupom e compra acima de R$100, seu desconto foi aprovado!
    ============================================================
    Deseja verificar um novo cliente? (s/n): s

## Cenário 3: Sem Direito ao Desconto

    ==================================================
    🎉 Bem-vindo ao Sistema Verificador de Descontos! 🎉
    ==================================================
    É Cliente VIP? (s/n): n

    Cliente não VIP. Verificando outras condições...
    Tem Cupom? (s/n): n
    Digite o valor da compra: R$ 200

    Que pena! Você não atende aos requisitos para o desconto.
    ============================================================
    Deseja verificar um novo cliente? (s/n): n

    Obrigado por usar o sistema. Encerrando...
