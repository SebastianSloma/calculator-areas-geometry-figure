import areas

Wybór = input("""Wybierz figure której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4.Trójkąt
5. Trapez
""")

if(Wybór == '1'):
    a = int(input("Podaj bok kwadratu: "))
    print("Pole kwadratu wynosi: ", areas.area_square(a))

if(Wybór == '2'):
    a = int(input("Podaj pierwszy bok prostokątu: "))
    b = int(input("Podaj drugi bok prostokątu: "))
    print("Pole prostokątu wynosi: ", areas.area_rectangle(a, b))

if(Wybór == '3'):
    r = int(input("Podaj promień koła: "))
    print("Pole koła wynosi: ", areas.area_circle(r))

if(Wybór == '4'):
    a = int(input("Podaj bok trójkąta: "))
    h = int(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi: ", areas.area_triangle(a, h))

if(Wybór == '5'):
    a = int(input("Podaj pierwszy bok trapezu: "))
    b = int(input("Podaj drugi bok trapezu: "))
    h = int(input("Podaj wysokość trapezu: "))
    print("Pole trapezu wynosi: ", areas.area_trapeze(a, b, h))