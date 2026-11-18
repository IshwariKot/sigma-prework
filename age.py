from datetime import date, datetime

Date = input("Please enter a date (DD-MM-YYYY): ")


Current = date.today()
Current = str(Current)


if Date[6:10] > Current[0:4]:
    difference = int(Date[6:10]) - int(Current[0:4])
    if int(Date[3:5]) < int(Current[5:7]):
        difference -= 1
    print("The difference in years is: " +
          str(difference) + " years in the future")

else:
    difference = int(Current[0:4]) - int(Date[6:10])
    if int(Date[3:5]) > int(Current[5:7]):
        difference -= 1
    print("The difference in years is: " + str(difference))
