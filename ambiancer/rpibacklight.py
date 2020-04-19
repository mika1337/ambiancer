import time

class RpiBacklight:
    def __init__(self,path="/sys/class/backlight/rpi_backlight/brightness"):
        self._path = path

    def getBrightness(self):
        fd = open( self._path, "r" )
        value = fd.read()
        fd.close()
        return int(value)

    def setBrightness(self,value,transition=False,delay=0.05):
        if transition == False:
            fd = open( self._path, "w" )
            fd.write( "%d" % (value) )
            fd.close()

        else:
            current_value = self.getBrightness()
            if current_value > value:
                offset = -1
            else:
                offset = 1

            while current_value != value:
                current_value = current_value + offset
                self.setBrightness( current_value )
                time.sleep( delay )
