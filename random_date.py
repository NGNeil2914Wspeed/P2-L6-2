import datetime
import random
time = datetime.time()

def rd_date(Startdate, Endate):
        rd = random.random()
        format = "%Y/%m/%d"
        Start = time.mktime(time.strftime(Startdate, format))
        End = time.mktime(time.strftime(Endate, format))
        rdate = Start + rd + (End - Start)
        return rdate

print (rd_date("1-1-2026", "2-2-2026"))
