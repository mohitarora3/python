def areaRectangle(length,breadth):
    '''
    objective: to compute the area of rectangle
    input parameters:
        length: length of rectangle
        breadth: breadth of rectangle
    approach: multiply length and breadth
    return value: area of rectangle
    '''
    area=length*breadth
    return area

def areaSquare(side):
    '''
    objective: to compute the area of a square
    input parameters:
        side: side of the square
    approach: to invoke the function areaRectangle with
              side as length and breadth
    return value: area of square
    '''
    return areaRectangle(side,side)

def areaTriangle(base, height):
    '''
    objective:to compute the area of Triangle
    input parameters:
        base: base of Triangle
        height: height of triangle
    approach: multiply base and height and divide it by 2
    return value: area of triangle
    '''
    area = base*height/2
    return area
    
