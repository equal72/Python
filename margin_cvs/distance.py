import numpy as np



def AtoB(Ax, Ay, Bx, By):
    result = np.sqrt((Ax - Bx)**2 + (Ay - By)**2)

    return result


def Min(A, B):
    if A <= B:
        result = A
    elif A > B:
        result = B

    return result



def Max(A, B):
    if A >= B:
        result = A
    elif A < B:
        result = B

    return result
