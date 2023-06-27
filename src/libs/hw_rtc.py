class RtcController:
    
    def __init__(self, hardware_instance):
        
        self.hw = hardware_instance
        pass
    
    
    def __str__(self):
        return str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))


    def update_rtc_hardware(self, data):

        # TODO pass rtc-model values to hardware rtc

        # convert values to hex format as bytearray
        #call def SetTime(self, NowTime = b'\x00\x23\x12\x28\x14\x07\x21'):

        print("Test RtcController ")
    