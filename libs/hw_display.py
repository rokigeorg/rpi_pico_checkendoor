from machine import Pin, I2C, Timer

from driver.ssd1306 import SSD1306_I2C

#### DEFINES ######
WIDTH=128
HEIGHT=64

##### GLOBALS ####
display_g = None



def init_display(i2c):
    return SSD1306_I2C(WIDTH,HEIGHT, i2c)


def display_start(display):
    display.fill(0)
    display.fill_rect(0, 0, 32, 32, 1)
    display.fill_rect(2, 2, 28, 28, 0)
    display.fill_rect(11, 13, 12, 18, 1)
    display.text('Klappen-Ctl', 40, 0, 1)
    display.text('...........', 40, 12, 1)
    display.text('Menu', 40, 24, 1)
    display.show()
