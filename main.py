def verificar_desconto(cliente_vip, tem_cupom, valor_compra):
    P = cliente_vip
    Q = tem_cupom
    R = valor_compra

print("=" * 50)
print("🎉 Bem-vindo ao Sistema Verificador de Descontos! 🎉".center(50))
print("="*50)

while True:
    while True:
        cliente_vip = input("É Cliente VIP? (s/n): ").lower()
        if cliente_vip in ['s', 'n']:
            break 
        else:
            print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")

    if cliente_vip == 's':
        print("\nParabéns! Por ser cliente VIP, seu desconto foi aprovado!")
    else:
        print("\nCliente não VIP. Verificando outras condições...")
        
        tem_cupom = input("Tem Cupom? (s/n): ").lower()
        
        valor_compra = 0.0
        while True:
            try:
                valor_compra = float(input("Digite o valor da compra: R$ "))
                break 
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")

        if tem_cupom == 's' and valor_compra >= 100:
            print("\nParabéns! Por ter um cupom e compra acima de R$100, seu desconto foi aprovado!".center(60))
        else:
            print("\nQue pena! Você não atende aos requisitos para o desconto.".center(60))

    print("=" * 60)
    continuar = input("Deseja verificar um novo cliente? (s/n): ").lower()
    
    if continuar != 's':
        print("\nObrigado por usar o sistema. Encerrando...")
        break