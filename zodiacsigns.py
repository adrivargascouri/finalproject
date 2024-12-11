
zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
stations = ["spring", "summer", "autum", "winter"]

def get_user_data():
    
while True:
    day = int(input("What day you were born?"))
    month = int(input("insert the number of the month you were born"))
    sign_position = 0
    stations = 0

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

    if month in [11, 12, 1]:
        stations = "winter"
    elif month in [8, 9, 10]:
        stations = "autum"
    elif month in [5, 6, 7]:
        stations = "summer"
    elif month in [2, 3, 4]:
        stations = "spring"
    
    print(f"You were born at the time of the year {stations}")
    resp = input("If you want to continue press enter, if not press space")
    if resp == " ":
        break

user_data = 
        