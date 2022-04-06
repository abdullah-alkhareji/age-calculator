from datetime import date, datetime
from webbrowser import get


def get_dob():
    # write code here
	year=input("Enter the Year of bitrh: ")
	mounth=input("Enter the Mounth of bitrh: ")
	day=input("Enter the Day of bitrh: ")

	if year.isdigit() == False or day.isdigit() == False or mounth.isdigit() == False:
		print("date in invalid")
		return
	else:
		return date(int(year),int(mounth),int(day))
	...


def get_age(dob):
    # write code here
	today = date.today()
	age = today - dob
	return int(age.days // 365)
	...


def main():
	# write code here
	dob = get_dob()
	if dob == None:
		return
	else:
		age = get_age(dob)
		if age < 0:
			print("You will Born in future Insha'Allah")
		else:
			print(f"Your age is {age} years old")

	...


if __name__ == '__main__':
    main()
