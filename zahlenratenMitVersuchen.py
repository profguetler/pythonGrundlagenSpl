import random
zufallszahl = random.randint(1,1001)

print("Zahlenraten - errate meine Zahl von 1 bis 1000")
versuche = 0
gewonnen = False

while gewonnen == False:
  zahl = int(input("Welche Zahl? "))
  versuche = versuche + 1
  if (zahl == zufallszahl):
    print("Gratuliere! Du hast die Zahl erraten.")
    gewonnen = True
  elif (zahl < zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist größer.")
  elif (zahl > zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist kleiner.")
    
print("Anzahl der Versuche", versuche)
