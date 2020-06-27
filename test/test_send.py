import serial


ARDUINO_DEV = "/dev/cu.usbmodem14A01"


arduino = serial.Serial(ARDUINO_DEV, 9600)

print(arduino.readline())
print(arduino.readline())

while True:
    can_msg = arduino.readline()
    print(can_msg)

