import math
import requests
from bs4 import BeautifulSoup

def pole(bok_a, bok_b):
    pole= bok_a * bok_b
    return pole

def boki_z_prpoporcji(prop_1, prop_2, pole):
    bok_b = math.sqrt(pole * prop_2 / prop_1)
    bok_a = pole / bok_b
    return bok_a, bok_b

def czytanie_poporcji(n_proporcje):
    licz = 0
    prop_1 = ''
    prop_2 = ''
    miejsce = n_proporcje.find(':')
    for i in n_proporcje:
        if licz < miejsce:
            prop_1 = prop_1 + i
        if licz > miejsce:
            prop_2 = prop_2 + i
        licz += 1
    return float(prop_1), float(prop_2)

def boki_z_prop(prop_1, prop_2, pole):
    bok_b = math.sqrt(pole * prop_2 / prop_1)
    bok_a = pole / bok_b
    return bok_a, bok_b

def bok_z_pola(bok_a, pole):
    bok_b = pole / bok_a
    return bok_b

def koniec():
    koniec = input('\nZakończyć? (T)ak / (N)ie\n').lower()
    if koniec[0] == 't':
        return 1

def wyliczenie_ceny(nr_produktu):
    if len(nr_produktu) != 7:
        return 0
    strona = requests.get('https://www.obi.pl/p/' + nr_produktu)
    zupa = BeautifulSoup(strona.text, 'html.parser')
    wynik = zupa.find_all('span', attrs={'class':'overview-sticky-header__price'})
    wynik1 = wynik[0]
    cena_txt = wynik1.find('strong').text[0:-3]
    cena_float = float(cena_txt.replace(',','.'))
    #cena_koncowa = cena_float * math.ceil(liczba_plytek)
    return cena_float
    #print('Cena jednostkowa: ' + str(cena_float) + ' zł. Całość kosztować będzie: ' + str(round(cena_koncowa, 2)) +' zł.')   
    #strona = requests.get('https://www.obi.pl/p/' + str(nr_produktu))
    #drzewo = html.fromstring(strona.content)
    #cena = drzewo.xpath('//span[@class="overview-sticky-header__price"]/text()')

def licz_ze_stratami(miejsce_a, miejsce_b, deska_a, deska_b):
    boki_a1 = miejsce_a / deska_a
    boki_b1 = miejsce_b / deska_b
    ilość_war_1 = math.ceil(boki_a1) * math.ceil(boki_b1)
    boki_a2 = miejsce_a / deska_b
    boki_b2 = miejsce_b / deska_a
    ilość_war_2 = math.ceil(boki_a2) * math.ceil(boki_b2)
    return ilość_war_1, ilość_war_2


while True:
    print('''v 0.8.1

    DŁUGOŚCI PODAWAĆ W  M E T R A C H

    ''')
    kod_prod = input('Podaj kod produktu lub przejdź dalej. ').replace(',','.')
    dlu = float(input('Podaj długość płytki/deski. ').replace(',','.'))
    szer = float(input('Podaj szerokość płytki/deskideski. ').replace(',','.'))
    pole_p = pole(dlu, szer)
    print('\nPole płytki/deski to: ' + str(round(pole_p, 2)) + ' m^2\n')
    nadmiar = input('Czy nadmiarowy materiał będzie wykorzystywany? (T)ak / (N)ie\n').lower()

    print('''\nCo jest wiadome o miejscu?
1 - Samo pole.
2 - Wymary.
3 - Pole z proporcjami.
4 - Pole i jeden bok.\n''')
    co_liczone = int(input('Podaj numer. '))

    if co_liczone == 1:
        print('\nZ podanych danych  nie jest możliwe wyliczenie ilości potrzebnych obrzeży.\n')
        pole_m = float(input('Podaj pole miejsca. ').replace(',','.'))
        ilosc_plytek = pole_m / pole_p
        print('\nPotrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek')
        cena = wyliczenie_ceny(kod_prod)
        print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
        if koniec() == 1: break

    if co_liczone == 2:
        if nadmiar == 't':
            dlugosc_m = float(input('\nPodaj długość miejsca. ').replace(',','.'))
            szerokosc_m = float(input('Podaj szerokość miejsca. ').replace(',','.'))
            ilosc_plytek = pole(dlugosc_m, szerokosc_m) / pole_p
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            print('\nPole miejsca to: ' + str(round(pole(dlugosc_m, szerokosc_m), 2)) + ' m^2. Potrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek oraz ' + str(round(obwod, 2)) + ' metrów obrzeży.')
            cena = wyliczenie_ceny(kod_prod)
            print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
            if koniec() == 1: break
        else:
            dlugosc_m = float(input('\nPodaj długość miejsca. ').replace(',','.'))
            szerokosc_m = float(input('Podaj szerokość miejsca. ').replace(',','.'))
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            il_war_1, il_war_2 = licz_ze_stratami(dlugosc_m, szerokosc_m, dlu, szer)
            cena = wyliczenie_ceny(kod_prod)
            cena_1 = il_war_1 * cena
            print('\nCena produktu: ' + str(cena) + ' zł.')
            print('\nW pierwszym warciancie potrzeba: ' + str(il_war_1) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_1, 2)) + ' zł.')
            cena_2 = il_war_2 * cena
            print('\nW drugim warciancie potrzeba: ' + str(il_war_2) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_2, 2)) + ' zł.')
            print('\nBędzie też potrzeba ' + str(round(obwod, 2)) + ' obrzeży.')
            if koniec() == 1: break

    if co_liczone == 3:
        if nadmiar == 't':
            pole_m = float(input('\nPodaj pole miejsca. ').replace(',','.'))
            prop = input('Podaj proporcje boków miejsca w postaci "x:y". ').replace(',','.')
            prop_x, prop_y = czytanie_poporcji(prop)
            dlugosc_m, szerokosc_m = boki_z_prpoporcji(prop_x, prop_y, pole_m)
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            ilosc_plytek = pole_m / pole_p
            print('\nWymiary miejsca to: ' + str(round(dlugosc_m, 2)) + ' na ' + str(round(szerokosc_m, 2)) + 'm. Potrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek oraz ' + str(round(obwod, 2)) + ' metrów obrzeży.')
            cena = wyliczenie_ceny(kod_prod)
            print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
            if koniec() == 1: break
        else:
            pole_m = float(input('\nPodaj pole miejsca. ').replace(',','.'))
            prop = input('Podaj proporcje boków miejsca w postaci "x:y". ').replace(',','.')
            prop_x, prop_y = czytanie_poporcji(prop)
            dlugosc_m, szerokosc_m = boki_z_prpoporcji(prop_x, prop_y, pole_m)
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            il_war_1, il_war_2 = licz_ze_stratami(dlugosc_m, szerokosc_m, dlu, szer)
            cena = wyliczenie_ceny(kod_prod)
            cena_1 = il_war_1 * cena
            print('\nWymiary miejsca to: ' + str(round(dlugosc_m, 2)) + ' na ' + str(round(szerokosc_m, 2)) + 'm.')
            print('\nCena produktu: ' + str(cena) + ' zł.')
            print('\nW pierwszym warciancie potrzeba: ' + str(il_war_1) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_1, 2)) + ' zł.')
            cena_2 = il_war_2 * cena
            print('\nW drugim warciancie potrzeba: ' + str(il_war_2) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_2, 2)) + ' zł.')
            print('\nBędzie też potrzeba ' + str(round(obwod, 2)) + ' obrzeży.')
            if koniec() == 1: break

    if co_liczone == 4:
        if nadmiar == 't':
            pole_m = float(input('\nPodaj pole miejsca. ').replace(',','.'))
            bok_a = int(input('Podaj w metrach długość jednego z boków miejsca. ').replace(',','.'))
            bok_b = bok_z_pola(bok_a, pole_m)
            obwod = bok_a * 2 + bok_b * 2
            ilosc_plytek = pole_m / pole_p
            print('\nWymiary miejsca to: ' + str(round(bok_a, 2)) + ' na ' + str(round(bok_b, 2)) + 'm. Potrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek oraz ' + str(round(obwod, 2)) + ' metrów obrzeży.')
            cena = wyliczenie_ceny(kod_prod)
            print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
            if koniec() == 1: break
        else:
            pole_m = float(input('\nPodaj pole miejsca. ').replace(',','.'))
            dlugosc_m = int(input('Podaj w metrach długość jednego z boków miejsca. ').replace(',','.'))
            szerokosc_m = bok_z_pola(dlugosc_m, pole_m)
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            il_war_1, il_war_2 = licz_ze_stratami(dlugosc_m, szerokosc_m, dlu, szer)
            cena = wyliczenie_ceny(kod_prod)
            cena_1 = il_war_1 * cena
            print('\nCena produktu: ' + str(cena) + ' zł.')
            print('\nW pierwszym warciancie potrzeba: ' + str(il_war_1) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_1, 2)) + ' zł.')
            cena_2 = il_war_2 * cena
            print('\nW drugim warciancie potrzeba: ' + str(il_war_2) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_2, 2)) + ' zł.')
            print('\nBędzie też potrzeba ' + str(round(obwod, 2)) + ' obrzeży.')
            if koniec() == 1: break
