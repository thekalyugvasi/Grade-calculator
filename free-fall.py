import matplotlib.pyplot as plt
import numpy as np

def simulate_free_fall(initial_height, total_time, time_step):
    # Constants
    g = 9.8  # Acceleration due to gravity (m/s^2)

    # Initial conditions
    time = np.arange(0, total_time, time_step)
    num_steps = len(time)
    position = np.zeros(num_steps)
    velocity = np.zeros(num_steps)

    position[0] = initial_height
    velocity[0] = 0

    # Simulation loop
    for i in range(1, num_steps):
        # Update velocity and position using equations of motion
        velocity[i] = velocity[i - 1] + g * time_step
        position[i] = position[i - 1] - velocity[i - 1] * time_step - 0.5 * g * time_step**2

        # If the object hits the ground, stop the simulation
        if position[i] <= 0:
            position[i] = 0
            velocity[i] = 0
            break

    return time[:i + 1], position[:i + 1]

def plot_simulation(time, position):
    plt.plot(time, position)
    plt.title('Free Fall Simulation')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.grid(True)
    plt.show()

# Simulation parameters
initial_height = 100.0  # Initial height in meters
total_time = 20.0  # Total simulation time in seconds
time_step = 0.1  # Time step for simulation in seconds

# Run simulation
time, position = simulate_free_fall(initial_height, total_time, time_step)

# Plot the results
plot_simulation(time, position)
