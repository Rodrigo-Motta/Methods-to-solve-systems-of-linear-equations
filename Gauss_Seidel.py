import numpy as np

def Gauss_Sindel(A,b,x,epsilon):
    print('---------- Gauss-Sindel Method ----------')
    condition = False
    solution = []
    diff = [None]
    while condition == False:
        x_copy = np.copy(x)
        solution.append(x_copy)
        for i in range(len(A[:])):
            x[i] = b[i]
            for j in range(len(b[:])):
                if i != j:
                    x[i] -= A[i,:][j]*x[j]
            x[i] = x[i]/A[i,i]
        
        diff.append(np.max(abs(x - x_copy)))
        if np.max(abs(x - x_copy)) < epsilon:
            condition = True
        else:
            condition = False
            
    solution.append(x)
    diff = np.array(diff)
    solution = np.array(solution)
    return x,solution


# example
a1 = np.float64([[10,-7,0],[0,2.5,5],[0,-0.001,6]])
b1 = np.float64([7,2.5,6.001])
x = [0.5,1.1,1.1]
epsilon = 0.0001

gauss = Gauss_Sindel(a1,b1,x,epsilon)
print('Solutions: {}'.format(gauss[0]))
print('Iterations: {}'.format(gauss[1]))




