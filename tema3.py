'''1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.'''

note_muzicale=['do', 're' , 'mi' , 'fa' , 'so' , 'la' , 'si' , 'do']
print(note_muzicale)
note_muzicale=note_muzicale[::-1]
print('note muzicale inversate:', note_muzicale)
note_muzicale.reverse()
print('lista initiala note', note_muzicale)

# 2.
# De cate ori apare ‘do’?

print(note_muzicale.count('do'))


'''# 3.
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista. 
'''
prima_lista=[3,1,0,2]
lista_secundara=[6,5,4]

lista_impreunata= prima_lista+lista_secundara
print(lista_impreunata)

prima_lista.extend(lista_secundara)
print(prima_lista)
'''
4.
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista
'''
prima_lista.sort()
print(prima_lista)

prima_lista.remove(0)
print(prima_lista)

#5.
#Folosind un if verificati lista generata la ex3 si afisati
#Lista este goala
#Lista nu este goala'''

if len(lista_impreunata) == 0:
    print('Lista este goala')
else: print('Lista nu e goala')

#6.
#Folositi o functie care sa stearga lista de la ex3

lista_impreunata.clear()

#7.
#Copy paste la ex 5. Verificati inca o data.
#Acum ar trebui sa se afiseze ca lista e goala

if len(lista_impreunata) == 0:
    print('Lista este goala')
else: print('Lista nu e goala')


#8.
#Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(dict1)
print(dict1.keys())


#9.
#Printati cei 3 elevi si notele lor
#Ex: ‘Ana a luat nota {x}’
#Doar nota o veti lua folosindu-va de cheie

print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Ana a luat nota {dict1['Dorel']}")


#10.
#Dorel a facut contestatie si a primit 6
#Modificati nota lui Dorel in 6
#Printati nota dupa modificare

dict1["Dorel"] = 6
print(dict1)



#11.
#Gigel se transfera din clasa
#Cautati o functie care sa il stearga
#Vine un coleg nou. Adaugati Ionica, cu nota 9
#Printati noii elevi
dict1.pop("Gigel")
print(dict1)
dict1["Ionica"] = 9
print([dict1])


#12.
#Set
#zile_sapt =  , 'sambata', 'duminica'}
#weekend = {'sambata', 'duminica'}
#Adaugati in zilele_sapt ‘luni’
#Afisati zile_sapt

zile_sapt = {'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')

print(zile_sapt)
#13.
#Folositi un if si verificati daca
#Weekend este un subset al zilelor din sapt
#Weekend nu este un subset al zilelor din sapt

if(weekend.issubset(zile_sapt)):
    print("Weekend este un subset al zilelor din sapt")
else:
    print("Weekend nu este un subset al zilelor din sapt")

#14.
#Afisati diferentele dintre aceste 2 seturi
print(zile_sapt.difference(weekend))

#15.
#Afisati intersectia elementelor din aceste 2 seturi
print(weekend.intersection(zile_sapt))