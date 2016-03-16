import numpy as np
import matplotlib.pyplot as plt


#----- fonctions perso -------

from bank_utils import *


#taux_annuel = 4/100.
#capital_emprunte = 100000
#duree_tot = 20*12
taux_annuel = 4/100.
capital_emprunte = 134000
duree_tot = 16 * 12.

val_amort_init = amortissement_init(capital_emprunte, taux_annuel, duree_tot)
tab_amortissement = []
val_mensualite=cal_mensualite(capital_emprunte, taux_annuel, duree_tot)
for i in range(np.int(duree_tot)):
    tab_amortissement.append(amortissement(val_amort_init, taux_annuel, i+1))

part_interet=val_mensualite-tab_amortissement
val_interet_restant=np.sum(part_interet[108:192])
val_capital_restant=np.sum(tab_amortissement[108:192])
print val_interet_restant
print val_capital_restant

mens_7_2_5 = cal_mensualite(val_capital_restant, 1.85/100., 7*12)

print mens_7_2_5
print "gain mensuel : " + str(val_mensualite-mens_7_2_5)
print "Nb de mois gagnés : " + str((val_mensualite-mens_7_2_5)*7*12/val_mensualite)
print "Mensualite 20, 2.5, 142000 : " + str(cal_mensualite(142000, 2.5/100., 240))
# plt.figure()
# plt.plot(tab_amortissement)
# plt.plot(part_interet)
# plt.show()
print "Capital empruntable 950 : " + str(cal_capital_enpruntable(950, 2/100., 240))
duree_tot = 20
p1 = 6.5
taux_annuel = 2/100.
taux_annuel_p1 = 3.5/100.
val_mens_fin, val_mens_debut = cal_mens_lisse(cal_frais_notaire(134000), 700, p1*12, duree_tot*12,
                                              taux_annuel/12., taux_annuel_p1/12)

print "Exemple de 134 000 sur 20 ans avec un palier de 500 après " + str(p1) + " ans. début : " + str(val_mens_debut) + " Fin : " + str(val_mens_fin)
