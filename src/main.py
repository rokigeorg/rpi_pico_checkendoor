from machine import Pin, I2C, Timer
import utime

# For debugging interrupts
import micropython
micropython.alloc_emergency_exception_buf(100)

# Load display lib
from libs.hw_display import *
from libs.hw_buttons import *

import framebuf

# Load RTC lib
from driver.ds3231 import *


######### GLOBALS #########
rtc_g = None
i2c_g = None
push_btn_enter_g = None
push_btn_add_g = None


######## FUNCTIONS ########
def init_rtc():
    return RTC(sda_pin=20, scl_pin=21)
    
def init_i2c():
    return I2C(0, scl=Pin(21), sda=Pin(20))

    
def get_time(rtc):
    rtc_time = rtc.ReadTime('time')
    print(rtc_time)


def main():    
    
    push_btn_enter_g, push_btn_add_g = init_buttons()
    print(push_btn_enter_g)

    rtc_g = init_rtc()
    i2c_g = init_i2c()
    display_g = init_display(i2c_g)
    
    display_start(display_g)
    x =0

    while True:
        check_button_pressed(push_btn_enter_g)
        check_button_pressed(push_btn_add_g)
        
        #get_time(rtc_g)
        #utime.sleep_ms(1)

main()