def hetman(n):
    print("Maximize\n")
    f = True
    for x in range(1, n + 1):                             # funkcja celu
        for y in range(1, n + 1):
            if f:
                f = False
            else:
                print(' + ', end = '')
            print("x" + str(x) + "," + str(y), end = '')
    print()
    print("\nSubject To\n")
                                                        # nierówności
    for x in range(1, n + 1):                           # suma w wierszach
      f= True;
      for y in range(1, n + 1 ):
        if f:
          f = False
        else:
          print(' + ', end = '')
        print("x" + str(x) + "," + str(y), end = '')
      print(" <= 1")
    print()

    for y in range(1, n + 1):                          # suma w kolumnach
      f= True
      for x in range(1, n + 1):
        if f:
          f = False
        else:
          print(' + ', end = '')
        print("x" + str(x) + "," + str(y), end = '')
      print(" <= 1")
    print()
                                                        # przekątne
    for x in range(1,n+1):                              # od prawej do lewej, górny "trójkąt"
        f= True
        for y in range(1, n-x+1+1):
            if f:
                f = False
            else:
                print(' + ', end = '')
            print("x" + str(n-y+1-x+1) + "," + str(y), end = '')
        print(" <= 1")
    for x in range(2,n+1):                              # od prawej do lewej, dolny "trójkąt"
        f= True
        for y in range(1, n-x+1+1):
            if f:
                f = False
            else:
                print(' + ', end = '')
            print("x" + str(y+x-1) + "," + str(n-y+1), end = '')
        print(" <= 1")
    print()

    for x in range(1,n+1):                              # od lewej do prawej, dolny "trójkąt"
        f= True
        for y in range(1, x+1):
            if f:
                f = False
            else:
                print(' + ', end = '')
            print("x" + str(n+y-x) + "," + str(y), end = '')
        print(" <= 1")
    for x in range(1,n):                                # od lewej do prawej, górny "trójkąt"
        f= True
        for y in range(1, x+1):
            if f:
                f = False
            else:
                print(' + ', end = '')
            print("x" + str(y) + "," + str(n+y-x), end = '')
        print(" <= 1")

    print("\nBounds\n")                                                 # zmienne z przedziału [0,1]
    for x in range(1, n + 1):
        for y in range(1, n + 1):
          print ("0 <= " + "x" + str(x) + "," + str(y) + " <= 1")

    print("\nGenerals\n")                                               # wypisane wszystkie zmienne
    for x in range(1, n + 1):
        for y in range(1, n + 1):
          print ("x" + str(x) + "," + str(y))
    print("\nEnd\n")

n = int(raw_input("Podaj wielkosc szachownicy:"))
if n != 0:
    hetman(n)
else:
    print("Podaj inna wartosc n")
    n = int(raw_input("Podaj wielkosc szachownicy:"))
