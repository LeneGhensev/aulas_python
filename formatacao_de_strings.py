print("*********************************")
print("Exemplos de Formatação de Strings")
print("*********************************")

print("Link da documentação: https://docs.python.org/3/library/string.html#formatexamples")
print("*********************************")

print("Invertendo a ordem:")
print("Tentativa {1} de {0}".format(1, 3))

print("Formatação de float:")
print("R$ {:f}".format(1.59))
print("Definindo 2 casas depois da vírgula:")
print("R$ {:.2f}".format(1.59))
print("R$ {:.2f}".format(1.5))
print("R$ {:.2f}".format(1))

print("Definindo quantidade de caracteres e 2 casas depois da vírgula:")
print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.59))
print("R$ {:7.2f}".format(1))

print("Definindo quantidade de caracteres, colocando zeros à frente e 2 casas depois da vírgula:")
print("R$ {:07.2f}".format(1234.50))
print("R$ {:07.2f}".format(1.59))
print("R$ {:07.2f}".format(1))

print("Formatação de data:")
print("Data {:02d}/{:02d}".format(9, 4))
print("Data {:02d}/{:02d}".format(19, 11))

