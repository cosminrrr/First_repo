#1 avand lista

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#a.Folositi un for ca sa iterati prin toata lista si sa afisati
#‘Masina mea preferata este x’

for x in range(len(masini)):
    print('Masina mea preferata este: '+ masini[x])
# b.	Faceti acelasi lucru cu un for each
print('for-each')
for masina in masini:
    print(f'Masina mea preferata este {masina}')
#c.	Faceti acelasi lucru cu un while
print('while')
i=0
while i<len(masini):
    print('Masina mea preferata este '+ masini[i] )
    i+=1

#2 ACeasi lista. Folositi un for in for.
# Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul#
masini= ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    for y in range(1,len(masini)-1):
        masini[y]=masini[y].upper()
print(masini)

# 3

# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam


masini= ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in masini:
     if x=='Mercedes':
        print('Am gasit masina dumneavostra.')
        break
     else:
          print('Am gasit masina ' + x + '.Mai cautam.')

#4

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in masini:
    if (x == 'Trabant' or x == 'Lastun'):
        continue
    else:
        print('S-ar putea sa va placa masina ' + x)

# 5
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for x in range(len(masini)):
    if (masini[x] == 'Trabant') or (masini[x] == 'Lastun'):
        masini_vechi.append(masini[x])
        masini[x] = 'Tesla'
print(masini_vechi)
print(masini)

# 6 Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for x in pret_masini:
    if pret_masini[x] <= 15000:
        print('Pentru un beget de sub 15000 puteti alege masina:', x)
# 7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
for numar in numere:
    if numar == 3:
        i = i + 1
print('Numarul 3 apare de', i, 'ori.')
# 8
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s = 0
for numar in numere:
    s = s + numar
print('Suma numerelor din lista este :', s)
# 9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# varianta cu for
max = 0
for numar in numere:
    if numar > max:
        max = numar
print('Numarul maxim din lista este :', max)
# varianta cu sort
max = sorted(numere)[-1]
print('Numarul maxim din lista este :', max)
# 10
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_noi = []
for x in range(len(numere)):
    if numere[x] > 0:
        numere[x] = -numere[x]
        numere_noi.append(numere[x])
    else:
        numere_noi.append(numere[x])
print(numere_noi)