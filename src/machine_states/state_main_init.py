
def init_all_hardware():
    push_btn_enter, push_btn_add = init_buttons()
    rtc = init_rtc()
    i2c = init_i2c()
    display = init_display(i2c)

    hw = Hardware(push_btn_enter, push_btn_add, rtc, i2c, display)
    
    return hw
