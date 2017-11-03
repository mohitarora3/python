import sys
sys.path.append('Desktop/mca101')
import area11
def main():
    '''
    objective: to complete the area of rectangle or triangle as per user's need
    user inputs:
         length: length of rectangle
         breadth: breadth of rectangle
         height: height of triangle
         base: base of triangle
    approach: to import the file area11 and find the area as per user's choice
    return value: area of rectangle or traingle as per user
    '''
    print('Press 1 to find area of rectangle')
    print('Press 2 to find area of triangle')
    print('Press 3 to find area of square')
    choice=int(input('Enter your choice: '))
    if choice==1:
        length=int(input('Enter length of rectangle: '))
        breadth=int(input('Enter breadth of rectangle: '))
        print('area of rectangle: ',area11.areaRectangle(length, breadth))
    elif choice==2:
        base=int(input('Enter base of triangle: '))
        height=int(input('Enter height of triangle: '))
        print('area of triangle: ',area11.areaTriangle(base, height))
    elif choice==3:
        side=int(input('Enter side of square: '))
        print('area of square: ',area11.areaSquare(side))

if __name__=='__main__':
    main()
    
