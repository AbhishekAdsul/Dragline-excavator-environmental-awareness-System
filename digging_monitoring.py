import tkinter as tk
import random
import time

class digging_monitoring:
    def __init__(self, root):
        self.root = root
        self.root.geometry("620x300+10+250")
        self.root.title("Dragline Operator System")

        self.info_label = tk.Label(root, text="Simulation Information", font=("Arial", 14, "bold"))
        self.info_label.pack(pady=10)

        self.coal_depth_label = tk.Label(root, text="", font=("Arial", 12))
        self.coal_depth_label.pack()

        self.digging_status_label = tk.Label(root, text="", font=("Arial", 12))
        self.digging_status_label.pack()

        self.dumping_status_label = tk.Label(root, text="", font=("Arial", 12))
        self.dumping_status_label.pack()

        self.total_buckets_label = tk.Label(root, text="", font=("Arial", 12))
        self.total_buckets_label.pack()

        self.total_digging_time_label = tk.Label(root, text="", font=("Arial", 12))
        self.total_digging_time_label.pack()

        self.total_dumping_time_label = tk.Label(root, text="", font=("Arial", 12))
        self.total_dumping_time_label.pack()

        self.start_time_digging = None
        self.start_time_dumping = None
        self.digging_area = 0
        self.dumped_amount = 0
        self.buckets_evacuated = 0

        self.simulate_digging_and_dumping(1000)

    def start_digging(self):
        self.start_time_digging = time.time()
        self.digging_status_label.config(text="Dragline started digging.")
        self.root.update()

    def stop_digging(self):
        elapsed_time = time.time() - self.start_time_digging
        self.digging_status_label.config(text=f"Digging stopped. Total digging area: {self.digging_area:.2f} square meters")
        self.total_digging_time_label.config(text=f"Time for digging operation: {elapsed_time:.2f} seconds")
        self.root.update()

    def start_dumping(self):
        self.start_time_dumping = time.time()
        self.buckets_evacuated += 1
        self.dumping_status_label.config(text=f"Dumping bucket #{self.buckets_evacuated}.")
        self.root.update()

    def stop_dumping(self, amount):
        elapsed_time = time.time() - self.start_time_dumping
        self.dumped_amount += amount
        self.dumping_status_label.config(text=f"Dumped {amount:.2f} cubic meters of material. Total dumped amount: {self.dumped_amount:.2f} cubic meters")
        self.total_dumping_time_label.config(text=f"Time for dumping operation: {elapsed_time:.2f} seconds")
        self.root.update()

    def simulate_digging_and_dumping(self, bucket_size):
        digging_area_to_simulate = random.uniform(1000, 5000)
        buckets_needed = digging_area_to_simulate / bucket_size

        self.start_digging()

        while self.digging_area < digging_area_to_simulate:
            time.sleep(1)
            self.digging_area += bucket_size
            self.digging_status_label.config(text=f"Digging: {self.digging_area:.2f} square meters")
            self.root.update()

            if self.digging_area < digging_area_to_simulate:
                remaining_area = digging_area_to_simulate - self.digging_area
                self.digging_status_label.config(text=f"Remaining area to dig: {remaining_area:.2f} square meters")
                self.root.update()

        self.stop_digging()

        while self.dumped_amount < digging_area_to_simulate:
            self.start_dumping()
            time.sleep(1)
            self.stop_dumping(bucket_size)

        self.total_buckets_label.config(text=f"Total number of buckets needed: {buckets_needed}")
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    obj = digging_monitoring(root)
    root.mainloop()
