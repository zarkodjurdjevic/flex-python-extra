# Hier importeer je de os module
import os

# De huidige directory opvragen en opslaan in de variabele: werkmap
werkmap = os.getcwd()

# De letters cwd staan voor: current working directory (de huidige map!)

# Op het scherm printen
print("De huidige map is: " + werkmap)


# Zet de variabele mapnaam eerst naar een lege tekst
mapnaam = ""

# Zet de variabele lengte_mapnaam naar 0
lengte_mapnaam = 0

# Zolang de lengte_mapnaam gelijk is aan 0, blijft het script vragen om de mapnaam
while lengte_mapnaam == 0:



    # Gebruiker om de naam van de map vragen
    mapnaam = input("Welke naam wil je voor de map? ")

    # Als de lengte van mapnaam > 0 is dan maken we de map
    lengte_mapnaam = len(mapnaam)
    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
        print("Je hebt geen naam ingevoerd")

print("De map " + mapnaam + " is gemaakt.")
