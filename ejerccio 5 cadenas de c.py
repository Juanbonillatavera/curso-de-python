palabra= input("coloque aqui la palabra")
palabra_length= len(palabra)
num_a= palabra.count("a")
num_e= palabra.count("e")
num_i= palabra.count("i")
num_o= palabra.count("o")
num_u= palabra.count("u")

metric= palabra_length*(num_a+ num_e+ num_i+num_o+num_u)

print(metric) 