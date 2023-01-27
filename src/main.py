from datastructs.state_machine import StateMachine
from machine_states.state_main_run import init_all_hardware, enter_run_state, shutdown_all_hardware
from machine_states.state_set_rtc import enter_set_rtc_state

# For debugging interrupts
import micropython
micropython.alloc_emergency_exception_buf(100)

######### GLOBALS #########


######## FUNCTIONS ########

def main():    
     
    fsm = StateMachine()
    fsm.add_state("Init_State", init_all_hardware)
    fsm.add_state("Run_State", enter_run_state)
    fsm.add_state("Set_Rtc_State", enter_set_rtc_state)
    fsm.add_state("Stop_State", shutdown_all_hardware, end_state=True)
    
    context = dict()
    
    fsm.set_start("Init_State")
    fsm.run(context)

main()
