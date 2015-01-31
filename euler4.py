maxnumber = 1
for i in range(101,999):
    for j in range(101,999):
        wynik = i*j
        wynik_string = str(wynik)
        if (wynik_string[0:1]==wynik_string[-1:] and wynik_string[1:2]==wynik_string[-2:-1]):
            if wynik>maxnumber:
                maxnumber = wynik
                print wynik
