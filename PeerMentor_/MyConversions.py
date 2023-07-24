#Conversions
'''Name
    Conversions
Description:
    This module contains functions for converting
    between feet and meters
Fucntions:
    to_feet(meters: float) -> float
        Accepts meters (meters argument)
        Returns feet
    to_meters(feet: float) -> float
        Accepts feet(feet argument)
        Returns meters'''
def to_meters(feet: float) ->float:
    ''' Accepts meters (meters argument)
        Returns feet'''
    return feet*0.3048
def m_to_cm(meters: float) -> float
    return meters*100
def m_to_mm(meters):
    return meters* 1000
def m_to_micro(meters):
    return meters*(10**6)
def m_to_nano(meters):
    return meters*(10**9)

def to_feet(meters):
    return meters*3.28084
def to_inch(meters):
    return meters*39.3701

def to_kpa(ksi):
    return 6894.757 * ksi
def to_ksi(kpa):
    return  0.000145038*kpa
def atm_to_kpa(atm):
    return atm* 101.325
