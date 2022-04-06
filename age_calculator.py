from datetime import date
from webbrowser import get

import datetime


def get_dob():
    # write code here
	year=input("Enter the Year of bitrh: ")
	mounth=input("Enter the Mounth of bitrh: ")
	day=input("Enter the Day of bitrh: ")


	# if year.isdigit() == False:
	# 	print("Year in invalid")
	# 	return
	
	# elif mounth.isdigit() == False:
	# 	print("Mounth in invalid")
	# 	return
		
	# elif day.isdigit() == False:
	# 	print("Day in invalid")
	# 	return
	# else:
	print("date:",(date(int(year),int(mounth),int(day))))
	return date(int(year),int(mounth),int(day))
	...


def get_age(dob):
    # write code here
	today = datetime.date.today()
	age = int((today - dob).days / 365)
	return age
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
