##########################  WCZYTYWANIE DANYCH ################################
# program pomocniczy szukajacy wierzcholka do metody sympleks
# zakladamy, ze ograniczenia podane sa w postaci rownan
# oraz wszystkie zmienne sa nieujemne

n = int(raw_input("Podaj liczbe zmiennych "))
funkcja_celu  = []
print "Funkcja celu"
for i in range(0,n):
    funkcja_celu.append(int(raw_input("Podaj wspolczynnik przy x" + str(i+1) + " ")))

m = int(raw_input("Podaj liczbe ograniczen "))
ograniczenia = []
b=[]

for i in range(0,m):
    temp = []
    print "Ograniczenie " + str(i+1)
    for j in range(0,n):
        temp.append(int(raw_input("Podaj wspolczynniki przy x" + str(j + 1) + " ")))
    b.append(int(raw_input("Podaj liczbe po prawej stronie równania ")))
    for j in range(0,m):                        # dodawanie nowych zmiennych
        if i==j:
            temp.append(1)
        else:
            temp.append(0)
    ograniczenia.append(temp)
    funkcja_celu.append(0)
c=[]                                            # nowa funkcja celu
for i in range(0,len(funkcja_celu)):
	if i < n:
		c.append(0)
	else:
		c.append(-1)

######################## ROZWIAZANIE PROBLEMU ##################################
g = InteractiveLPProblem(ograniczenia, b, c, 'x',constraint_type="==", variable_type=">=")
view(g)
print "rozwiazanie: " + str(g.optimal_solution())
