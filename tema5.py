#1. Functie care sa calculeze si sa returneze suma a 2 numere
#prima varianta
def suma(a,b):
    print(f'suma este {a+b}')

suma(2,5)
#a doua varianta
def suma(a,b):
    return a+b

print(suma(10,5))



# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def par_impar(numar):
   if numar%2==0:
      return True
   else:
       return False
x= par_impar(5)
print('Valoarea afirmatiei este:',x)

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
#
def lungime(nume):
    a=len(nume)
    return a

b=lungime('Rusu Constantin')
print('Numarul total de caractere: ', b)




# 4. Functie care returneaza aria dreptunghiului

def aria_dreptunghi(a,b):
    aria = a * b
    return aria
x=aria_dreptunghi(7,9)
print('Aria dreptunghiului este', x)

# 5. Functie care returneaza aria cercului
#
PI=  3.14159

def aria_cercului(raza):
    return PI*raza**2

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
#
def chr_in_string(a,string):
    for i in range(len(string)):
        if a==string[i]:
          return True
        else :
          return False
x=chr_in_string('a','alfabet')
print('Valoarea afirmatiei este:',x)


# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y

def my_function(string):
    x = 0
    y = 0
    for i in range(len(string)):
         if string[i].islower():
            x=x+1
         elif string[i].isupper():
            y=y+1
         else:
             pass
    print('Numarul de caractere lower case este:', x)
    print('Numarul de caractere upper case este :', y)
my_function('Ana are multe mere ')




# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
#

def pozitiv(list):
    list_poz=[]
    for i in range(len(list)):
        if list[i]>=0:
            list_poz.append(list[i])
    return list_poz
x=pozitiv([-1,2,-10,3,-9,4,5,10,23])
print('Lista cu numere pozitive este:', x)


# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
#  Numerele sunt egale.

def comparatii(a,b):
    if a==b:
        print('Numerele sunt egale')
    elif a>b:
        print(f'{a} este mai maare decat{b}')
    else:
        print(f'{b} este mai mare decat {a}')

    comparatii(4,5)

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

