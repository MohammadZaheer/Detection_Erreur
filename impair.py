#!/usr/bin/env python3

def impair(p):
	for i in p:
		c = bin(i).strip('0b')
		if (c.count('1') % 2 == 0):
			d = '1' + c
			e = bytearray(d,'utf-8')
		else:
			d = '0' + c
			e = bytearray(d,'utf-8')
	print(e)
	
a = input("Entrez un mot svp: ")
b = bytearray(a, 'utf-8')
impair(b)
