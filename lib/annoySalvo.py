description = "a module for some basic tools used to annoy Salvo"
author = "Reed Essick"

import time

from RPi import GPIO as gpio

#=================================================

GPIO.setmode(GPIO.BCM) ### set up GPIO using BCM numbering

#=================================================

def mplayer_cmd( song ):
    """
    defines a command string to launch mplayer
    """
    return "mplayer %s"%(song)

#=================================================

def has_moved( pin ):
    """
    determines whether Salvo has moved

    WARNING: currently just returns True
    """
    return GPIO.input(pin): ### nonzero

def wait():
    """
    determines how long we have to wait until we're allowed to mess with Salvo
    """
    return 0
