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

I2C_SDA_PIN = 20
I2C_SCL_PIN = 21

######### GLOBALS #########
rtc_g = None
i2c_g = None
push_btn_enter_g = None
push_btn_add_g = None


class Hardware(object):
    
    def __init__(self, btn_enter_instance, btn_add_instance, rtc_instance, i2c_instance, display_instance):
        self.push_button_enter = btn_enter_instance
        self.push_button_add = btn_add_instance
        self.rtc = rtc_instance
        self.i2c = i2c_instance
        self.display = display_instance
        
        
class DisplayUpdater(object, Timer):
    
    def __init__(self):
        self.hw = None
        self.needs_update = False
        
        self.timer = Timer(mode=Timer.PERIODIC, period=1000, callback=self.on_timer_irq ) # periodic every 1 sec
        print(self.timer)

    def set_hw(self, hardware_instance):
        self.hw = hardware_instance
        
    def on_timer_irq(self,timer):
        self.needs_update = True
        
    def show_menu_screen(self, hh_mm_ss):        
        self.hw.display.fill(0)
        self.hw.display.fill_rect(0, 0, 32, 32, 1)
        self.hw.display.fill_rect(2, 2, 28, 28, 0)
        self.hw.display.fill_rect(11, 13, 12, 18, 1)
        self.hw.display.text('Klappen-Ctl', 40, 0, 1)
        self.hw.display.text('...........', 40, 12, 1)
        self.hw.display.text('Menu', 40, 24, 1)
        self.hw.display.text('...................', 0, 34, 1)
        self.hw.display.text(str(hh_mm_ss), 23, 44, 1)
        self.hw.display.show()
    
    def update(self):
        rtc_time = self.hw.rtc.ReadTime('time')
        self.show_menu_screen(rtc_time)
        self.needs_update = False
        

######## FUNCTIONS ########
def init_rtc():
    return RTC(sda_pin=I2C_SDA_PIN, scl_pin=I2C_SCL_PIN)
    
def init_i2c():
    return I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))

    
def get_time(rtc):
    rtc_time = rtc.ReadTime('time')
    print(rtc_time)
    

def main():    
    
    push_btn_enter_g, push_btn_add_g = init_buttons()
    rtc_g = init_rtc()
    i2c_g = init_i2c()
    display_g = init_display(i2c_g)
    
    hw = Hardware(push_btn_enter_g, push_btn_add_g, rtc_g, i2c_g, display_g)
    
    displayUpdater = DisplayUpdater()
    displayUpdater.set_hw(hw)
    display_start(hw.display)

    while True:
        check_button_pressed(push_btn_enter_g)
        check_button_pressed(push_btn_add_g)
        
        if displayUpdater.needs_update:
            displayUpdater.update()            
        

main()