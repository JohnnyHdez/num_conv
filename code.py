#!/usr/bin python

'''Este programa transforma un número decimal en un número hexadecimal, es decir de base 16.'''

def hex_upper(nDec):
	temp = []
	nHex = []
	
	while nDec >= 16:
		temp.append(nDec % 16)
		nDec = nDec // 16
	temp.append(nDec)
	
	i = 0
	
	while (i < len(temp)):
		if temp[i] == 10:
			temp[i] = 'A'
		if temp[i] == 11:
			temp[i] = 'B'
		if temp[i] == 12:
			temp[i] = 'C'
		if temp[i] == 13:
			temp[i] = 'D'
		if temp [i] == 14:
			temp[i] = 'E'
		if temp [i] == 15:
			temp [i] = 'F'
		i+= 1

	j = len (temp) - 1

	while j >= 0:
		nHex.append (temp [j])
		j -= 1
		
	return str(nHex).replace('[',''). replace (']','').replace(', ','').replace("'",'')

def hex_lower(nDec):
	temp = []
	nHex = []
	
	while nDec >= 16:
		temp.append(nDec % 16)
		nDec = nDec // 16
	temp.append(nDec)
	
	i = 0
	
	while (i < len(temp)):
		if temp[i] == 10:
			temp[i] = 'a'
		if temp[i] == 11:
			temp[i] = 'b'
		if temp[i] == 12:
			temp[i] = 'c'
		if temp[i] == 13:
			temp[i] = 'd'
		if temp [i] == 14:
			temp[i] = 'e'
		if temp [i] == 15:
			temp [i] = 'f'
		i+= 1

	j = len (temp) - 1

	while j >= 0:
		nHex.append (temp [j])
		j -= 1
		
	return str(nHex).replace('[',''). replace (']','').replace(', ','').replace("'",'')
