import datetime
tdelta = datetime.timedelta(days=1)
tday = datetime.datetime.now()
print("Yesterday", (tday - tdelta).strftime("%x"))
print("Today:", tday.strftime("%x"))
print("Tomorrow", (tday + tdelta).strftime("%x"))