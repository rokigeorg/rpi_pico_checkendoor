class RtcController:
    
    def __init__(self, hardware_instance):
        
        self.hw = hardware_instance
        pass
    
    
    def __str__(self):
        return str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))


    def show(self):
        print("Test RtcController ")
    