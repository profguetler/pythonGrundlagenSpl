import random
zufallszahl = random.randint(1,101)

print("Zahlenraten - errate meine Zahl zwischen 1 und 100")
zahl = int(input("Welche Zahl? "))

gewonnen = False
while gewonnen == False:
  if (zahl == zufallszahl):
    print("Gratuliere! Du hast die Zahl erraten.")
    gewonnen = True
  elif (zahl < zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist größer.")
  elif (zahl > zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist kleiner.")
