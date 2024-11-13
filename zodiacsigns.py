
signos_zodicales=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
estaciones=["spring","summer","autum","winter"]
while True:
    dia=int(input("What day were you born?\n"))
    mes=int(input ("What number of the month were you born?\n"))
    posicion_signo=0
    estaciones=0
    if (dia>=21 and mes==3) or (dia<=19 and mes==4):
        print(signos_zodicales[0])
    elif (dia>=20 and mes==4) or (dia<=20 and mes==5):
        print(signos_zodicales[1])
    elif (dia>=21 and mes==5) or (dia<=20 and mes==6):
        print(signos_zodicales[2])
    elif (dia>=21 and mes==6) or (dia<=22 and mes==7):
        print(signos_zodicales[3])
    elif (dia>=23 and mes==7) or (dia<=22 and mes==8):
        print(signos_zodicales[4])
    elif (dia>=23 and mes==8) or (dia<=22 and mes==9):
        print(signos_zodicales[5])
    elif (dia>=23 and mes==9) or (dia<=22 and mes==10):
        print(signos_zodicales[6])
    elif (dia>=23 and mes==10) or (dia<=21 and mes==11):
        print(signos_zodicales[7])
    elif (dia>=22 and mes==11) or (dia<=21 and mes==12):
        print(signos_zodicales[8])
    elif (dia>=22 and mes==12) or (dia<=19 and mes==1):
        print(signos_zodicales[9])
    elif (dia>=20 and mes==1) or (dia<=18 and mes==2):
        print(signos_zodicales[10])
    elif (dia>=19 and mes==2) or (dia<=20 and mes==3):
        print(signos_zodicales[11])

        #determinar estacion del año
    if mes in[11,12,1]:
        estaciones="winter"
    elif mes in [8,9,10]:
        estaciones="autum"
    elif mes in [5,6,7]:
        estaciones="summer"
    elif mes in [2,3,4]:
        estaciones="spring"

    print(f"You were born at the time of the year {estaciones}")
    resp=input("If you desire to not continue press space , if not press enter to continue")
    if resp==" ":
        break

        