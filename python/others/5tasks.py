#NB! Kasutage palun kontrollimiseks kõik scriptid eraldi, et ulesanne 1 eraldi ulesandest 2, ärge proovi kasutada kõik scriptid koos


#ulesanne 1
print('Tere')


#ulesanne 2
a=3+8/(4-2)*4
print(a)


#ulesanne 3
from math import *
r=3
d=6
S_1=float(r*d)
P_1=float(d*6)
S_2=float(pi*r**2)
P_2=float(2*pi*3)
print(S_1)
print(P_1)
print(floor(S_2)) 
print(ceil(P_2))


#ulesanne 2.2 Lihtne muutuda andmeid, naiteks diaametrit uheks mundiks, ei ole vaja kasutada PI, siis pole vaja teha liigset ümardamist
from math import *
earth_km=63878
money_km=0.00002575
distance=floor(earth_km/money_km)
print('We need '+ str(distance) + ' 2eu-coins')
#ulesanne 3 Sest sõnad muutuvad lause jooksul, kasutasin primitiivset formulat, viimane 'kill-koll' panin teisele reale, kasutan \n
a=str("kill-koll kill-koll killadi-koll")*2+('kill-koll kill-koll killkoll \nkill-koll')
print(a)


#ulesanne 4 Kui juba on vaja kolmas laul, lisame veel uks varriable, ka saame kasutada replace, aga kas on vaja leituda jalgratta?
a=int(input('Esimene laul - 1; Teine -2\n[1 or 2]:'))
if a==1:
	print('Rong see sõitis tsuhh tsuhh tsuhh,\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?')
elif a==2:
	print('Rong see sõitis tuut tuut tuut,\npiilupart oli rongijuht.\nRattad tegid kill koll koll,\nkill koll koll ja kill koll kill.\n\n....Sisend, väljund, tingimus...')
else: print('Viga')


#ulesanne 5  :):):):):)
a=float(input('Ristküliku pikkus:'))
b=float(input('Ristküliku laius:'))
c=input('What you want calculate?\n[S or P]:')
if c=="S":
	c1=a*b
	print(c1)
elif c=="P":
	c2=2*(a+b)
	print(c2)
else: print('S or P nothing more!')












