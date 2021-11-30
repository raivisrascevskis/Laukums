def trijsturis():
  print('Figūra ir trijstūris')
  a = float(input('Ievadiet pirmo malu: '))  
  b = float(input('Ievadiet otro malu: '))  
  c = float(input('Ievadiet trešo malu: '))  
  s = (a + b + c) / 2 ;
  area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
  print('Trijstūra laukums ir %0.2f' %area)   

def trapece():
  print('Figūra ir trapece')
  trapecesPamats1 = float(input("Ievadiet pamats1:"))
  trapecesPamats2 = float(input("Ievadiet pamats2:"))
  trapecesAugstums = float(input("Ievadiet trapeces augstumu:"))
  trapecesLaukums = (trapecesPamats1 + trapecesPamats2) * trapecesAugstums / 2
  print("Trapeces laukums ir: " , trapecesLaukums)

def taisnsturis():
 print('Figūra ir taisnstūris')
 l = float(input('Ieavadiet taisnstūra garumu: '))
 b = float(input('Ievadiet taisnstūra platumu: '))
 Area = l * b
 print("Taisnstūra laukums ir: %.2f" %Area)

def kvadrats():
 print('Figūra ir kvadrāts')
 side = int(input("Ievadiet malas garumus:"))
 Area = side*side
 print("Kvadrāta laukums ir="+str(Area))
def rinkis():
 print('Figūra ir riņķis')
 PI = 3.14
 r = float(input("Ievadiet riņķa rādiusu: "))
 area = PI * r * r
 print("Rinķa laukums ir %.2f" %area) 
def paralelograms():
 print("Figūra ir paralelograms")
 pamats = float(input('Ievadiet pamata garumu: '))
 augstums = float(input('Ievadiet augstuma garumu: '))
 laukums = pamats * augstums
 print("Laukums ir: ", laukums)





print('Programma pieprasa figūras elementus un aprēķina to lakumu.')
print('Nospiediet burtu:')
print('T   - ja figura trijstūris')
print('Tr  - ja figūra trapece')
print('P   - ja figūra paralelograms')
print('Ta  - ja figūra taisnstūris')
print('K   - ja figūra kvadrāts')
print('R   - ja figūra riņķis')
print('____________________')

Izvele = input()
if Izvele == 'T':
  trijsturis()
  
 
if Izvele == 'Tr':
  trapece()

if Izvele == 'P':
  paralelograms()

if Izvele == 'Ta':
  taisnsturis()


if Izvele == 'K':
  kvadrats()
 
if Izvele == 'R':
  rinkis()

