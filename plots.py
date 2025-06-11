import numpy as np
import matplotlib.pyplot as plt

# System parameters (you can adjust these)
I = 0.05         # Moment of inertia (kg*m^2)
c = 0.1          # Damping coefficient (N*m*s)
k = 0.5          # Torsional stiffness (N*m/rad)
tau_step = 0.1   # Step torque (N*m)

# Derived parameters
omega_n = np.sqrt(k / I)                  # Natural frequency (rad/s)
zeta = c / (2 * np.sqrt(k * I))           # Damping ratio
omega_d = omega_n * np.sqrt(1 - zeta**2)    # Damped natural frequency (rad/s)
theta_ss = tau_step / k                   # Steady-state angular displacement (rad)

# Time vector for transient response
t = np.linspace(0, 10, 1000)  # 0 to 10 seconds

# Transient response (underdamped response)
theta = theta_ss * (1 - np.exp(-zeta * omega_n * t) *
                    (np.cos(omega_d * t) + (zeta / np.sqrt(1 - zeta**2)) * np.sin(omega_d * t)))

# Plot transient response
plt.figure(figsize=(8, 4))
plt.plot(t, theta, 'b', linewidth=2)
plt.axhline(theta_ss, color='r', linestyle='--', label='Steady-State (θ_ss)')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement, θ (rad)')
plt.title('Transient Response with Overshoot')
plt.legend()
plt.grid(True)
plt.show()

# Calculate percent overshoot:
percent_overshoot = np.exp(-np.pi * zeta / np.sqrt(1-zeta**2)) * 100
print(f"Percent Overshoot: {percent_overshoot:.1f}%")
