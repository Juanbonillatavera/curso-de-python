puede_volar=str(input("¿Puede volar? responda si o no"))
es_humano=str(input("¿Es humano? responda si o no"))
tiene_mascara=str(input("¿Tiene mascara? responda si o no"))


if puede_volar=="si":
    if es_humano=="si":
        if tiene_mascara=="si":
            print("ironman")
        else:
            print("capitan marvel")
    else:
        if tiene_mascara=="si":
            print("ronan el acusador")
        else:
            print("vision")
else:
    if es_humano=="si":
        if tiene_mascara:
            print("hombre araña")
        else:
            print("hulk")
    else:
        if tiene_mascara=="si":
            print("black bolt")
        else:
           print("thanos")