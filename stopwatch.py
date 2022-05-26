# Ian Royer
# Stopwatch Class

import time
import sys

class StopWatch:
    
    curtime = None
    currunning = False

    def __init__(self):
        self.curtime = None

    def start(self):
        self.curtime = time.monotonic()
        self.currunning = True

    def stop(self):
        self.currunning = False

    def reset(self):
        self.curtime = None
        self.currunning = False
    
    def get_start(self):
        return self.curtime

    def get_diff(self):
        return time.monotonic() - self.curtime
    
    def isRunning(self):
        return self.currunning
    