import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(1)
tomorrow=today+datetime.timedelta(1)
print("Today is ",today)
print("Yesterday was ",yesterday)
print('Tomorrow ',tomorrow)