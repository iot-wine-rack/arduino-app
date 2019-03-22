#Project: IoT Wine Rack
#Authors: PJ
#Version: 0.0.1
#Date: 3/20/2019
#Changelog found in workspace
#Codebase for utilizing LEDs on rack

#Specific parts
#LEDs:
#Shift registers:

#Output scheme is based on shift register bank
#2x 8-bit shift registers daisy chained together
#3x banks of shift registers, one for each color for each LED
#e.g. 16 lights x 48 led connections

#Class for an ledRack
def ledRack(self, parameter_list):
    pass
    #Parameters of physical rack
    #xmax: Total number of wine slots in the x direction
    #ymax: Total number of wine slots in the y direction
    
    #Current status of rack
    #[Active bottle array] (BOOL)
    #[RedArray, GreenArray, BlueArray] (BOOL)

    #Current color layout for rack
    #[RedArray, GreenArray, BlueArray] (BOOL)
    
    #attached functions
    #

#Loads the shift register bank with the desired RGB layout
#Input: newState [3x16 array]
def loadRegisters(newState):
    #Confirm the physical pin outputs
    #Relevant pins: Register clock, out0-2 (act as inputs to the RGB shift registers respectively)

    #Active portion of code
    #Set RGB outputs to match value of first
    #Toggle register clock to load values
    #Repeat above two lines until all values are loaded
    return

#Takes in currently active configuration and new configuration to determine if they are different
#Input: currState [3x16 arrays for LED, from rack class, BOOL] newState [3x16 arrays for LED, from external update, BOOL]
def checkChange(currState, newState):
    #TODO directly compare nested arrays
    return

#Takes in 2 dimensional account and returns a single digit
#Row major order e.g. y increments full row, x increments location
#Input: x, y location of desired address & xmax, ymax parameters of rack
#Output: int that represents 1D location of light
#ERROR: Returns 0, not possible location
def convertXY(x, y, xmax, ymax):
    #Check to make sure x, y are in bounds
    if(x<0 or x>xmax or y<0 or y>ymax):
        return 0
    else:
        return y*xmax + x

#Takes in an integer and converts it to the right RGB on/off combinations
#Input: int representation of the color that should be displayed
#Output: [Bool,Bool,Bool] that represents RGBs on/off
#ERROR: Does not return array but returns simply 'False'
def convertColor(intColor):
    #TODO populate full colors
    #Red = 0
    #Green = 1 
    #Blue = 2
    #etc....
    if(intColor==0):
        return [True, False, False]
    elif(intColor==1):
        return [False, True, False]
    elif(intColor==1):
        return [False, False, True]
    else:
        return False