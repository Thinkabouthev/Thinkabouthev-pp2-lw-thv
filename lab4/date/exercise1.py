import datetime
tdelta = datetime.timedelta(days=5)
tday = datetime.datetime.now()
print("Today:", tday.strftime("%x"))
print("Five days ago:", (tday - tdelta).strftime("%x"))