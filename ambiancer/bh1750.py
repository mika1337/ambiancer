import smbus
import time


class BH1750:
    OP_POWER_DOWN = 0x01
    OP_POWER_ON   = 0x01
    OP_RESET      = 0x07

    OP_CONT_HRES_MODE  = 0x10
    OP_1TIME_HRES_MODE = 0x20

    def __init__(self, i2c_bus, address=0x23):
        self._bus = smbus.SMBus(i2c_bus)
        self._address = 0x23

    def stop(self):
        self._bus.write_byte( self._address, self.OP_POWER_DOWN )

    def _convertRawToLux( self, raw_value ):
        return (raw_value[1] + raw_value[0]*256) / 1.2

    def read(self):
        self._bus.write_byte( self._address, self.OP_1TIME_HRES_MODE )

        time.sleep(0.180)

        raw_value = self._bus.read_i2c_block_data( self._address, 0 )
        lux = self._convertRawToLux( raw_value )
        return lux
