from itertools import cycle

def validar_rut(rut):
	rut = limpiar_rut(rut)
	if rut.find("-") == -1:
		return False
	split_rut = rut.split("-")
	if digito_verificador(split_rut[0]) == split_rut[1]:
		return True
	else:
		return False

def limpiar_rut(rut):
	rut = rut.upper()
	list_rut = rut.split(".")
	clean_rut = ""
	for lrut in list_rut:
		clean_rut = clean_rut + lrut
	return clean_rut 

def digito_verificador(rut):
	reversed_digits = map(int, reversed(str(rut)))
	factors = cycle(range(2, 8))
	s = sum(d * f for d, f in zip(reversed_digits, factors))
	verificado = (-s) % 11
	if verificado == 11:
		verificado = "K"
	return str(verificado)