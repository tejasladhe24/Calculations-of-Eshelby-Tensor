import numpy as np
from sympy import *
from sympy.utilities.lambdify import lambdify
import Functions
from scipy.integrate import dblquad
from stiffness_tensor_rules import TensorTermsCombinations

'''
to find repeating terms in stiffness tensor, run command TensorTermsCombinations. Each line contains all possible 
combinations of indices of first term such that all terms have same value.
>> TensorTermsCombinations()
'''

a1 = int(input('a1 = '))
a2 = int(input('a2 = '))
a3 = int(input('a3 = '))
a = sqrt(a1**2 + a2**2 + a3**2)
phi = Symbol('phi')
theta = Symbol('theta')
x = a1 * cos(phi) * cos(theta)
y = a2 * cos(phi) * sin(theta)
z = a3 * sin(phi)
zeta = Matrix([x, y, a3 * sqrt(1 - x*x/a1*a1 - y*y/a2*a2)])

L = Functions.StiffnessTensorGenerator()
K = Functions.K_matrix(L, zeta)
N = Functions.matrix_cofactor(K)
D = Functions.det(K)
H = Functions.H_Tensor(N, zeta)

print('\nK =\n', K)
print('\nN =\n', N)
print('\nD =\n', D)
print('\nH =\n', H)

P = np.repeat(a, 81).reshape([3, 3, 3, 3])
err = np.repeat(a, 81).reshape([3, 3, 3, 3])
for l in range(3):
    for k in range(3):
        for j in range(3):
            for i in range(3):
                f = lambdify([phi, theta], exp(a1 * a2 * a3 / (2 * 3.1415 * a ** 3) * H[l][k][j][i] / D))
                ans, error = dblquad(lambda phi, theta: f(phi, theta), -pi / 2, pi / 2, lambda phi: -pi,
                                     lambda phi: pi, epsabs=0)
                print('P_' + str(i + 1) + str(j + 1) + str(k + 1) + str(l + 1) + ' = ' + str(ans))
                P[l][k][j][i] = ans
                err[l][k][j][i] = error
print('\nP =\n ', P)
print('\nerror_P =\n ', err)

S = np.einsum('lknm,nmji->lkji', L, P)
print('\nS = \n', S)

L1 = Functions.StiffnessTensorGenerator()

L_inv = Functions.tensorinv(L)
T = Functions.tensorinv(np.tensordot(np.tensordot(S, L_inv), (L1-L)) + I)  # T = [S(L^-1)(L1 - L) + I]^-1
print('\nT = \n', T)