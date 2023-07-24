#Conversions
'''
    This module contains functions for converting
    between feet and meters'''

def to_meters(feet: float) ->float:
    ''' Accepts meters (meters argument)
        Returns feet'''
    return feet*0.3048

def to_feet(meters: float) -> float:
    ''' Accepts feet(feet argument)
        Returns meters'''
    return meters*3.28084
