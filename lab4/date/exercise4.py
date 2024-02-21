import datetime
tday = datetime.datetime.now()
bday = datetime.datetime(2024, 2, 11, 18, 15, 5)
difference = tday - bday
print(int(difference.total_seconds()))