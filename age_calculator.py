from datetime import date, datetime
from webbrowser import get


def get_dob():
    # write code here
	year=input("Enter the Year of bitrh: ")
	mounth=input("Enter the Year of bitrh: ")
	day=input("Enter the Year of bitrh: ")

	if year.isdigit() == False:
		print("Year is invaled")
		return
	elif mounth.isdigit() == False:
		print("Month is invaled")
		return
	elif day.isdigit() == False:
		print("Day is invaled")
		return
	else:
		return date(int(year),int(mounth),int(day))
	...


def get_age(dob):
    # write code here
	today = date.today()
	age = today - dob
	return age.days // 365
	...


def main():
	# write code here
	dob = get_dob()
	age = get_age(dob)
	print(f"Your age is {age} years old")

	...


if __name__ == '__main__':
    main()
