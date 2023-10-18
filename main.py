import sys

# allows the program to be exited ^
# set up masterlist

masterlist = []
# open and read the stocks.txt
stocks_file = open('stocks.txt', 'r')
stocks_content = stocks_file.read()
# ignore the line if its first character is a #
for line in stocks_file:
    if line[0] != '#':
        masterlist.append(line.strip().split(','))


# Menu function
def menu():
    print('Welcome to Simply Screws')
    print('***MAIN MENU***')
    print('1: List of screw types available and their details')
    print('2: Report showing total number of units in stock in each length')
    print('3: List of screws and their details based on desired length')
    print('4: Queries')
    print('5: Discount feature')
    print('6: Barchart')
    print('7: Quit')


menu()

choice = int(input('Please make a selection from 1-7: '))

while choice != 0:
    if choice == 1:
        for line in stocks_file:
            if line[0] != '#':
                masterlist.append(line.strip().split(','))
        print(stocks_content)

    elif choice == '2':
        print('')

    elif choice == '3':
        length_category = input('Enter desired length category, 20mm, 40mm or 60mm: ')
        if length_category == 20:
            print('')
        elif length_category == 40:
            print('')
        elif length_category == 60:
            print('')
        else:
            print('ERROR: invalid length category')

