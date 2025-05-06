def is_valid_date(year,month,day):
	if year < 1 or month < 1 or month > 12 or day < 1:
		return False

	days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		days_in_month[1] = 29 
	return day <= days_in_month[month -1]

def increment_date(year,month,day):
	days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		days_in_month[1] = 29

	day += 1
	if day > days_in_month[month - 1]:
		day = 1
		month +=1
		if month > 12:
			month = 1
			year += 1
	return year,month,day

year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

if is_valid_date(year,month,day):
	print("valid")
	next_year, next_month, next_day = increment_date(year,month,day)
	print(f"incremented date: {next_year}-{next_month:02d}-{next_day:02d}")
else:
	print("invalid")
