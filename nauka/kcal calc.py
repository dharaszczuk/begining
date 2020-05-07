#prosty kalkulator dziennego zapotrzebowania na kalorie
print ("Do obliczenia dziennego zapotrzebowania na kalorie \nbędziemy potrzebowali kliku danych\n")
w = int(input ("Podaj swoją wagę w kg:\n"))
h = int(input ("Podaj swój wzrost w cm:\n"))
a = int(input ("Podaj swój wiek:\n"))
g = input ("Podaj swoją płeć k/m:\n")
if g == "k":
    s = -161
else:
    s = 5
int(s)
PPM = 10*w+6.25*h-5*a+s
print ("Twoje dzienne zapotrzebowanie wynosi:", 1.2*PPM)
