import areas

from enum import IntEnum

Menu_Figures = IntEnum('Menu_Figuers', 'Square Ractangle Circle Triangle Trapeze')

choice = int(input("""Select the figure whose area you want to calculate:
1. Square
2. Ractangle
3. Circle
4. Triangle
5. Trapezoid
"""))

if(choice == Menu_Figures.Square):
    a = int(input("Give the side of the square: "))
    print("The area of the square is: ", areas.area_square(a))

elif(choice == Menu_Figures.Ractangle):
    a = int(input("Give the first side of the rectangle: "))
    b = int(input("Give the second side of the rectangle: "))
    print("The area of the ractangle is: ", areas.area_rectangle(a, b))

elif(choice == Menu_Figures.Circle):
    r = int(input("Give the radius of the circle: "))
    print("The area of the circle is: ", areas.area_circle(r))

elif(choice == Menu_Figures.Triangle):
    a = int(input("Give the side of the triangle: "))
    h = int(input("Give the height of the triangle: "))
    print("The area of the triangle is: ", areas.area_triangle(a, h))

elif(choice == Menu_Figures.Trapeze):
    a = int(input("Give the first side of the trapezoid: "))
    b = int(input("Give the second side of the trapezoid: "))
    h = int(input("Give the height of the trapezoid: "))
    print("The area of the trapezoid is: ", areas.area_trapeze(a, b, h))