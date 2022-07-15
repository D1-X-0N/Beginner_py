sum_sec = int(input("Введите время в секундах: "))

time_hours = sum_sec // 3600
time_minutes = (sum_sec - time_hours * 3600) // 60
time_sec = (sum_sec - time_hours * 3600) % 60

if time_hours < 10:
    time_hours = "0" + str(time_hours)
if time_minutes < 10:
    time_minutes = "0" + str(time_minutes)
if time_sec < 10:
    time_sec = "0" + str(time_sec)

print(f"{time_hours}:{time_minutes}:{time_sec}")
