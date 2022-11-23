import areas

from enum import IntEnum

Menu_Figures = IntEnum('Menu_Figuers', 'Square Ractangle Circle Triangle Trapeze')

choice = int(input("""Wybierz figure której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez
"""))

if(choice == Menu_Figures.Square):
    a = int(input("Podaj bok kwadratu: "))
    print("Pole kwadratu wynosi: ", areas.area_square(a))

elif(choice == Menu_Figures.Ractangle):
    a = int(input("Podaj pierwszy bok prostokątu: "))
    b = int(input("Podaj drugi bok prostokątu: "))
    print("Pole prostokątu wynosi: ", areas.area_rectangle(a, b))

elif(choice == Menu_Figures.Circle):
    r = int(input("Podaj promień koła: "))
    print("Pole koła wynosi: ", areas.area_circle(r))

elif(choice == Menu_Figures.Triangle):
    a = int(input("Podaj bok trójkąta: "))
    h = int(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi: ", areas.area_triangle(a, h))

elif(choice == Menu_Figures.Trapeze):
    a = int(input("Podaj pierwszy bok trapezu: "))
    b = int(input("Podaj drugi bok trapezu: "))
    h = int(input("Podaj wysokość trapezu: "))
    print("Pole trapezu wynosi: ", areas.area_trapeze(a, b, h))