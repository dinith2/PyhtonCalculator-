import calendar

year = 2023
month = 6

cal = calendar.monthcalendar(year, month)

print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")

for week in cal:
    for day in week:
        if day == 0:
            print("  ", end=" ")
        else:
            print(f"{day:2d}", end=" ")
    print()  