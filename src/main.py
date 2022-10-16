from machine import Pin, I2C, Timer
import utime

# For debugging interrupts
import micropython
micropython.alloc_emergency_exception_buf(100)

# Load display lib
from libs.hw_hardware import Hardware, init_rtc, init_i2c
from libs.hw_display import DisplayUpdater, init_display
from libs.hw_buttons import *

import framebuf

# Load RTC lib
from driver.ds3231 import *

######### GLOBALS #########
push_btn_enter_g = None
push_btn_add_g = None


######## FUNCTIONS ########

def main():    
    
    push_btn_enter_g, push_btn_add_g = init_buttons()
    rtc = init_rtc()
    i2c = init_i2c()
    display = init_display(i2c)
    
    hw = Hardware(push_btn_enter_g, push_btn_add_g, rtc, i2c, display)
    
    displayUpdater = DisplayUpdater()
    displayUpdater.set_hw(hw)

    while True:
        
        if displayUpdater.needs_update:
            displayUpdater.update()
        elif check_button_pressed(hw.push_button_enter):
            print("TEST: Enter button")
        elif check_button_pressed(hw.push_button_add):
            print("TEST: Add button")

main()