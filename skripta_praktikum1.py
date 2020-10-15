import numpy as np 
from matplotlib import pyplot as plt 
from scipy.optimize import curve_fit 
#from scipy.interpolate import spline

def funkcija():
    podatkiCo  = np.loadtxt('Beltram_spektroskopija_Co.mca',skiprows=12)
    #delimiter je simbol, ki ločuje stolpce podatkov
    #ce imas stolpce ločene z vejico ali katerim drugim simbolom napišeš: np.loadtxt('ime.txt', delimiter=',', unpack=True)
    #po defaultu je delimiter kakeršen koli prazen prostor (uporabno, če kopiraš iz excella ali drugih programov)
    xx=[i for i in range(len(podatkiCo))]
    #naslov grafa
    plt.title("Blablabla")
    #oznaka osi U (napetost) izpiše napetost {V} pa je primer enote (volt)
    #znotraj dveh dolarjev lahko uporabiš latex notacijo, ampak je samo stilistični popravek, da izgleda lepše $$
    plt.xlabel("$U\,\, [\mathrm{V}]$") #oznaka x osi
    plt.ylabel("$F\,\, [\mathrm{N}]$") #oznaka y osi
    #T1_error = 0.1
    #F_error = 0.0010 #določiš napako vrednosti (tu je napaka konstantna)
    #U_error = 0.020*Napetost #tako pa določiš relativno napako (vsako vrednost množiš) in dobiš različne vrednosti napak

    #izrišeš error bare
    #izbereš lahko svoja imena tako da jih zamenjaš z mojimi;
    #Ostali ukazi so za stil prikaza. pri fmt='' si lahko izberes stil točk.
    #label je oznaka legende
    
    #plt.errorbar(T1, eps_vzp, xerr=T1_error,fmt='k.', elinewidth=0.5, capsize=2, label="meritve")

    #definiramo funkcijo, ki jo hočemo prilagoditi našim podatkomself. v tem primeru je to y = ax + b. kar je premicaself.
    #enako bi izgledalo za ostale na primer
    #def krivulja(x, a, b, c ...):
        #return a*x**3+bx+c (dve zvezdici sta potenca)
    #x = linspace(0,70,1000)
    plt.plot(xx,podatkiCo)
    """
    def linear(x, a, b): #ime bi lahko bilo karkoli, samo jaz sem dal linear, ker je premica
        return a*x + b
    #to vrača tale funkcija (znotraj programa, moramo kasneje še izpisati)
    # return: [best_a, best_b]
    #kovariancna matrika: napako parametra ocenis s korenom diagonalne vrednosti
    # torej: a = best_a +- error_a = params[0] +- sqrt(cov[0,0])

    #vnesemo funkcijo v tem primeru linear in podatke x in y.
    params, cov = curve_fit(linear, T1, eps_vzp)
    print(params, cov) #print izpiše marametre in kovariančno matriko
    #nekako takole:
    #[best_a, best_b]
    #[[x,y][z,d]] s kovariancno matriko se da določiti ustreznost funkcije na podatke
    #sedaj imamo podatke z napako, osi in izračunane parametre
    #želimo narisati krivuljo iz paramtrov, ki se prilega
    x = np.linspace(0, 70, 1000) # xmin, xmax, št točk fita vmes; x min je kjer se bo začela naša krivulja na grafu
    #(v resnici z np.linspace izberemo na primer 500 točk x, ki jim bomo v naslednji funkciji priredili vrednosti glede na parametre)
    fit = linear(x, params[0], params[1]) # poracunajmo y koordinate tock vnaprej
    plt.plot(x, fit, '--', label="fit", color='blue') #narišemo fit torej x, y, izberemo stil prekinjena:'--'; ravna črta:'-'; prekinjena drugače'-.' ali ':';
    #delujejo pod color='' vse rgb barve s heksadecimalnim zapisom (pogledaš na internetu) ali pa napišeš ime (večina jih deluje)

    plt.grid() #po želji lahko izrišemo mrežo
    plt.legend() #nariše legendo
    plt.show() #prikaže vse kar smo označili s plt.
    """
funkcija() #dejansko izvedemo funkcijo