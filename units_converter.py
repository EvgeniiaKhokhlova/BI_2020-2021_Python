

time = int(input("Enter the time in seconds: "))

Hour = time // 3600
Hour1 = time % 3600
Minute = Hour1 // 60
Second = Hour1 % 60

print(Hour, "Hour", Minute, "Minutes", Second, "Seconds")
