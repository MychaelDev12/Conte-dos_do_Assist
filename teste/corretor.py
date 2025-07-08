#refv = ["analisa/analisa.txt","calcula/calcula.txt","classifica/classifica.txt","compara/compara.txt","descreve/descreve.txt","dizer/dizer.txt","estar/estar.txt","faca/faca.txt","falar/falar.txt","fazer/fazer.txt","identifica/identifica.txt","isola/isola.txt","poder/poder.txt","representa/representa.txt","resolva/resolva.txt","significa/significa","tem/tem.txt","transforma/transforma.txt","use/use.txt"]

ref_p = ["porques","para","quando","onde","quanto","quantos","como","o que","quais"]
		
refv = ["analisa","calcula","classifica","compara","descreve","dizer","estar","faca","falar","fazer","identifica","isola","poder","representa","resolva","significa","tem","transforma","use"]



def corretor(cont,key):
	
	invalidos = []
	sub = []
	ind =	[]
	palavra = []
	chave = []
	ck = []
	
	cont = cont.lower()
	key = key.lower()
	
	for n in cont:
		palavra.append(n)
		
	for n in key:
		chave.append(n)
	
	if len(chave) > len(palavra):
		h = 3
	
	elif len(palavra) > len(chave):
		h = 3
		
	elif len(palavra) == len(chave):
		h = 3
	
	
	if h > 3:
		return "não compreendi"
	
	elif h <= 3:
		
		for n in palavra:
			
			if n in chave:
				
				#if n not in ck:
				ck.append(n)
			
			
			#while len(ck) < len(chave):
				#ck.append(" ")
			
		if len(ck) >= 3:
			
			
			return chave
		
		elif len(ck) < 3:
			return "não compreendi"
			
			
		
	for n in range(0,5,1):
		
		#if n > len(palavra) and len(chave):
		#	break;
			if True:
				
				if palavra[n] == chave[n]:				
					
					pass
				
				else:
					invalidos.append(palavra[n])
				
					ind.append(n)
					
					
					sub.append(chave[n])
	
	for n in range(0,len(invalidos),1):
		palavra[ind[n]] = sub[n]
		return palavra
		

def comparar(p1,ref):
	
	letras = []
	letras2 = []
	
	for n in ref:
		
		if p1 == n:
			
			letras2.append(p1)
		
		if len(letras2) == 1:
			return letras2					
			
		
		if len(p1) == 3:
			
			if p1[0] == n[0]:
				letras.append(n[0])
				
			
			if p1[1] == n[1] :
				letras.append(n[1])
						
			
			if p1[2] == n[2]:
				letras.append(n[2])
				#return letras[2]
			
			if len(letras) == 3:
				return corretor(str(letras),n)
				
			else:
				letras.clear()
		
		
		elif len(p1) == 4:
			
			if p1[0] == n[0]:
				letras.append(n[0])
				
			
			if p1[1] == n[1] :
				letras.append(n[1])
						
			
			if p1[2] == n[2]:
				letras.append(n[2])
				#return letras[2]
			
			if p1[3] == n[3]:
				letras.append(n[3])
				#return letras[2]
			
			if len(letras) == 4:
				return print(corretor(str(letras),n))
				
			else:
				letras.clear()
		
		
		
		elif len(p1) >= 5 and p1[0] == n[0]:
			letras.append(p1)
			
			if len(p1) == 5 and not len(n) == 4:
				if p1[4] == n[4] and len(letras2) == 0:
				
					return corretor(str(letras),n)
					
				
			else:
				
				if len(letras2) == 0:
					return corretor(str(letras),n)
			

def testar(p,ref):
	
	return comparar(p,ref)



			
			
	
#print(testar("ond",ref_p))
#print(certa)
		
#print(corretor("pq x é negativo","porque x é negativo"))	
