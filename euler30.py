wynik = 0
for i in range(1,1000000):
    liczba = i
    liczba_str = str(liczba)
    suma_cyfr = 0
    for cyfra in liczba_str:
        suma_cyfr=suma_cyfr+int(cyfra)**5
    if suma_cyfr == liczba and liczba!=1 :
        wynik = wynik + suma_cyfr
        print suma_cyfr
print "Problem 30 solution is: %s " % (wynik)
