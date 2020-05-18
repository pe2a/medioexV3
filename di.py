import RPi.GPIO as GPIO
import time

#medioexV3

__author__ = "pe2a"
__license__ = "GPL"

#GLOBAL VARIABLES DIGITAL INPUT

DI_1 = 18 #pin1
DI_2 = 23
DI_3 = 24
DI_4 = 12

DI_5 = 16
DI_6 = 20
DI_7 = 21
DI_8 = 26

DI_9 = 19 
DI_10 = 13 
DI_11 = 6 
DI_12 = 5 

DI_13 = 22
DI_14 = 27 
DI_15 = 17 
DI_16 = 4 



def __myGPIOInit__():

    #init function
    GPIO.setmode(GPIO.BCM) #bcm library
    #for digital inputs
    
    #DIGITAL INPUT
    GPIO.setup(DI_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(DI_5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(DI_9,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(DI_13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_14,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(DI_16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


  
    GPIO.setwarnings(False)
    
__myGPIOInit__()


#Digital Input Query
def getDIVal(ch):

    if GPIO.input(ch):
        return True
    else:
        return False

counter  = 0
while 1:
    #counter+=1
    print(getDIVal(DI_13))
    print(getDIVal(DI_14))
    print(getDIVal(DI_15))
    print(getDIVal(DI_16))

    print("\n")

    




    time.sleep(0.3)
    

 


