from libs.hw_buttons import check_button_pressed
from datastructs.rtc_time import RtcTimeModel

def enter_set_rtc_state(context):
    
    hw = context["hardware"]    
    displayUpdater = context["displayUpdater"]
    rtcTimeModel = context["rtcTimeModel"]
    
    idx = rtcTimeModel.current_mode
    
    next_state = "Set_Rtc_State"
    
    if check_button_pressed(hw.push_button_enter):
        #TODO on ENTER button press, switch sec to minutes, minutes to hours, hours to run_state
        idx = idx + 1
        print("TEST: Current Set RTC Modus ")
        print(idx)
        
    elif check_button_pressed(hw.push_button_add):
        #TODO on ADD button press, count the sec|min|hour up
        
        if rtcTimeModel.modis[idx] == 'seconds':
            print("TEST: seconds ++")
        if rtcTimeModel.modis[idx] == 'minutes':
            print("TEST: minutes ++")
        if rtcTimeModel.modis[idx] == 'hours':
            print("TEST: hours ++")
            next_state = "Set_Rtc_State"
            
    rtcTimeModel.update_mode(idx)
    context["rtcTimeModel"] = rtcTimeModel
   
    return (next_state, context)