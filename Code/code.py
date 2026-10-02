import board
import digitalio
import pwmio
import sys
import time
import supervisor  # Essential for non-blocking serial
from adafruit_motor import servo

# --- Configuration ---
BUTTON_PIN = board.D2  
SERVO_PIN = board.D7  

# 1. Setup Button (D2 to GND)
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP 

# 2. Setup Servo (D7)
pwm = pwmio.PWMOut(SERVO_PIN, duty_cycle=2 ** 15, frequency=50)
shutter_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

# State Variables
is_open = False
last_button_state = True
input_buffer = ""

def move_shutter(status):
    global is_open
    if status == "open":
        print(">> Opening Shutter to 120")
        shutter_servo.angle = 120
        is_open = True
    elif status == "close":
        print(">> Closing Shutter to 30")
        shutter_servo.angle = 30
        is_open = False

# Initialize
shutter_servo.angle = 30
print("--- System Ready ---")
print("Button is ACTIVE. Serial 'open'/'close' is ACTIVE.")

while True:
    # --- 1. Physical Button Logic (Always checked) ---
    current_button_state = button.value
    if current_button_state != last_button_state:
        if not current_button_state: # Pressed
            if is_open:
                move_shutter("close")
            else:
                move_shutter("open")
        time.sleep(0.05) # Debounce
        last_button_state = current_button_state

    # --- 2. Non-Blocking Serial Logic ---
    # This check prevents the code from 'sticking'
    if supervisor.runtime.serial_bytes_available:
        char = sys.stdin.read(1)
        if char == "\n" or char == "\r":
            command = input_buffer.strip().lower()
            if command == "open":
                move_shutter("open")
            elif command == "close":
                move_shutter("close")
            input_buffer = "" # Reset buffer
        else:
            input_buffer += char