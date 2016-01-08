import numpy as np
import matplotlib.pyplot as plt


#----- fonctions perso -------

from bank_utils import *


#taux_annuel = 4/100.
#capital_emprunte = 100000
#duree_tot = 20*12
taux_annuel = 4/100.
capital_emprunte = 116519
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

mens_7_2_5 = cal_mensualite(val_capital_restant, 2.5/100., 7*12)

print mens_7_2_5
print "gain mensuel : " + str(val_mensualite-mens_7_2_5)
print "Nb de mois gagnés : " + str((val_mensualite-mens_7_2_5)*7*12/val_mensualite)
plt.figure()
plt.plot(tab_amortissement)
plt.plot(part_interet)
plt.show()


