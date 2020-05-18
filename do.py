import RPi.GPIO as GPIO
import spidev
import time
from enum import Enum,auto
from Pi_MCP23S17 import MCP23S17

__author__ = "pe2a"
__license__ = "GPL"


#ANALOG INPUT 
AI_1 = 0
AI_2 = 1
AI_3 = 2
AI_4 = 3

AI_5 = 4
AI_6 = 5
AI_7 = 6
AI_8 = 7

#converts digital number to voltage
def rpi_dig_vol_converter(val):
    return val*33.0/4095.0


#ANALOG INPUT START
#mcp3208 ADC

def rpi_readAI(ch):

    try:

        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  # only B11 is here
        val |= ret[1] << 3           # B10:B3
        val |= ret[2] >> 5           # MSB has B2:B0 ... need to move down to LSB

        return (val & 0x0FFF)  # ensure we are only sending 12b


    except:
        pass


#GPIO tanimlari cagiriliyor
def init():
    global mcp1
    global spi

    mcp1 = MCP23S17(ce=0)
    mcp1.open()

     #DO tanimlanmasi
    for x in range(0, 16):

        mcp1.setDirection(x, mcp1.DIR_OUTPUT)

    time.sleep(1)

    spi = spidev.SpiDev()
    spi.open(0, 1)
    spi.max_speed_hz = 7629

   
def DO_Set_High(ch):
    try:

        mcp1.digitalWrite(ch, MCP23S17.LEVEL_HIGH)
    except:
        pass
   

def DO_Set_Low(ch):
    try:


        mcp1.digitalWrite(ch, MCP23S17.LEVEL_LOW)
    except:
        pass
    
     
init()

while 1:

    DO_Set_High(8)
    time.sleep(1)
    print(rpi_readAI(7))
  
    DO_Set_Low(8)
    time.sleep(1)

 


