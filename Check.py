import matplotlib.pyplot as plt
import numpy as np

# Example data
sizes = [800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600]
times = [0.0007097244262695313, 0.0011456966400146484, 0.002248668670654297, 0.005301904678344726, 0.01250617504119873, 0.027693462371826173, 0.059641695022583006, 0.14479358196258546, 0.37331461906433105, 0.7306217908859253]

# Create a scatter plot
plt.scatter(sizes, times, color='blue', label='Measured Time')

# Optionally fit a polynomial model and plot it
coeffs = np.polyfit(np.log(sizes), np.log(times), 1)  # Fit a line to the log-log plot
polynomial = np.poly1d(coeffs)
fitted_times = np.exp(polynomial(np.log(sizes)))

# Plot the fitted line
plt.plot(sizes, fitted_times, color='red', label='Fitted Line')

# Add labels and title
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Array Size')
plt.legend()

# Show the plot
plt.show()
