from sympy import *
import random
import matplotlib.pyplot as plt
import numpy as np


class Particle:
    def __init__(self, dim, min, max, f):
        self.dim = dim
        self.pos = np.array([0.0 for i in range(dim)])
        self.vel = np.array([0.0 for i in range(dim)])

        for i in range(dim):
            self.pos[i] = min + (max-min)*random.random()
            self.vel[i] = min + (max-min)*random.random()

        self.fitness = sub(f, self.pos)
        self.pbest_val = self.fitness
        self.pbest = np.copy(self.pos)


def sub(f, x):
    val = []
    for i in range(len(x)):
        val.append(('x'+str(i+1), x[i]))
    return f.subs(val).evalf()


def contour(f, min, max):
    x = np.arange(min, max, (max-min)/100)
    y = np.arange(min, max, (max-min)/100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            Z[i][j] = sub(f, (X[i][j], Y[i][j]))

    return X, Y, Z


def plot2d(gbest_arr):
    global X, Y, Z

    x1 = []
    x2 = []
    for gbest in gbest_arr:
        x1.append(gbest[0])
        x2.append(gbest[1])

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(x1, x2, color='orange')
    ax.contourf(X, Y, Z)
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.plot_surface(X, Y, Z)
    plt.show()


def plot1d(f, min, max, gbest_arr):
    x = np.arange(min, max, (max-min)/100)
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = sub(f, (x[i],))

    plt.plot(x, y, color='orange')
    plt.plot(gbest_arr, [0 for i in range(len(gbest_arr))], 'o')
    plt.show()


def print_table(p, gbest):
    width = 10
    prec = 3
    for k in range(dim):
        print(f'x{k+1}'.rjust(width), end="")
    for k in range(dim):
        print(f'v{k+1}'.rjust(width), end="")
    for k in range(dim):
        print(f'pb{k+1}'.rjust(width), end="")
    print('Best'.rjust(width), end="")
    print('Fitness'.rjust(width), end="")
    print('Gbest'.rjust(width))
    for i in range(n):
        for k in range(dim):
            print(f"{p[i].pos[k]:{width}.{prec}f}", end="")
        for k in range(dim):
            print(f"{p[i].vel[k]:{width}.{prec}f}", end="")
        for k in range(dim):
            print(f"{p[i].pbest[k]:{width}.{prec}f}", end="")
        print(f"{p[i].pbest_val:{width}.{prec}f}", end="")
        print(f"{p[i].fitness:{width}.{prec}f}", end="")
        print(f"{gbest:{width}.{prec}f}")
    print('\n')


def plot_points(p, n, iter, num):
    global X, Y, Z
    x1 = np.zeros(n)
    x2 = np.zeros(n)
    for i in range(n):
        x1[i] = p[i].pos[0]
        x2[i] = p[i].pos[1]

    plt.subplot(2, 3, iter+1)
    plt.title(f'Iteration {iter*num}')
    plt.plot(x1, x2, 'o', color='black')
    plt.contourf(X, Y, Z)


def pso(n, dim, min, max, f, max_iter):

    w = 0.729
    c1 = 1.492
    c2 = 1.492

    p = np.array([Particle(dim, min, max, f) for i in range(n)])
    gbest_val_arr = []
    gbest_arr = []
    gbest = np.copy(p[0].pos)
    gbest_val = p[0].fitness

    for i in range(1, n):
        if p[i].fitness < gbest_val:
            gbest_val = p[i].fitness
            gbest = np.copy(p[i].pos)

    gbest_arr.append(gbest)
    gbest_val_arr.append(gbest_val)
    print('\n')
    print_table(p, gbest_val)
    num = max_iter//5
    iter = 0
    if dim==2 : 
        plot_points(p, n, iter, num)

    while iter < max_iter:
        for i in range(n):
            r1 = random.random()
            r2 = random.random()
            new_vel = (
                (w*p[i].vel) +
                (c1*r1*(p[i].pbest-p[i].pos)) +
                (c2*r2*(gbest-p[i].pos))
            )

            for k in range(dim):
                if new_vel[k] > min and new_vel[k] < max:
                    p[i].vel[k] = new_vel[k]
                if p[i].pos[k] + p[i].vel[k] > min and p[i].pos[k] + p[i].vel[k] < max:
                    p[i].pos[k] = p[i].pos[k] + p[i].vel[k]

            p[i].fitness = sub(f, p[i].pos)

            if p[i].fitness < p[i].pbest_val:
                p[i].pbest_val = p[i].fitness
                p[i].pbest = np.copy(p[i].pos)

            if p[i].fitness < gbest_val:
                gbest_val = p[i].fitness
                gbest = np.copy(p[i].pos)

        iter += 1
        num = max_iter//5
        if iter % (num) == 0 and dim == 2:
            plot_points(p, n, iter//num, num)
        gbest_arr.append(gbest)
        gbest_val_arr.append(gbest_val)
        print_table(p, gbest_val)

    print(f"Best value : {gbest_val}")
    print(f"Best position {gbest}")

    plt.show()
    return gbest_arr, gbest_val_arr


dim = int(input("Enter the Dimension : "))
var = ''
for i in range(dim):
    var += 'x'+str(i+1)+' '
x = symbols(var)
func = input("Enter the Function : ")
f = sympify(func)
min = float(input("Min : "))
max = float(input("Max : "))
n = int(input("Enter No.Of Particles : "))
max_iter = int(input("Enter Max Iterations : "))

X = Y = Z = None
if dim == 2:
    X, Y, Z = contour(f, min, max)

gbest_arr, gbest_val_arr = pso(n, dim, min, max, f, max_iter)

if dim == 2:
    plot2d(gbest_arr)
if dim == 1:
    plot1d(f, min, max, gbest_arr)

plt.plot(gbest_val_arr)
plt.show()
