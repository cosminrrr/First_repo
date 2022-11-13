#TEMA 1
"""Ex 1 Ce este o variabila?
R: O variabila este o adresa de memorie unde putem stoca anumite valori

ex. 2
Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
"""
nume='Cosmin'
varsta=29
inaltime=1.79
valoare_inaltime=True

print(nume)
print(varsta)
print(inaltime)
print(valoare_inaltime)
print(f'String {nume},Int {varsta},Float {inaltime},Bool {valoare_inaltime} ')

#ex 3 Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(f'{nume} este de tip {type(nume)}')
print(f'{varsta} este de tip {type(varsta)}')
print(f'{inaltime} este de tip {type(inaltime)}')
print(f'{valoare_inaltime} este de tip {type(valoare_inaltime)}')

# ex 4 Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia

inaltime=round(inaltime)
print(f'{inaltime} este de tip{type(inaltime)}')

#5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f'Numele meu este {nume}')
print(f'Am varsta de {varsta}')
print(f'Inaltimea mea este {inaltime} rotunjit')
print(f'Inaltime dupa masurare {valoare_inaltime}')

#tema 6 Citește de la tastatură:
#- numele;
#- prenumele.
#Afișează: 'Numele complet are x caractere'.

numele=input('Introduceti numele:')
prenumele=input('Introduceti prenumele')
print(f'Numele complet are {len(numele + prenumele)} caractere')


#ex 7
#Citește de la tastatură:
#- lungimea;
#- lățimea.
#Afișează: 'Aria dreptunghiului este x'.

lungime=int(input('Lungimea:'))
latimea=int(input('Latimea'))
print(f'Aria dreptunghiului este {lungime*latimea}')

#ex 8  Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# afișează de câte ori apare cuvântul 'the';

mystr='Coral is either the stupidest animal or the smartest rock'
print(mystr.count('the'))


#ex 9 ??

#10 Același string.
#● Folosiți un assert ca să verificați dacă acest string conține doar numere.

a='Coral is either the stupidest animale or the smartest rock'
b= a.isnumeric()
print(b)




