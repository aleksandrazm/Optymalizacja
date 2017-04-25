# Zagadnienie pomocnicze
Program szuka wierzchołka, od którego można rozpocząć rozwiązywanie problemu optymalizacji liniowej za pomocą metody sympleks.

Zakładamy, że wszystkie ograniczenia podane są za pomocą równań oraz że wszystkie zmienne są nieujemne.

Program można uruchomić na stronie: http://cloud.sagemath.org

Testy:
1. Dane A=[[8, 3, -5, -1], [3, 1, -2, -1]], b=[4, 1], c=[7, 2, -3, -1]
   wynik: rozwiązanie optymalne v=[3,0,4,0,0,0], wartość optymalna x=0.
2. Dane A=[[1, 3, 1], [0, 2, 1]], b=[4, 2], c=[1, 2, 0]
   wynik: rozwiązanie optymalne v=[2,0,2,0,0], wartość optymalna x=0.
