import time
import random
import pandas as pd

# Seed the random number generator with the current system time
random.seed(time.time())

def generate_borehole_data(num_samples=100, depth_range=(0, 100), temp_range=(10, 30), pressure_range=(800, 1200), gamma_range=(0, 100)):
    data = []

    for _ in range(num_samples):
        depth = round(random.uniform(depth_range[0], depth_range[1]), 2)
        temperature = round(random.uniform(temp_range[0], temp_range[1]), 2)
        pressure = round(random.uniform(pressure_range[0], pressure_range[1]), 2)
        # Assume that the first layer of coal has a higher gamma radiation value
        gamma_radiation = round(random.uniform(50, 80), 2)

        data.append({'Depth': depth, 'Temperature': temperature, 'Pressure': pressure, 'GammaRadiation': gamma_radiation})

    return pd.DataFrame(data)

def find_coal_depth(borehole_data, gamma_threshold=60):
    # Find the depth at which gamma radiation exceeds the threshold
    coal_layer = borehole_data['GammaRadiation'] > gamma_threshold

    if any(coal_layer):
        coal_depth = borehole_data.loc[coal_layer, 'Depth'].iloc[0]
        return coal_depth
    else:
        return None

class DraglineOperatorSystem:
    def __init__(self):
        self.start_time_digging = None
        self.start_time_dumping = None
        self.digging_area = 0
        self.dumped_amount = 0
        self.buckets_evacuated = 0

    def start_digging(self):
        self.start_time_digging = time.time()
        print("Dragline started digging.")

    def stop_digging(self):
        elapsed_time = time.time() - self.start_time_digging
        print(f"Digging stopped. Total digging area: {self.digging_area:.2f} square meters")
        print(f"Time for digging operation: {elapsed_time:.2f} seconds")

    def start_dumping(self):
        self.start_time_dumping = time.time()
        self.buckets_evacuated += 1
        print(f"Dumping bucket #{self.buckets_evacuated}.")

    def stop_dumping(self, amount):
        elapsed_time = time.time() - self.start_time_dumping
        self.dumped_amount += amount
        print(f"Dumped {amount:.2f} cubic meters of material. Total dumped amount: {self.dumped_amount:.2f} cubic meters")
        print(f"Time for dumping operation: {elapsed_time:.2f} seconds")

    def simulate_digging_and_dumping(self, bucket_size):
        digging_area_to_simulate = random.uniform(1000, 5000)  # Random digging area between 1000 and 5000 square meters

        # Calculate the number of buckets needed
        buckets_needed = digging_area_to_simulate / bucket_size

        # Simulating digging until the desired area is reached
        while self.digging_area < digging_area_to_simulate:
            time.sleep(1)  # Simulating a 1-second interval of digging
            self.digging_area += bucket_size  # Simulated area increment
            print(f"Digging: {self.digging_area:.2f} square meters", end='\r', flush=True)

            # Check if another bucket is needed
            if self.digging_area < digging_area_to_simulate:
                remaining_area = digging_area_to_simulate - self.digging_area
                print(f"Remaining area to dig: {remaining_area:.2f} square meters", end='\r', flush=True)

        # Stop digging and calculate the area
        self.stop_digging()

        # Simulating dumping until the desired material is reached
        while self.dumped_amount < digging_area_to_simulate:
            self.start_dumping()
            time.sleep(1)  # Simulating time required for dumping operation
            self.stop_dumping(bucket_size)

        # Print the total number of buckets needed
        print(f"\nTotal number of buckets needed: {buckets_needed}")

        # Print the total time spent digging and dumping
        total_digging_time = time.time() - self.start_time_digging
        total_dumping_time = time.time() - self.start_time_dumping
        print(f"Total time spent digging: {total_digging_time:.2f} seconds")
        print(f"Total time spent dumping: {total_dumping_time:.2f} seconds")

material_to_dump = 5
bucket_size = 1000  # Size of each bucket (in square meters)

# Generate random borehole data with a higher gamma radiation value for the first layer of coal
borehole_data = generate_borehole_data()

# Find the depth at which the first layer of coal is found
coal_depth = find_coal_depth(borehole_data)

# Display the coal depth
if coal_depth is not None:
    print(f"The first layer of coal is found at a depth of {coal_depth} meters.")
else:
    print("No coal layer found based on the specified threshold.")

dragline_system = DraglineOperatorSystem()
dragline_system.start_digging()
dragline_system.simulate_digging_and_dumping(bucket_size)
