import sys

def main():

    '''

    Objective: To compute price per unit weight of a item

    Input Parameter: None

    Return Value: None

    '''

    price = float(input('Enter price of item purchased: '))

    weight = float(input('Enter weight of item purchased: '))

    try:

        if price == '': price = None

        try:

            price = float(price)

        except ValueError:

            print('Invalid inputs: ValueError')

        if weight == '': weight = None

        try:
    
            weight = float(weight)

        except ValueError:

            print('Invalid inputs: ValueError')
    
        assert price >= 0 and weight >= 0

        result =float(price / weight)

    except TypeError:

        print('Invalid inputs: TypeError')

    except ZeroDivisionError:

        print('Invalid inputs: ZeroDivisionError')

    except:

        print(str(sys.exc_info()))

    else:

        print('Price per unit weight: ', result)

if __name__ == '__main__':

    main()
