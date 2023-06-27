from libs.hw_buttons import check_button_pressed
from libs.hw_rtc import RtcController
from datastructs.rtc_time import RtcTimeModel, RtcMenuModel, RtcMenuModes


####################
## local function ##
####################

def print_models(models):
    for model in models:
        print(model)
        print('####################')


def count_up_sec_min_hour(data, mode):
    # Counts sec|min|hour up
    
    if mode == RtcMenuModes.MODE_SECONDS:
        print("TEST: seconds ++")
        data.add_to_seconds(1)
        
    if mode == RtcMenuModes.MODE_MINUTES:
        print("TEST: minutes ++")
        # increase minutes by 1
        data.add_to_minutes(1)

    if mode == RtcMenuModes.MODE_HOURS:
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
    rtc_time_model = context["rtcTimeModel"]
    menu_model = context["rtcMenuModel"]
    rtc_controller = context["rtcController"]
    
    next_state = "Set_Rtc_State"
    
    if check_button_pressed(hw.push_button_enter):
        #TODO on ENTER button press, switch sec to minutes, minutes to hours, hours to run_state
        menu_model.next_mode()

        print("TEST: Current Set RTC Modus ")
        print(menu_model.get_current_mode())
        print_models([menu_model, rtc_time_model])
        
        displayUpdater.show_rtc_submenu_screen()
        
    elif check_button_pressed(hw.push_button_add):

        mode = menu_model.get_current_mode()
        rtc_time_model = count_up_sec_min_hour(rtc_time_model, mode)
    
        rtc_controller.update_rtc_hardware(rtc_time_model)
        
        print_models([menu_model, rtc_time_model])

        # TODO Show current rtc-model on display
        # Display update
        displayUpdater.show_rtc_submenu_screen()
    
    # save models 
    context["rtcMenuModel"] = menu_model
    context["rtcTimeModel"] = rtc_time_model
   
    return (next_state, context)