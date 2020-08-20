
# medioexV3

MedioexV3 is a new model of MedIOEx is retired.

Improvements:
- 16 ch Isolated digital input (0-7V False; 8-30V True)
- 16ch Transistor digital output (Each channel 500mA @ 24VDC)
- 8ch Analog Input (4ch 0-10V, 4ch 0-33V)
- More reliable power feed topology
- More reliable RS485 line 
- Aluminum case for better cooling 
- Controllable fan

# Power

Min. power Requirements: 24VDC, 1A

![Image of MedIOEx-V3](https://github.com/pe2a/medioexV3/blob/master/medioexv3.jpg)

## Digital Input 
MedioexV3 has 16ch isolated Digital Input. You must tie COM to field GND. 

| Raspberry Pi Pin   |     Physical Pin      |  BCM Adress |
|----------|:-------------:|------:|
| 12 | DI_1 | BCM18 |
| 16 |    DI_2   |   BCM23 |
| 18 | DI_3 |    BCM24 |
| 32 | DI_4 | BCM12 |
| 36 |    DI_5   |   BCM16 |
| 38 | DI_6 |   BCM20 |
| 40 | DI_7 | BCM21 |
| 37 |    DI_8   |   BCM26 |
| 35 | DI_9 |    BCM19 |
| 33 | DI_10 | BCM13 |
| 31 |    DI_11   |   BCM6 |
| 29 | DI_12 |    BCM5 |
| 15 | DI_13 | BCM22 |
| 13 |    DI_14   |   BCM27 |
| 11 | DI_15 |   BCM17 |
| 7 | DI_16 |    BCM4 |

![Image of MedIOEx-V3](https://github.com/pe2a/medioexV3/blob/master/input.JPG)

## Digital Output 
MedIOExV3 provides SPI based Digital Output Control via Transistors. 
Fan Output:

| Raspberry Pi Pin   |     Physical Pin      |  BCM Adress |
|----------|:-------------:|------:|
| 22 | DO_FAN | BCM25 |

MedIOExV3 uses MCP23S17 for digital outputs. 
SPI output:
|Physical Pin   |     SPI Address      | 
|----------|:-------------:|
| DO_1 | 0 |
| DO_2 | 1 |
| DO_3 | 2 |
| DO_4 | 3 |
| DO_5 | 4 |
| DO_6 | 5 |
| DO_7 | 6 |
| DO_8 | 7 |
| DO_9 | 15 |
| DO_10 | 14 |
| DO_11 | 13 |
| DO_12 | 12 |
| DO_13 | 11 |
| DO_14 | 10 |
| DO_15 | 9 |
| DO_16 | 8 |

![Image of MedIOEx-V3](https://github.com/pe2a/medioexV3/blob/master/output.JPG)

## Analog Input 
MedIOExV3 uses MCP3208 (12bit) for analog inputs. 

| Analog Input Channel   |     Channel Max. Voltage     |  
|----------|:-------------:|
| AI_1 | 0-10V | 
| AI_2 | 0-10V | 
| AI_3 | 0-10V | 
| AI_4 | 0-10V | 
| AI_5 | 0-33V | 
| AI_6 | 0-33V | 
| AI_7 | 0-33V |
| AI_8 | 0-33V | 


Function converts digital number to voltage for 33V channels:

```python
#converts digital number to voltage
def rpi_dig_vol_converter(val):
    return val*33.0/4095.0
```
for 10V channels:
```python
#converts digital number to voltage
def rpi_dig_vol_converter(val):
    return val*10.0/4095.0
```

## Serial Port

Raspberry Pi 3 and 4 has ttyS0 port. You can tie cable screen to Shield Terminal. 
