import serial 

ser = serial.Serial('COM5')
print(ser.name)
ser.write(b'hello')
ser.close()

# with serial.Serial('COM4', 19200, timeout=1) as ser:
#     x = ser.read()
#     s = ser.read(10)
#     line = ser.readline()
#     print("")