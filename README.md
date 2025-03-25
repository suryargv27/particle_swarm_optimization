# Particle Swarm Optimization (PSO)

## Introduction
This repository contains an implementation of the **Particle Swarm Optimization (PSO) algorithm** in Python. The implementation supports both **1D and 2D function optimization**, visualizing the swarm's movement towards the optimal solution.

## Algorithm Explanation
**Particle Swarm Optimization (PSO)** is a population-based optimization technique inspired by the behavior of bird flocks and fish schools. It searches for the optimal solution by iteratively updating the positions and velocities of particles in a search space.

### Mathematical Formulation
Let:
- $\mathbf{x}_i^t$ be the position of particle $i$ at iteration $t$.
- $\mathbf{v}_i^t$ be the velocity of particle $i$ at iteration $t$.
- $\mathbf{p}_i$ be the best position found by particle $i$ (personal best).
- $\mathbf{g}$ be the global best position found by any particle in the swarm.

The velocity and position update rules are:

$$
\mathbf{v}_i^{t+1} = w \mathbf{v}_i^t + c_1 r_1 (\mathbf{p}_i - \mathbf{x}_i^t) + c_2 r_2 (\mathbf{g} - \mathbf{x}_i^t)
$$

$$
\mathbf{x}_i^{t+1} = \mathbf{x}_i^t + \mathbf{v}_i^{t+1}
$$

where:
- $w$ is the inertia weight (controls exploration vs. exploitation).
- $c_1, c_2$ are acceleration coefficients (cognitive and social factors).
- $r_1, r_2 \sim U(0,1)$ are random numbers sampled from a uniform distribution.

## Features
- Works for **any dimension (1D, 2D, etc.)**
- **Graphical visualization** for 1D and 2D functions
- Configurable number of **particles, iterations, and bounds**
- Contour plots and trajectory visualization for 2D optimization problems

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/particle-swarm-optimization.git
cd particle-swarm-optimization
```

Install dependencies:
```bash
pip install numpy sympy matplotlib
```

## Usage
Run the script:
```bash
python pso.py
```

### Input Parameters
When prompted, enter the following details:
- **Dimension**: Number of dimensions (1 or 2 for visualization)
- **Function**: Mathematical function to optimize (e.g., `x1**2 + x2**2`)
- **Min & Max**: Search space boundaries
- **Number of Particles**: Number of swarm particles
- **Max Iterations**: Number of iterations to run

### Example Input
```
Enter the Dimension: 2
Enter the Function: x1**2 + x2**2
Min: -10
Max: 10
Enter No. of Particles: 30
Enter Max Iterations: 100
```

## Visualization
### 2D Example
The contour plot and swarm movement will be displayed:
![PSO Contour Plot](docs/pso_contour.png)

### 1D Example
The function curve and best positions will be shown:
![PSO 1D Plot](docs/pso_1d.png)

## License
This project is licensed under the MIT License.

