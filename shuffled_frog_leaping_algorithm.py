# Shuffled Frog Leaping Algorithm      # OTML assignment

from sympy import *
import numpy as np

def sub(f, x):
    var = []
    for i in range(len(x)):
        var.append(('x'+str(i+1), x[i]))
    return f.subs(var).evalf()

class frog:
    def __init__(self, dim, domain, f):
        self.pos = np.zeros(dim)
        for i in range(dim):
            self.pos[i] = domain[i][0] + (domain[i][1]-domain[i][0])*np.random.rand()

        self.fitness = sub(f, self.pos)

    def __gt__(self, other):
        return self.fitness>other.fitness
    def __le__(self, other):
        return self.fitness<=other.fitness
    def __ge__(self, other):
        return self.fitness>=other.fitness

def local_search(memeplex, frog_g, dim, domain, f, i_max = 10):
    func_eval = 0
    for i in range(i_max):
        frog_w = np.amax(memeplex)
        frog_b = np.amin(memeplex)

        frog_w_new = frog_w.pos + (np.random.rand() * (frog_b.pos - frog_w.pos))
        frog_w_new_fitness = sub(f, frog_w_new)
        func_eval += 1

        if frog_w_new_fitness > frog_w.fitness:
            frog_w_new = frog_w.pos + (np.random.rand() * (frog_g.pos - frog_w.pos))
            frog_w_new_fitness = sub(f, frog_w_new)
            func_eval += 1

        if frog_w_new_fitness > frog_w.fitness:
            frog_w = frog(dim, domain, f)
            func_eval += 1
        else:
            frog_w.pos = frog_w_new
            frog_w.fitness = frog_w_new_fitness
            func_eval += 1
    return func_eval

def SFLA(dim, domain, f, k_max, num_frogs=50, num_memeplexes = 5, i_max = 10):
    frogs = np.array([frog(dim, domain, f) for i in range(num_frogs)])
    func_eval = num_frogs

    k = 0
    for i in range(k_max):
        np.random.shuffle(frogs)
        memeplexes = np.array_split(frogs, num_memeplexes)

        frog_g = np.amin(frogs)

        for sub_population in memeplexes:
            func_eval += local_search(sub_population, frog_g, dim, domain, f, i_max)

    best = np.amin(frogs)
    return (best.pos, best.fitness, func_eval)

def get_input():
    dim = int(input("Enter Dimension: "))
    var = ''
    for i in range(dim):
        var += 'x'+str(i+1)+' '
    x = symbols(var)
    func = input(f"Enter the Function using {x} as variables:\n")
    f = sympify(func)
    print('Input Function:', f)
    domain=[]
    print('Enter Domain')
    for i in range(dim):
        min=float(input(f"x{i+1} lower bound : "))
        max=float(input(f"x{i+1} upper bound : "))
        domain.append([min,max])

    return dim, domain, f

dim, domain, f = get_input()

optVal = SFLA(dim, domain, f, k_max = 15, num_frogs = 50, num_memeplexes=5, i_max = 10) 
# k_max is max number of iterations, num_frogs is the number of frogs, num_memeplexes is the number of sub_populations
# i_max is the number of iterations in local search
# The default values work very well

print('Minimum =', optVal[1])
print('Minimum at', optVal[0])
print('Function Evaluations:', optVal[2])