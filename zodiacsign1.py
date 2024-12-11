
print("Welcome to your Zodiac signs and season game")
print("")


zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

rango_min = (int(1))

def get_and_check_days(rango_min):

    message = (str("What day of the year you were born? "))
    rango_max = (int(31))
    while True:
        try:
            day = int(input(message))

            if rango_min <= day <= rango_max:
                return day
            else:
                print(f"Please, enter a valid input between {rango_min} and {rango_max}")
        except ValueError:
            print("please enter a int number for the day ")


def get_and_check_months(rango_min):

    while True:
        try:
            question = (str("Insert number of your birth month: "))
            max_rango = (int(12))
            month = int(input(question))
            if rango_min <= month <= max_rango:
                return month
            else:
                print(f"Please, enter a valid input between {rango_min} and {max_rango}")
        except ValueError:
            print("Please enter a int number of month")


def calculate_zodiac_sign(day, month):

    sign_position = 0

    if (day >= 21 and month == 3) or (day <= 19 and month == 4):
        print(zodiac_signs[0])
        
    elif (day >= 20 and month == 4) or (day <= 20 and month == 5):
        print(zodiac_signs[1])
        
    elif (day >= 21 and month == 5) or (day <= 20 and month == 6):
        print(zodiac_signs[2])
        
    elif (day >= 21 and month == 6) or (day <= 22 and month == 7):
        print(zodiac_signs[3])
        
    elif (day >= 23 and month == 7) or (day <= 22 and month == 8):
        print(zodiac_signs[4])
        
    elif (day >= 23 and month == 8) or (day <= 22 and month == 9):
        print(zodiac_signs[5])
        
    elif (day >= 23 and month == 9) or (day <= 22 and month == 10):
        print(zodiac_signs[6])
        
    elif (day >= 23 and month == 10) or (day <= 21 and month == 11):
        print(zodiac_signs[7])
        
    elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
        print(zodiac_signs[8])
        
    elif (day >= 22 and month == 12) or (day <= 19 and month == 1):
        print(zodiac_signs[9])

    elif (day >= 20 and month == 1) or (day <= 18 and month == 2):
        print(zodiac_signs[10])
        
    elif (day >= 19 and month == 2) or (day <= 20 and month == 3):
        print(zodiac_signs[11])
    
    else:
        print("Invalid option, please insert a number between (1/31)")
        print("")


def calculate_season_year(month):

    if month == 12 or month == 1 or month == 2:
        print("Winter")
    elif month >= 3 and month <= 5:
        print("Spring")
    elif month >= 6 and month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Autumn")
    else:
        print("Invalid option, please insert a number between (1/12)")


def main():
    while True:
        print("")
        print("Main Menu:")
        print("1. See your zodiac sign")
        print("2. See in which season of the month you were borned ")
        print("3. Exit")

        try:
            option = int(input("choose an option: "))

            if option == 1:
                while True:
                    day = get_and_check_days(rango_min)
                    month = get_and_check_months(rango_min)
                    if day and month:
                        calculate_zodiac_sign(day, month)
                        break
                    else:
                        print("Invalid input, please enter a correct day and month.")
                        print("")
                    
            elif option == 2:
                while True:
                    month = get_and_check_months(rango_min)
                    calculate_season_year(month)
                    break

            elif option == 3:
                print("")
                print("Thanks for participating!")
                print("Hope to see you soon!")
                print("")
                break
            
            else:
                print("Invalid Option. Please enter a number between (1-2)")
                print("")
        
        except ValueError:
            print("Invalid Input. Please enter a number between (1-2)")
            print("")


main()

