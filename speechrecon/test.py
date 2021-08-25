import sys
import datetime

time = datetime.datetime.now()

Output = "Hi %s current time is %s" % (sys.argv[1],time)

print(Output)