import math
import requests
from bs4 import BeautifulSoup

def area(side_a, side_b):
    area = side_a * side_b
    return area

def sides_from_proportions(prop_1, prop_2, area):
    bok_b = math.sqrt(area * prop_2 / prop_1)
    bok_a = area / bok_b
    return bok_a, bok_b

def read_proportions(proportion):
    count = 0
    prop_1 = ''
    prop_2 = ''
    location = proportion.find(':')
    for i in proportion:
        if licz < location
            prop_1 = prop_1 + i
        if licz > location:
            prop_2 = prop_2 + i
        count += 1
    return float(prop_1), float(prop_2)

def side_from_field(side_a, area):
    side_b = area / side_a
    return side_b

def end():
    end = input('\nDo you want to close the script? (Y)es / (N)o\n').lower()
    if end[0] == 'y':
        return 1

def calculate_price(product_id):
    if len(product_id) != 7:
        return 0
    webpage = requests.get('https://www.obi.pl/p/' + product_id)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    result = soup.find_all('span', attrs={'class':'overview-sticky-header__price'})
    result1 = result[0]
    price_txt = result1.find('strong').text[0:-3]
    price_float = float(price_txt.replace(',','.'))
    return price_float

def calculate_with_losses(terrace_l, terrace_w, plank_l, plank_w):
    sides_a1 = terrace_l / plank_l
    sides_b1 = terrace_w / plank_w
    quantity_1 = math.ceil(sides_a1) * math.ceil(sides_b1)
    sides_a2 = terrace_l / deska_b
    sides_b2 = terrace_w / plank_w
    quantity_2 = math.ceil(sides_a2) * math.ceil(sides_b2)
    return quantity_1, quantity_2


while True:
    print('''v 0.8.1

    DŁUGOŚCI PODAWAĆ W  M E T R A C H

    ''')
    kod_prod = input('Podaj kod produktu lub przejdź dalej. ').replace(',','.')
    dlu = float(input('Podaj długość płytki/deski. ').replace(',','.'))
    szer = float(input('Podaj szerokość płytki/deskideski. ').replace(',','.'))
    area_p = area(dlu, szer)
    print('\nPole płytki/deski to: ' + str(round(area_p, 2)) + ' m^2\n')
    nadmiar = input('Czy nadmiarowy materiał będzie wykorzystywany? (T)ak / (N)ie\n').lower()

    print('''\nCo jest wiadome o miejscu?
1 - Samo area.
2 - Wymary.
3 - Pole z proporcjami.
4 - Pole i jeden bok.\n''')
    co_liczone = int(input('Podaj numer. '))

    if co_liczone == 1:
        print('\nZ podanych danych  nie jest możliwe wyliczenie ilości potrzebnych obrzeży.\n')
        area_m = float(input('Podaj area miejsca. ').replace(',','.'))
        ilosc_plytek = area_m / area_p
        print('\nPotrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek')
        cena = calculate_price(kod_prod)
        print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
        if koniec() == 1: break

    if co_liczone == 2:
        if nadmiar == 't':
            dlugosc_m = float(input('\nPodaj długość miejsca. ').replace(',','.'))
            szerokosc_m = float(input('Podaj szerokość miejsca. ').replace(',','.'))
            ilosc_plytek = area(dlugosc_m, szerokosc_m) / area_p
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            print('\nPole miejsca to: ' + str(round(area(dlugosc_m, szerokosc_m), 2)) + ' m^2. Potrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek oraz ' + str(round(obwod, 2)) + ' metrów obrzeży.')
            cena = calculate_price(kod_prod)
            print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
            if koniec() == 1: break
        else:
            dlugosc_m = float(input('\nPodaj długość miejsca. ').replace(',','.'))
            szerokosc_m = float(input('Podaj szerokość miejsca. ').replace(',','.'))
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            il_war_1, il_war_2 = calculate_with_losses(dlugosc_m, szerokosc_m, dlu, szer)
            cena = calculate_price(kod_prod)
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
            area_m = float(input('\nPodaj area miejsca. ').replace(',','.'))
            prop = input('Podaj proporcje boków miejsca w postaci "x:y". ').replace(',','.')
            prop_x, prop_y = read_proportions(prop)
            dlugosc_m, szerokosc_m = sides_from_proportions(prop_x, prop_y, area_m)
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            ilosc_plytek = area_m / area_p
            print('\nWymiary miejsca to: ' + str(round(dlugosc_m, 2)) + ' na ' + str(round(szerokosc_m, 2)) + 'm. Potrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek oraz ' + str(round(obwod, 2)) + ' metrów obrzeży.')
            cena = calculate_price(kod_prod)
            print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
            if koniec() == 1: break
        else:
            area_m = float(input('\nPodaj area miejsca. ').replace(',','.'))
            prop = input('Podaj proporcje boków miejsca w postaci "x:y". ').replace(',','.')
            prop_x, prop_y = read_proportions(prop)
            dlugosc_m, szerokosc_m = sides_from_proportions(prop_x, prop_y, area_m)
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            il_war_1, il_war_2 = calculate_with_losses(dlugosc_m, szerokosc_m, dlu, szer)
            cena = calculate_price(kod_prod)
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
            area_m = float(input('\nPodaj area miejsca. ').replace(',','.'))
            bok_a = int(input('Podaj w metrach długość jednego z boków miejsca. ').replace(',','.'))
            bok_b = side_from_field(bok_a, area_m)
            obwod = bok_a * 2 + bok_b * 2
            ilosc_plytek = area_m / area_p
            print('\nWymiary miejsca to: ' + str(round(bok_a, 2)) + ' na ' + str(round(bok_b, 2)) + 'm. Potrzeba: ' + str(math.ceil(ilosc_plytek)) + ' płytek/desek oraz ' + str(round(obwod, 2)) + ' metrów obrzeży.')
            cena = calculate_price(kod_prod)
            print('Cena jednostkowa: ' + str(cena) + ' zł. Całość kosztować będzie: ' + str(cena * math.ceil(ilosc_plytek)) +' zł.')
            if koniec() == 1: break
        else:
            area_m = float(input('\nPodaj area miejsca. ').replace(',','.'))
            dlugosc_m = int(input('Podaj w metrach długość jednego z boków miejsca. ').replace(',','.'))
            szerokosc_m = side_from_field(dlugosc_m, area_m)
            obwod = dlugosc_m * 2 + szerokosc_m * 2
            il_war_1, il_war_2 = calculate_with_losses(dlugosc_m, szerokosc_m, dlu, szer)
            cena = calculate_price(kod_prod)
            cena_1 = il_war_1 * cena
            print('\nCena produktu: ' + str(cena) + ' zł.')
            print('\nW pierwszym warciancie potrzeba: ' + str(il_war_1) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_1, 2)) + ' zł.')
            cena_2 = il_war_2 * cena
            print('\nW drugim warciancie potrzeba: ' + str(il_war_2) + ' płytek/desek.')
            print('Kosztować to będzie: ' + str(round(cena_2, 2)) + ' zł.')
            print('\nBędzie też potrzeba ' + str(round(obwod, 2)) + ' obrzeży.')
            if koniec() == 1: break
