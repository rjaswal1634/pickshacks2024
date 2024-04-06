import time
from smbus import SMBus

# LCD Address
LCD_ADDRESS = 0x3f

# Setup SMBus for I2C LCD
bus = SMBus(1)

# Function to write a single command to the I2C LCD
def write_cmd(cmd):
    bus.write_byte(LCD_ADDRESS, cmd)
    time.sleep(0.0001)

# Function to initialize the I2C LCD
def init_lcd():
    write_cmd(0x03)
    write_cmd(0x03)
    write_cmd(0x03)
    write_cmd(0x02)
    write_cmd(0x28)
    write_cmd(0x0C)
    write_cmd(0x06)
    write_cmd(0x01)

# Function to send string to I2C LCD
def send_string(text):
    for char in text:
        write_cmd(ord(char))

# Initialize the LCD
init_lcd()

# Send "Hello" to the LCD
send_string("Hello")
