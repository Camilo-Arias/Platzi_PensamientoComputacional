pesoTerrestre = float(input("ingrese su peso en kilogramos con (.) si tiene decimales: "))

gravedadMercurio = 3.7
gravedadVenus = 8.87
gravedadTierra = 9.81
gravedadMarte = 3.711
gravedadJupiter = 24.79
gravedadSaturno = 10.44
gravedadUrano = 8.87
gravedadNeptuno = 11.15
gravedadPluton = 0,62
gravedadLuna = 1.62

pesoMarte = (pesoTerrestre // gravedadTierra)*gravedadMarte

print(pesoMarte)