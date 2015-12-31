description = "a module for some basic tools used to annoy Salvo"
author = "Reed Essick"

from RPi import GPIO as gpio

#=================================================

def mplayer_cmd( song ):
    """
    defines a command string to launch mplayer
    """
    return "mplayer %s"%(song)
