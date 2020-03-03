import numpy as np

def lud_sub(m, l, u, index, dim_minus1):
    "sub function of lud"
    if index >= dim_minus1:
        u[dim_minus1, dim_minus1] = m[dim_minus1, dim_minus1]
        return l, u
    else:
        tmp = np.zeros(np.shape(m))
        u[index, index:] = m[index, index:]
        l[index+1:, index] = m[index+1: ,index]/m[index, index]
        tmp[index+1:, index+1:] = np.outer(l[index+1: ,index], u[index, index+1:])
        return lud_sub(m-tmp, l, u, index+1, dim_minus1)

# Tail recursion 
def lud(m):
    """
    LU decompsition implemented with tail recursion

    Parameters
    ----------
    m: array
        two dimensional array

    Returns
    -------
    l: array
        lower trianglar array, det(l)=det(m)
    u: array
        upper trianglar array, det(u)=1
    """
    if (type(x) == np.ndarray) and (len(np.shape(x)) == 2):
        row, col = np.shape(m)
        if row == col:
            l, u = np.eye(row), np.eye(col)
            index = 0
            dim_minus1 = row - 1
            return lud_sub(m, l, u, index, dim_minus1)
        else:
            raise ValueError("not square matrix")
    else:
        raise ValueError("matrix type or shape mismatch")
