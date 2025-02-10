import datetime
print(dir(datetime))

from datetime import datetime
import pytz
now=datetime(2026,10,1,20,10,5)
now.strftime("%d/%m/%Y,%H:%M:%S")
now = datetime.now(pytz.timezone('US/Eastern'))
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
second=now.second
print(day,month,year,hour,minute,second)

print(f"day={day},month={month},year={year},hour={hour},minute={minute},second={second}")
