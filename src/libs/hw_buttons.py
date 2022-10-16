from machine import Pin, Timer
import utime
######### DEFINES #########
PUSH_BTN_ENTER_GPIO = 13
PUSH_BTN_ADD_GPIO = 15


###### Global Varibles ######


##### Test LED ########

# Initialisierung von GPIO25 als Ausgang
led_onboard = Pin(25, Pin.OUT, value=0)

class PushButton(object):
        
    def __init__(self, button_name, gpio):
        self.name = button_name
        self.was_pressed = False
        # PIN and set interrupt service routine
        self.pin = Pin(gpio, Pin.IN, Pin.PULL_DOWN)
        self.pin.irq(handler=self.irq_handler, trigger=Pin.IRQ_RISING)
        print("Init button " + self.name + ", pressed Flag: " + str(self.was_pressed))
    
    def is_pressed(self):
        return self.was_pressed
        
    def reset(self):
        self.was_pressed = False
    
    # IRQ handler function
    def irq_handler(self, pin):
        if pin.value():
            self.was_pressed = True
    

###### private #####

def debounce(pin):
    debounce_count = 0

    while debounce_count < 100:
        if pin.value() != True:
            debounce_count += 1
        else:
            debounce_count = 0 

###### Public function #####

def check_button_pressed(push_button):
    debounce(push_button.pin)
    
    if push_button.was_pressed:
        #led_onboard.toggle()
        print(push_button.name + ' button pressed')
        push_button.reset()
        return True
    return False
        

def init_buttons():

    enter_btn_g = PushButton("ENTER", PUSH_BTN_ENTER_GPIO)
    add_btn_g = PushButton("ADD", PUSH_BTN_ADD_GPIO)
    
    return enter_btn_g, add_btn_g
