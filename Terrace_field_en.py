# -*- coding: utf-8 -*-
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
        if licz < location:
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
    
    All dimensions in M E T E R S

    ''')
    product_id = input('Enter the product code or continue.  ').replace(',','.')
    length = float(input('Enter the length of the tile / plank. ').replace(',','.'))
    width  = float(input('Enter the width of the tile / board. ').replace(',','.'))
    area_p = area(length , width )
    print('\nThe tile / plank area is: ' + str(round(area_p, 2)) + ' m^2\n')
    excess = input('Will the excess material be used?  (Y)es / (N)o\n').lower()

    print('''\nWhat is known about the terrace? 
1 - Just a field.
2 - Dimensions.
3 - Field with proportions.
4 - Area and one dimension.\n''')
    what_calculated = int(input('Enter the number. '))

    if what_calculated == 1:
        print('\nIt is not possible to calculate the number of finishing strips needed from the given data.\n')
        area_m = float(input('Enter the area of the terrace. ').replace(',','.'))
        tiles_number = area_m / area_p
        print('\nNeed: ' + str(math.ceil(tiles_number)) + ' tiles / planks.')
        price = calculate_price(product_id)
        print('Unit price: ' + str(price) + ' zł. The entire cost will be: ' + str(price * math.ceil(tiles_number)) +' zł.')
        if end() == 1: break

    if what_calculated == 2:
        if excess == 'y':
            length_m = float(input('\nEnter the length of the terrace. ').replace(',','.'))
            width_m = float(input('Enter the width of the terrace. ').replace(',','.'))
            tiles_number = area(length_m, width_m) / area_p
            perimeter = length_m * 2 + width_m * 2
            print('\nThe terrace area is: ' + str(round(area(length_m, width_m), 2)) + ' m^2. ' + str(math.ceil(tiles_number)) + ' planks / tiles are needed and ' + str(round(perimeter, 2)) + ' finishing strips.')
            price = calculate_price(product_id)
            print('Unit price: ' + str(price) + ' zł. The entire cost will be: ' + str(price * math.ceil(tiles_number)) +' zł.')
            if end() == 1: break
        else:
            length_m = float(input('\nEnter the length of the terrace. ').replace(',','.'))
            width_m = float(input('Enter the width of the terrace. ').replace(',','.'))
            perimeter = length_m * 2 + width_m * 2
            value_1, value_2 = calculate_with_losses(lengthm, width_m, length, width)
            price = calculate_price(product_id)
            price_1 = value_1 * price
            print('\nProduct price: ' + str(price) + ' zł.')
            print('\nIn the first variant, you will need: ' + str(value_1) + ' tiles / planks.')
            print('It will cost: ' + str(round(price_1, 2)) + ' zł.')
            price_2 = value_2 * price
            print('\nIn the second variant, you will need: ' + str(value_2) + ' płytek/desek.')
            print('It will cost: ' + str(round(price_2, 2)) + ' zł.')
            print('\nYou will also need ' + str(round(perimeter, 2)) + ' finishing strips.')
            if end() == 1: break

    if what_calculated == 3:
        if excess == 'y':
            area_m = float(input('\nEnter the area of the terrace. ').replace(',','.'))
            prop = input('Enter the proportions of the sides of the terrace in the form "x: y". ').replace(',','.')
            prop_x, prop_y = read_proportions(prop)
            length_m, width_m = sides_from_proportions(prop_x, prop_y, area_m)
            perimeter = length_m * 2 + width_m * 2
            tiles_number = area_m / area_p
            print('\nThe dimensions of the terrace are: ' + str(round(length_m, 2)) + ' by ' + str(round(width_m, 2)) + 'm. ' + str(math.ceil(tiles_number)) + ' planks / tiles are needed and ' + str(round(perimeter, 2)) + ' finishing strips.')
            price = calculate_price(product_id)
            print('Unit price: ' + str(price) + ' zł. The entire cost will be: ' + str(price * math.ceil(tiles_number)) +' zł.')
            if end() == 1: break
        else:
            area_m = float(input('\nEnter the area of the terrace. ').replace(',','.'))
            prop = input('Enter the proportions of the sides of the terrace in the form "x: y". ').replace(',','.')
            prop_x, prop_y = read_proportions(prop)
            length_m, width_m = sides_from_proportions(prop_x, prop_y, area_m)
            perimeter = length_m * 2 + width_m * 2
            value_1, value_2 = calculate_with_losses(length_m, width_m, length, width)
            price = calculate_price(product_id)
            price_1 = value_1 * price
            print('\nThe dimensions of the terrace are: ' + str(round(length_m, 2)) + ' by ' + str(round(width_m, 2)) + 'm.')
            print('\nProduct price: ' + str(price) + ' zł.')
            print('\nIn the first variant, you will need: ' + str(value_1) + ' tiles / planks.')
            print('It will cost: ' + str(round(price_1, 2)) + ' zł.')
            price_2 = value_2 * price
            print('\nIn the second variant, you will need: ' + str(value_2) + ' tiles / planks.')
            print('It will cost: ' + str(round(price_2, 2)) + ' zł.')
            print('\nYou will also need ' + str(round(perimeter, 2)) + ' finishing strips.')
            if end() == 1: break

    if what_calculated == 4:
        if excess == 'y':
            area_m = float(input('\nEnter the area of the terrace. ').replace(',','.'))
            side_a = int(input('Enter the length of one side of the terrace. ').replace(',','.'))
            side_b = side_from_field(side_a, area_m)
            perimeter = side_a * 2 + side_b * 2
            tiles_number = area_m / area_p
            print('\nThe dimensions of the terrace are: ' + str(round(side_a, 2)) + ' by ' + str(round(side_b, 2)) + 'm. ' + str(math.ceil(tiles_number)) + ' planks / tiles are needed and ' + str(round(perimeter, 2)) + ' finishing strips.')
            price = calculate_price(product_id)
            print('Unit price: ' + str(price) + ' zł. The entire cost will be: ' + str(price * math.ceil(tiles_number)) +' zł.')
            if end() == 1: break
        else:
            area_m = float(input('\nEnter the area of the terrace. ').replace(',','.'))
            length_m = int(input('Enter the length of one side of the terrace. ').replace(',','.'))
            width_m = side_from_field(length_m, area_m)
            perimeter = length_m * 2 + width_m * 2
            value_1, value_2 = calculate_with_losses(length_m, width_m, length, width)
            price = calculate_price(product_id)
            price_1 = value_1 * price
            print('\nProduct price: ' + str(price) + ' zł.')
            print('\nIn the first variant, you will need: ' + str(value_1) + ' płytek/desek.')
            print('It will cost: ' + str(round(price_1, 2)) + ' zł.')
            price_2 = value_2 * price
            print('\nIn the second variant, you will need: ' + str(value_2) + ' płytek/desek.')
            print('It will cost: ' + str(round(price_2, 2)) + ' zł.')
            print('\nYou will also need ' + str(round(perimeter, 2)) + ' finishing strips.')
            if end() == 1: break
