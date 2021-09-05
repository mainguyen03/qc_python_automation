import datetime
import time

dt = datetime.datetime
now = dt.now()
while True:
    timeLeft = dt(year = 2021, month = 12, day = 25, hour = 0, minute = 0, second = 0, microsecond = 0) - dt(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second, microsecond= now.microsecond)
    print ("Days left until Christmas: ", timeLeft)
    # time.sleep(20)