class RtcTimeModel:
    
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hour = 0
        
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
        
    def get_binary_rtc_time():
        #creates the binary string with hex e.g. b'\x00\x23\x12\x28\x14\x07\x21'
        s = str(self.seconds) + str(self.minutes) + str(self.hour) + '00000000'
        return bytes.fromhex(s)