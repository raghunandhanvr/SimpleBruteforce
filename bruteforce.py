cl = "abcdefghijklmnopqrstuvwxyz" #wordlist

passw = "raghu"

for a in range(5):
	b = [c for c in cl]
	for d in range(a):
		b= [e + c for c in cl for e in b]
		if passw in b:
			print(f'pass:{b[b.index(passw)]}')
			exit()
