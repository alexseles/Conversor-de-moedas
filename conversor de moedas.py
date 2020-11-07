
real = float(input("Digite o valor em Real que você quer converter para Dólar e Euro:"))
dolar = real / 5.36
euro = real / 6.37
print("Com R${:.3f} você pode comprar US$ {:.3f}" .format(real, dolar))
print("Com R${:.3f} você pode comprar €{:.3f}" .format(real, euro))
