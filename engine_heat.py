import serial
from tkinter import *
import time

class engine_heat:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200+10+250")
        self.root.title("DHT11 Sensor Data")

        self.sensor_label = Label(self.root, text="Waiting for data...", font=("Arial", 12))
        self.sensor_label.pack(padx=20, pady=10)

        # Define the serial port and baud rate
        self.ser = serial.Serial('COM6', 9600)  # Change 'COM6' to your Arduino's serial port
        self.update_data()

    def get_sensor_data(self):
        self.ser.write(b'1')  # Send a character '1' to Arduino
        time.sleep(2)  # Wait for Arduino to process and respond
        sensor_data = self.ser.readline().decode().strip()  # Read sensor data from Arduino
        return sensor_data

    def update_data(self):
        data = self.get_sensor_data()
        if "Temperature" in data and "Humidity" in data:
            self.sensor_label.config(text=f"Sensor Data:\n{data}")
        else:
            self.sensor_label.config(text="Invalid data received")
        
        self.root.after(2000, self.update_data)  # Update data every 2 seconds

if __name__ == "__main__":
    root = Tk()
    obj = engine_heat(root)
    root.mainloop()

    # Close serial connection when GUI window is closed
    obj.ser.close()
