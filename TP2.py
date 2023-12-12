import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Nous ajoutons dans un table toute les données du fichier RTE_2020.csv
dataRTE=[]
with open("RTE_2020.csv",newline="") as csvfile:
	reader=csv.reader(csvfile,delimiter=",")
	for row in reader:
		dataRTE.append(row)
#On supprime la première ligne du fichier qui correspond à l'entête du fichier csv et la dernière ligne qui correspond à un petit message dans le fichier
del dataRTE[0]
del dataRTE[35136]
#Nous allons maintenant supprimé toute les lignes superflux qui n'apporte aucune donnée
compteur=0
RTE_filtre=[]
for j in range(len(dataRTE)):
	if (compteur%2)==0:
		RTE_filtre.append(dataRTE[j])
	compteur=compteur+1


#Nous allons maintenant calculer la consommation totale pour l'année 2020
conso_totale=0
conso_energiefossile=0
conso_energierenouvlable=0
for j in range(len(RTE_filtre)):
	conso_totale=conso_totale+int(RTE_filtre[j][4])
	conso_energiefossile=conso_energiefossile+int(RTE_filtre[j][7])+int(RTE_filtre[j][8])+int(RTE_filtre[j][9])+int(RTE_filtre[j][10])
	conso_energierenouvlable=conso_energierenouvlable+int(RTE_filtre[j][11])+int(RTE_filtre[j][12])+int(RTE_filtre[j][13])+int(RTE_filtre[j][14])+int(RTE_filtre[j][15])

#On va maintenant affiché les pourcentages d'utilisation de l'énergie fossiles par rapport à l'énérgie renouvlable
print(conso_energiefossile/conso_totale)
print(conso_energierenouvlable/conso_totale)

#Maintenant que nous avons calculé ce rendement pour toute l'année 2020, nous allons maintenant nous intéressé à ce rendement pour chaque jour de l'année
jour=input("choisir un jour de l'année (au format YYYY-MM-DD) ")
conso_totale_jour=0
conso_energiefossile_jour=0
conso_energierenouvlable_jour=0
for j in range(len(RTE_filtre)):
	if jour==RTE_filtre[j][2]:
		conso_totale_jour=conso_totale_jour+int(RTE_filtre[j][4])
		conso_energiefossile_jour=conso_energiefossile_jour+int(RTE_filtre[j][7])+int(RTE_filtre[j][8])+int(RTE_filtre[j][9])+int(RTE_filtre[j][10])
		conso_energierenouvlable_jour=conso_energierenouvlable_jour+int(RTE_filtre[j][11])+int(RTE_filtre[j][12])+int(RTE_filtre[j][13])+int(RTE_filtre[j][14])+int(RTE_filtre[j][15])
print("la consommation totale du "+jour+" est de: "+str(conso_totale_jour))

#Nous allons maintenant proposé à l'utilisateur de choisir entre affiché le rendement énergie fossile du jour ou celui energie renouvlables. Nous proposerons d'affiché les deux
choix=input("choisir la donnée à retourné fossile/renouvlable/autre ")
if choix=="fossile":
	print("Le rendement en énérgie fossile à la date du "+jour+" est de "+str(conso_energiefossile_jour))
elif choix=="renouvlable":
	print("Le rendement en énérgie renouvlable à la date du "+jour+" est de "+str(conso_energierenouvlable_jour))
else:
	print("Le rendement des 2 est fossile: "+str(conso_energiefossile_jour)+" renouvlable: "+str(conso_energierenouvlable_jour))

#Nous créons un affichage qui nous dit à la date choisi si l'énérgie fossile à été plus utilisé que l'énérgie renouvlable ou l'inverse
if (conso_energiefossile_jour/conso_totale_jour)>(conso_energierenouvlable_jour/conso_totale_jour):
	print("A la date du: "+jour+", le rendement en énérgie fossile à été plus élevés")
else:
	print("A la date du: "+jour+", le rendement en énérgie renouvlable à été plus élevés")
	
#On calcule la dates qui nous servira pour notre futur diagramme
dates=[]
fossile=[]
renouvlable=[]
f=0
r=0
indice=0
for j in range(len(RTE_filtre)):
	indice=30*j
	f=int(RTE_filtre[j][7])+int(RTE_filtre[j][8])+int(RTE_filtre[j][9])+int(RTE_filtre[j][10])
	r=int(RTE_filtre[j][11])+int(RTE_filtre[j][12])+int(RTE_filtre[j][13])+int(RTE_filtre[j][14])+int(RTE_filtre[j][15])
	fossile.append(f)
	renouvlable.append(r)
	dates.append(indice)
	f=0
	r=0
	
#Nous allonspour finir crée un diagramme affichant les courbes de ces consommations fossile ou renouvlable pour l'année compléte
g1= plt.plot(dates, fossile, label="fossiles")
g2= plt.plot(dates, renouvlable, label="renouvlables")
plt.ylabel("consommation énergétique")
plt.title("Comparaison consommation en énérgies fossiles et renouvlables en 2020")
plt.grid(True)
plt.legend([g1, g2], ["fossile","renouvelable"])

plt.show()
