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
