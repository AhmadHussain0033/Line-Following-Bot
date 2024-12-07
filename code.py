import math

# Constants
ROBOT_SPEED_M_PER_HR = 8000  # Speed in meters/hour

# Function to simulate normal spiral traversal
def normal_spiral_traversal(num_layers, step_size):
    total_distance = 0
    for i in range(num_layers):
        # Distance covered in each spiral arm
        total_distance += step_size * (i + 1)
    return total_distance

# Function to simulate Golden Spiral traversal
def golden_spiral_traversal(num_layers, scaling_factor_c, scaling_factor_b):
    total_distance = 0
    for i in range(num_layers):
        # Golden Spiral step size decreases according to Golden Ratio properties
        step_size = scaling_factor_c * math.e**(scaling_factor_b * i)
        total_distance += step_size
    return total_distance

# Function to calculate the time required to traverse a given distance
def calculate_traversal_time(distance):
    return distance / ROBOT_SPEED_M_PER_HR

# Main Function
def main():
    # Parameters
    num_layers = 50  # Number of spiral layers
    step_size = 2   # Step size in meters for normal spiral
    scaling_factor_c = 1.0  # Scaling constant for Golden Spiral
    scaling_factor_b = 0.1  # Decreasing spacing according to Golden Ratio

    # Normal Spiral Traversal
    normal_distance = normal_spiral_traversal(num_layers, step_size)
    normal_time_hr = calculate_traversal_time(normal_distance)
    normal_time_minutes = normal_time_hr * 60

    print(f"Normal Spiral Traversal:")
    print(f"Total Distance: {normal_distance} meters")
    print(f"Time Required: {normal_time_minutes:.2f} minutes\n")

    # Golden Spiral Traversal
    golden_distance = golden_spiral_traversal(num_layers, scaling_factor_c, scaling_factor_b)
    golden_time_hr = calculate_traversal_time(golden_distance)
    golden_time_minutes = golden_time_hr * 60

    print(f"Golden Spiral Traversal:")
    print(f"Total Distance: {golden_distance:.2f} meters")
    print(f"Time Required: {golden_time_minutes:.2f} minutes")


# Run main
main()
