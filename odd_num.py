"""
    A simple python program to tell when the minutes
    in the time is odd at a randow secinds interval

"""

import random
import time
from datetime import datetime

odds = []

for i in range(1, 60, 2):
    odds.append(i)

while True:
    try:
        right_this_minute = datetime.today().minute
        wait_time = random.randint(1, 60)
        curr_time_unit = 'seconds'

        if right_this_minute in odds:
            print("This minute seems a little odd. Next wait time:", wait_time, curr_time_unit)
        else:
            print('Not an odd minute. Next wait time:', wait_time, curr_time_unit)
        time.sleep(wait_time)
    except:
        print('Error occured!')

