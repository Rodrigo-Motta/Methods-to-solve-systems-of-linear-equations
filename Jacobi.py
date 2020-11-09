import numpy as np

def Jacobi(A,b,x,epsilon):
    print('---------- Jacobi Method ----------')
    '''
    epsilon is the precision desire.
    x is the initial guess.
    '''
    
    condition = False
    x_copy = np.copy(x)
    solution = []
    diff = [None]

    while condition == False:
        x = np.copy(x_copy)
        solution.append(x)
        for i in range(len(A[:])):
            x_copy[i] = b[i]
            for j in range(len(b[:])):
                if i != j:
                    x_copy[i] -= A[i,:][j]*x[j]
            x_copy[i] = x_copy[i]/A[i,i]

        
        diff.append(np.max(abs(x - x_copy)))
        if np.max(abs(x - x_copy)) < epsilon:
            condition = True
        else:
            condition = False
    solution.append(x_copy)
    diff = np.array(diff)
    solution = np.array(solution)
    return x,solution
    

# example
a1 = np.float64([[10,-7,0],[0,2.5,5],[0,-0.001,6]])
b1 = np.float64([7,2.5,6.001])
x = [0.5,1.1,1.1]
epsilon = 0.0001

jaco = Jacobi(a1,b1,x,epsilon)
print('Solution: {}'.format(jaco[0]))
print('Iterations: {}'.format(jaco[1]))





