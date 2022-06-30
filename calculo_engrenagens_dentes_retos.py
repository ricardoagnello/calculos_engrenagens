import funcao_calculos

print("\nCalculo de Engrenagens Dentes Retos")

print("\nDigite 0 para o dado a ser calculado")
d_ext = float(input("\nDigite o diametro: "))
m = float(input("\nDigite o módulo: "))
z = int(input("\nDigite o numero de dentes: "))

funcao_calculos.calculos(d_ext, m, z)

