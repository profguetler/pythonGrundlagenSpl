print("Taschenrechner (+/-/*/:)")
zahl1 = int(input("Bitte die 1. Zahl eingeben: "))
zahl2 = int(input("Bitte die 2. Zahl eingeben: "))
operation = input("+,-,*,: rechnen? ")

if (operation == "+"):
  summe = zahl1 + zahl2
  print("Summe = ", summe)

if (operation == "-"):
  differenz = zahl1 - zahl2
  print("Differenz = ", differenz)
  
if (operation == "*"):
  produkt = zahl1 * zahl2
  print("Produkt = ", produkt)
  
if (operation == ":"):
  if (zahl2 != 0):
    quotient = zahl1 / zahl2
  else:
    quotient = "nicht definiert!"
  print("Quotient = ", quotient)