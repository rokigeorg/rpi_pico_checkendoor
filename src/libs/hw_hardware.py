from machine import Pin, I2C, Timer
from libs.hw_display import init_display

# RTC driver module and GPIOs
from driver.ds3231 import *

I2C_SDA_PIN = 20
I2C_SCL_PIN = 21

### Init functions ###
def init_rtc():
    return RTC(sda_pin=I2C_SDA_PIN, scl_pin=I2C_SCL_PIN)
    
def init_i2c():
    return I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))

### classes ###
class Hardware(object):
    
    def __init__(self, btn_enter_instance, btn_add_instance, rtc_instance, i2c_instance, display_instance):
        self.push_button_enter = btn_enter_instance
        self.push_button_add = btn_add_instance
        self.rtc = rtc_instance
        self.i2c = i2c_instance
        self.display = display_instance