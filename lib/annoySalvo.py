description = "a module for some basic tools used to annoy Salvo"
author = "Reed Essick"

import time

from RPi import GPIO as gpio

#=================================================

gpio.setmode(gpio.BCM) ### set up GPIO using BCM numbering

#=================================================

def mplayer_cmd( song ):
    """
    defines a command string to launch mplayer
    """
    return "mplayer -noconsolecontrols %s"%(song)

#=================================================

def has_moved( pin, verbose=True ):
    """
    determines whether motion was detected via pin
    """
    input = gpio.input( pin )
    if verbose:
        print "pin=%d : %.3f"%(pin, input)
    return input ### positive -> motion detected

def wait():
    """
    determines how long we have to wait until we're allowed to mess with Salvo

    WARNING: currently just returns 0. We need to set up date-time logic to make this useful
    """
    return 0
