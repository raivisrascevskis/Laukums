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
  trapecePamats1 = float(input("Ievadiet pamats1:"))
  trapezoidBase2 = float(input("Ievadiet pamats2:"))
  trapezoidHeight = float(input("Ievadiet trapeces augstumu:"))
  areaOfTrapezoid = (trapezoidBase1 + trapezoidBase2) * trapezoidHeight / 2
  print("Area of trapezoid is: " , areaOfTrapezoid)

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
  print('Figūra ir paralelograms')
if Izvele == 'Ta':
  print('Figūra ir taisnstūris')
if Izvele == 'K':
  print('Figūra ir kvadrāts')
if Izvele == 'R':
  print('Figūra ir riņķis')

