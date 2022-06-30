import math

# Engrenagem Reta

def calculos(d_ext, m, z):
    if (d_ext == 0):
        d_ext = m * (z+2)
        print(f"\nDiâmetro Externo = {d_ext}mm")

    elif (m == 0):
        m = d_ext / (z + 2)
        print(f"\nMódulo = {m}")
    
    elif (z == 0):
        z = (d_ext / m) - 2
        print(f"\nNúmero de dentes = {z} dentes")
        
# Engrenagem Helicoidal 

def calculo_helicoidal(m, z, a):
    dp = (m * z) / math.cos(math.radians(a))
    d_ext = round(dp, 2) + (2 * m)
    print(f"\nDiâmetro Externo = {d_ext}mm") 
    
# Entrecentro

def calculo_entrecentro(z1, z2, m):
    ent = (m * (z1 + z2)) / 2
    print(f"\nEntrecentro: = {ent}mm")      
