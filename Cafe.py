status = 1
while status != 0:
	nota = int(input('Em uma escala de 0 a 5 de a nota da qualidade do café: '))

	if nota <= 0:
		print ('O café ta um lixo, joga fora e faz de novo!')
	elif nota <= 1:
		print ('O café ta quase uma coca sem gás, mas, da para sentir o cheiro pelo menos!')
	elif nota <= 2:
		print ('Ta indo mas ainda sim prefiro agua de encanamento velho!')
	elif nota <= 3:
		print ('O café ta bom!')
	elif nota <= 4:
		print ('Ta beleza pode continuar assim, pelo menos temos condições de oferecer para as visitas!')
	elif nota <= 5:
		print ('Ta muito bom o café, acertou a mão!')
	else:
		print ('Ta bom pra caralho, Parabéns!')


	status = int(input('Se desejar continuar com a avaliação digite 1 se não digite 0: '))

