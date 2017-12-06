## This will keep track of how much time has elapsed since a button as been pressed


import time
import msvcrt

print "This is the stopwatch. Press space to begin timing."

pressed = msvcrt.getch();

if pressed == chr(32):
    ## Begin tracking time
    start_time = time.time()
#    print "%r" % start_time
else :
    print "Press space"

print "Press space to stop timing."

pressed_again = msvcrt.getch();

if pressed_again == chr(32):
    end_time = time.time()
#    print "%r" % end_time

total_time = end_time - start_time

#print total_time
## Print out the time

print "\nTime elapsed:  %s" % (time.strftime("%H:%M:%S", time.gmtime(total_time)))
