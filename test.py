import serial

# Define the serial port and baud rate
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change '/dev/ttyUSB0' to your serial port

while True:
    if ser.in_waiting > 0:
        arduino_data = ser.readline().decode('utf-8').rstrip()
        print(arduino_data)  # Print the received data
