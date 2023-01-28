# Load display lib
from libs.hw_hardware import Hardware, init_rtc, init_i2c
from libs.hw_display import DisplayUpdater, init_display
from libs.hw_buttons import init_buttons, check_button_pressed
from datastructs.rtc_time import RtcTimeModel, RtcMenuModel

def init_all_hardware(context):
    push_btn_enter, push_btn_add = init_buttons()
    rtc = init_rtc()
    i2c = init_i2c()
    display = init_display(i2c)

    hw = Hardware(push_btn_enter, push_btn_add, rtc, i2c, display)
    
    displayUpdater = DisplayUpdater()
    displayUpdater.set_hw(hw)
    
    context["hardware"] = hw
    context["displayUpdater"] = displayUpdater
    context["rtcTimeModel"] = RtcTimeModel()
    context["rtcMenuModel"] = RtcMenuModel()
    
    next_state = "Run_State"
    return (next_state, context)


def enter_run_state(context):

    hw = context["hardware"]
    displayUpdater = context["displayUpdater"]
    
    next_state = "Run_State"
    
    if displayUpdater.needs_update:
        displayUpdater.update()
        print("********************")
    elif check_button_pressed(hw.push_button_enter):
        print("TEST: Enter button")
        #hw.set_rtc()
        next_state = "Set_Rtc_State"
        
    elif check_button_pressed(hw.push_button_add):
        print("TEST: Add button")
        #next_state = "Stop_State"
    
    return (next_state, context)


def shutdown_all_hardware(context):
    print("Done...")