# Particle Swarm Optimization (PSO)

## Overview
This project implements the **Particle Swarm Optimization (PSO)** algorithm in Python using **SymPy, NumPy, and Matplotlib**. PSO is a heuristic optimization technique inspired by the social behavior of bird flocks and fish schools. It is widely used for solving continuous optimization problems.

## How It Works
PSO maintains a **swarm of particles**, where each particle represents a candidate solution in the search space. The movement of each particle is influenced by:
- **Personal Best Position** (*pbest*): The best position found by the particle itself.
- **Global Best Position** (*gbest*): The best position found by any particle in the swarm.

Each particle updates its velocity and position using the following equations:

### Mathematical Formulation
Let:
- \( \mathbf{x}_i^t \) be the position of particle \( i \) at iteration \( t \)
- \( \mathbf{v}_i^t \) be the velocity of particle \( i \) at iteration \( t \)
- \( \mathbf{p}_i \) be the personal best position of particle \( i \)
- \( \mathbf{g} \) be the global best position found by the swarm
- \( w \) be the inertia weight (controls exploration and exploitation)
- \( c_1, c_2 \) be acceleration coefficients (typically set to 1.492)
- \( r_1, r_2 \) be random values drawn from \( [0,1] \)

#### Velocity Update Equation:
\[
\mathbf{v}_i^{t+1} = w \mathbf{v}_i^t + c_1 r_1 (\mathbf{p}_i - \mathbf{x}_i^t) + c_2 r_2 (\mathbf{g} - \mathbf{x}_i^t)
\]

#### Position Update Equation:
\[
\mathbf{x}_i^{t+1} = \mathbf{x}_i^t + \mathbf{v}_i^{t+1}
\]

The process iterates until a stopping criterion (such as a maximum number of iterations) is met.

---
## Implementation Details
### Dependencies
Make sure you have the following Python libraries installed:
```sh
pip install sympy numpy matplotlib
```

### Code Structure
- `Particle` class: Represents a particle in the swarm.
- `sub(f, x)`: Evaluates the function at a given position.
- `contour(f, min, max)`: Generates contour plots for visualization.
- `plot2d(gbest_arr)`: Plots 2D trajectories of particles.
- `plot1d(f, min, max, gbest_arr)`: Plots function values in 1D.
- `pso(n, dim, min, max, f, max_iter)`: Runs the PSO algorithm and finds the optimal solution.

### Running the PSO Algorithm
To execute the PSO optimization, run the script and provide the following inputs:
```sh
python pso.py
```

### Example Input:
```
Enter the Dimension: 2
Enter the Function: x1**2 + x2**2  # Minimizing a quadratic function
Min: -10
Max: 10
Enter No. of Particles: 30
Enter Max Iterations: 100
```

### Expected Output
- The script prints intermediate values of positions, velocities, and fitness.
- The **best position** and **best function value** are displayed at the end.
- For 2D problems, contour plots visualize particle movement.
- A convergence plot shows the best fitness value over iterations.

### Example Output:
```
Best value: 0.0001
Best position: [0.001, 0.002]
```

---
## Visualization
- **2D Contour Plot**: Shows the movement of particles towards the optimum.
- **3D Surface Plot**: Displays the function's shape.
- **Convergence Plot**: Illustrates fitness improvement over iterations.

## Applications of PSO
- Function optimization
- Machine learning hyperparameter tuning
- Engineering design problems
- Financial modeling

## References
- Kennedy, J., & Eberhart, R. (1995). *Particle Swarm Optimization*. IEEE International Conference on Neural Networks.
- Clerc, M. (2010). *Particle Swarm Optimization*. Wiley.

## License
This project is open-source and can be used freely for educational purposes.

---
### Future Enhancements
- Implementing constraints in optimization.
- Hybrid approaches combining PSO with other optimization techniques.
- Performance tuning with adaptive parameters.

---

