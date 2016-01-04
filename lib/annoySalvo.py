description = "a module for some basic tools used to annoy Salvo"
author = "Reed Essick"

import time
#from RPi import GPIO as gpio

#=================================================

def mplayer_cmd( song ):
    """
    defines a command string to launch mplayer
    """
    return "mplayer %s"%(song)

#=================================================

def has_moved():
    """
    determines whether Salvo has moved

    WARNING: currently just returns True
    """
    return True

def wait():
    """
    determines how long we have to wait until we're allowed to mess with Salvo
    """
    return 0
