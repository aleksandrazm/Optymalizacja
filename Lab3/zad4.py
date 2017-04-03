import numpy

# wczytywanie problemu do normalizacji (zakladamy, ze wszystkie nierownosci sa postaci "<=" i
#                                        wszystkie zmienne sa >= 0)
temp1 = raw_input("Wpisz min lub max ")

n = int(raw_input("Podaj liczbe zmiennych "))
funkcja_celu = []
print "Funkcja celu"
for i in range(0,n):
    print "Podaj wspolczynnik przy x" + str(i+1)
    funkcja_celu.append(int(raw_input()))

m = int(raw_input("Podaj liczbe ograniczen "))
ograniczenia = []
b=[]

for i in range(0,m):
    temp = []
    print "Ograniczenie " + str(i+1)
    for j in range(0,n):
        temp.append(int(raw_input("Podaj wspolczynniki przy x" + str(j + 1) + " ")))
    b.append(int(raw_input("Podaj liczbe po prawej stronie nierownosci ")))
    for j in range(0,m):                        # zamiana nierownosci na rownosci
        if i==j:
            temp.append(1)
        else:
            temp.append(0)
    ograniczenia.append(temp)
    funkcja_celu.append(0)

if temp1 == "min":
    for i in range(0, n):
        funkcja_celu[i] = 0-funkcja_celu[i]
funkcja_celu=[funkcja_celu]

def mnozenie(matrix,vector):
    wynik = []
    for i in range(0,len(matrix)):
        a = 0.0
        for j in range(0,len(vector)):
            a = a + matrix[i][j]*vector[j]
        wynik.append(a)
    return wynik

k = m + n

def algorytm(e, f, out):
    if next == k:
        if len(f) == m:
            Bk = []
            for i in range(0, m):
                wiersz = []
                for j in f:
                    wiersz.append(A[i][j])
                Bk.append(wiersz)

            if numpy.linalg.matrix_rank(Bk) == m:
                maxX = out[0]
                maxV = out[1]

                vk = mnozenie(numpy.linalg.inv(Bk), b)
                i = 0
                v = []
                for j in range(0, k):
                    if i < m and j == f[i]:
                        v.append(vk[i])
                        i = i + 1
                    else:
                        v.append(0.0)

                if mnozenie(funkcja_celu, v)[0] > maxV:
                    maxX = v[:n]
                    maxV = mnozenie(funkcja_celu, v)[0]

                out[0] = maxX
                out[1] = maxV

    else:
        algorytm(next + 1, f, out)
        if len(f) < m:
            f.append(next)
            mnozenie(next + 1, f, out)
            f.pop()

out = [[], float('-inf')]
f = []
algorytm(0, f, out)
maxX = out[0]
maxV = out[1]

if temp1 == "min":
    print "Minimalna wartoscia funkcji celu jest " + -maxV
    print "Minimalna wartosc jest przyjmowana dla " +  maxX
else:
    print "Maksymalna wartoscia funkcji celu jest " + maxV
    print "Maksymalna wartosc jest przyjmowana dla " + maxX
