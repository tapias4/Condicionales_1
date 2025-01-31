cant_minutos = int(input("Digite la cantidad de minutos que duro la llamada: ")) # input

if cant_minutos <= 3:

    valor_llama = 300

else:

    valor_llama = 300+50*(cant_minutos-3)

print(f"el valor de l llamada es: " + str(valor_llama))
