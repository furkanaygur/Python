from datetime import datetime

now = datetime.now()

print(" Date : ", now.year, now.month, now.day)

print(" Clock : ", now.hour, now.minute, "\n")

# ***************** ctime ******************
print(datetime.ctime(now))
# ***************** strftime ******************
print(datetime.strftime(now, '%Y'))
print(datetime.strftime(now, '%X'))
print(datetime.strftime(now, '%d'))
print(datetime.strftime(now, '%A'))
print(datetime.strftime(now, '%B'))

print("\n", datetime.strftime(now, '%Y %B %d'))

# ****************************************************

d = "28 September 2020"
day, month, year = d.split()
print(day, month, year)

d2 = "28 September 2020 hour 22:07:12"

result = datetime.strptime(d2, '%d %B %Y hour %H:%M:%S')
print(result)
print(result.year)

# ********************************************************

birtday = datetime(1998, 8, 2)
print(birtday)

result = datetime.timestamp(birtday)  # second
print(result)

result = datetime.fromtimestamp(result)  # from second to datetime
print(result)

result = now - birtday  # timedelta
print(result)

days = result.days
print(days)


from datetime import timedelta

addtime = result + timedelta(days=30)
print(addtime)
removetime = result - timedelta(days=30)
print(removetime)