import numpy as np

def amortissement_init(C0, t, n):
    num = C0*(t/12.)
    denum = np.power(1+(t/12.), n)-1
    val_init = num/denum

    return val_init

def amortissement(A, t, p):
    a = np.power(1+(t/12.), p-1)
    val_amort = a * A

    return val_amort

def cal_mensualite(C0, t, n):
    num = C0*(t/12.)
    denum = 1-np.power(1+(t/12.), -1*n)
    val_mens = num/denum

    return val_mens

def cal_capital_enpruntable(m, t, n):
    C_tot = m*(1-np.power(1+t/12, -1*n))
    C_tot *= 12/t
    C = cal_prix_hors_frais(C_tot)

    return C

def cal_frais_notaire(C):
    C_tot = C * 1.076
    C_tot += 1200
    return C_tot

def cal_prix_hors_frais(C_tot):
    C = C_tot - 1200
    C /= 1.076
    return C

def cal_mens_lisse(C0, mens_p1, nb_mens_p1, nb_mens_tot, t, t_p1):
    """Calcul la  mensualite pour le lisse de 2 prets de taux potentiellements
    different

    Keyword arguments:
    C0 -- Capital principal emprunte
    mens_p1 -- Montant de la mensualite de pret p1
    nb_mens_p1 -- Nombre de mensualite du pret p1
    nb_mens_tot -- Nombre de mensualite du pret principal
    t -- taux du pret principal
    t_p1 -- taux du pret p1

    return values:
    val_mens_pp1 = valeur de la mensualite du pret principale sur la periode
        nb_mens_p1
    val_mens_lisse = valeur de la mensualite lisse
    """
    val_pw_num = -1.*nb_mens_p1
    val_pw_denum = -1.*nb_mens_tot
    #if (t_p1 == 0.):
    #    num = C0 * t + mens_p1
    #else :
    num = C0 * t + mens_p1 * (1-np.power((1+t), val_pw_num))
    denum = 1-np.power(1+t, -1*nb_mens_tot)
    #print num
    #print denum
    #print C0
    #print mens_p1
    #print t_p1
    #print nb_mens_p1
    #print t
    #print nb_mens_tot
    val_mens_lisse = num/denum
    val_mens_pp1 = val_mens_lisse - mens_p1

    return val_mens_lisse, val_mens_pp1
