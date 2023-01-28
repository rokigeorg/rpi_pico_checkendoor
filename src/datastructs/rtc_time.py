class RtcTimeModel:
    '''
    Holds the data to set the time of the RTC.

    Valid values are:
    - seconds [0,59]
    - minutes [0,59]
    - hour    [0,23]

    Format:                    hh:mm:ss
    one second before midnight 23:59:59
    midnight time              00:00:00
    '''
    
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hour = 0
        
        
    def set_seconds(self, seconds):
        if seconds < 0 or seconds > 59:
            seconds = 0
        self.seconds = seconds
        
        
    def set_minutes(self, minutes):
        if minutes < 0 or minutes > 59:
            minutes = 0
            
        self.minutes = minutes


    def set_hours(self, hours):
        if hours < 0 or hours > 23:
            hours = 0
        self.hours = hours


    def add_to_seconds(self, x):
        sec = self.seconds
        self.set_seconds(sec + x)
        

    def add_to_minutes(self, x):
        minet = self.minutes
        self.set_minutes(minet + x)


    def add_to_hours(self, x):
        hour = self.hour
        self.set_hours(hour + x)


    # TODO move this to RtcController class in hw_rtc.py
    def get_binary_rtc_time():
        #creates the binary string with hex e.g. b'\x00\x23\x12\x28\x14\x07\x21'
        s = str(self.seconds) + str(self.minutes) + str(self.hour) + '00000000'
        return bytes.fromhex(s)



class RtcMenuModel:
    '''
    Holds the data for the sub-menu to set the RTC.
    '''

    def __init__(self):
        # possible modes are seconds | minutes | hours
        self.modis = ("seconds", "minutes", "hours")
        self.current_mode = 0


    def get_current_mode(self):
        return self.current_mode


    def update_mode(self, mode_index):
        # Make sure index does not over shoot modis array
        if mode_index > 2:
            mode_index = 0
        self.current_mode = mode_index
        