# Automatic chickendoor with RPi pico

Work in progress


## Hardware
* Raspberry Pi Pico
* RTC Module DS3231 using I2C bus
* OLED display ssd1306 (128x64 px) using I2C bus

## Pin Connections 
Inside the libs directory, there are hardware abstaction modules:
* hw_buttons.py
* hw_display.py

There are globale variables to adjust the GPIO pins.

Default pins
* PUSH_BTN_ENTER_GPIO = 13
* PUSH_BTN_ADD_GPIO = 15
* I2C_SDA_PIN = 20
* I2C_SCL_PIN = 21
