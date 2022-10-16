from machine import Pin, I2C, Timer

from driver.ssd1306 import SSD1306_I2C
import framebuf

#### DEFINES ######
WIDTH=128
HEIGHT=64

##### GLOBALS ####
display_g = None



def init_display(i2c):
    return SSD1306_I2C(WIDTH,HEIGHT, i2c)


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
