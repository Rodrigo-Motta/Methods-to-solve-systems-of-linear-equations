import numpy as np

def partial_pivoting(A,b):
    print('---------- Partial Pivoting ----------')
    copy_A = np.copy(A)
    copy_b = np.copy(b)
    print(matrix_print(copy_A,copy_b))
    
    for j in range(0,len(A[:]-1)):
    
        row_max = np.argmax(copy_A[j:,j])
        
        copy2_A = np.copy(copy_A)
        copy2_b = np.copy(copy_b)
        copy_A[row_max + j,:] = copy2_A[j,:]
        copy_A[j,:] = copy2_A[row_max +j,:]
        copy_b[row_max+j] = copy2_b[j]
        copy_b[j] = copy2_b[row_max + j]
        
        if row_max + j != j:
            print(matrix_print(copy_A,copy_b))
    return copy_A,copy_b


def matrix_print(A,b):
    nrow = len(A[:])
    ncol = len(A[:])
    matriz= A
    matriz_b = b
    
    s = ""
    for i in range(0,nrow):
        for j in range(0,ncol):
            if j == (ncol-1) and matriz[i][j] >= 10:
                s += "{} |{} ".format(matriz[i][j],matriz_b[i])
            if j != (ncol-1) and matriz[i][j] >= 10:
                s += "{}, ".format(matriz[i][j])
            if j == (ncol-1) and matriz[i][j] < 10:
                s += " {} | {}".format(matriz[i][j],matriz_b[i])
            if j!= (ncol-1) and matriz[i][j] < 10:
                s += " {}, ".format(matriz[i][j])
        s += "\n"
    return s


def elimination(A,b):
    print('---------- Gauss Elimination ----------')
    copy_A = np.copy(A)
    copy_b = np.copy(b)
    print(matrix_print(copy_A,copy_b))

    for i in range(1,len(A)):
        for j in range(0,i):
            if copy_A[i,j] != 0:
                copy2_A = np.copy(copy_A)
                copy2_b = np.copy(copy_b)
                
                copy_A[i,:] = (copy2_A[i,:]/copy2_A[i,j])*copy2_A[j,j] - copy2_A[j,:]
                copy_b[i] = (copy2_b[i]/copy2_A[i,j])*copy2_A[j,j] - copy2_b[j]
                print(matrix_print(copy_A,copy_b))

    return copy_A, copy_b


def back_substitution(A,b):
    solution = np.zeros(len(b))
    for i in range(len(A) -1,-1,-1):
        term = b[i]
        for j in range(len(A[:]) -1 ,i,-1):
            term -= A[i,j]*solution[j]
        solution[i] = term/A[i,i]
    return solution


def Gauss(A,b):
    pivot = partial_pivoting(a,b)
    elimi = elimination(pivot[0],pivot[1])
    return back_substitution(elimi[0],elimi[1])
    
# example

a = np.float64([[0, 5, -1],[13,0,1],[1,-1,-1]])
b = np.float64([4,15,0])


gauss = Gauss(a,b)
print('Solution:{} \n'.format(gauss))



