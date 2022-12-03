def criar_multiplicador(multiplicar):
    def multiplicador (numero):
        return numero * multiplicar
    return multiplicador

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))     
    