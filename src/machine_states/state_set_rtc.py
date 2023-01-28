from libs.hw_buttons import check_button_pressed
from datastructs.rtc_time import RtcTimeModel, RtcMenuModel


####################
## local function ##
####################

def count_up_sec_min_hour(data, mode):
    # Counts sec|min|hour up
    
    if mode == 'seconds':
        print("TEST: seconds ++")
        data.add_to_seconds(1)
        
    if mode == 'minutes':
        print("TEST: minutes ++")
        # increase minutes by 1
        data.add_to_minutes(1)

    if mode == 'hours':
        print("TEST: hours ++")
        # increase hours by 1
        data.add_to_hours(1)
    
    return data


##################
## Step handler ##
##################

def enter_set_rtc_state(context):
    
    hw = context["hardware"]    
    displayUpdater = context["displayUpdater"]
    rtcTimeModel = context["rtcTimeModel"]
    menu_model = context["rtcMenuModel"]
    
    mode_counter = menu_model.current_mode
    
    next_state = "Set_Rtc_State"
    
    if check_button_pressed(hw.push_button_enter):
        #TODO on ENTER button press, switch sec to minutes, minutes to hours, hours to run_state
        mode_counter = mode_counter + 1
        print("TEST: Current Set RTC Modus ")
        print(mode_counter)
        
    elif check_button_pressed(hw.push_button_add):
        # On ADD button press, count the sec|min|hour up
        
        mode = menu_model.modis[mode_counter]
        rtcTimeModel = count_up_sec_min_hour(rtcTimeModel, mode)
    
    # save mode counter to not get lost after leaving step 
    menu_model.update_mode(mode_counter)
    
    # save models 
    context["rtcMenuModel"] = menu_model
    context["rtcTimeModel"] = rtcTimeModel
   
    return (next_state, context)