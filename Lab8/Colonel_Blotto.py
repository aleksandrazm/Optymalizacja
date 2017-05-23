import numpy

# 7 możliwych strategii: (0,0,6), (0,1,5), (0,2,4), (0,3,3), (1,1,4), (1,2,3), (2,2,2)
# Macierz wypłat

M = numpy.array([[0,0,0,0,-1,-1,-1],[0,0,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,0,-1,0,1],[1,0,0,1,0,0,-1],[1,1,0,0,0,0,0],[1,1,0,-1,1,0,0]])
b=[0,0,0,0,0,0,0,1]
c=[1,0,0,0,0,0,0,0]

A=M.T
A=(-1)*A
# dodawanie wiersza
newrow = [1,1,1,1,1,1,1]
A = numpy.append(A, [newrow], axis = 0)
# dodawanie kolumny
newcol = numpy.array([[1,1,1,1,1,1,1,1]])
A = numpy.concatenate((newcol.T,A),axis=1)
# problem
P = InteractiveLPProblem(A, b, c, ["y", "x1", "x2", "x3", "x4", "x5", "x6", "x7"], constraint_type = ["<=","<=","<=","<=","<=","<=","<=","=="], variable_type = ["", ">=", ">=", ">=", ">=",">=", ">=", ">="])
show(P)
x = P.optimal_solution()
print "Optymalna strategia gracza: " + str(x[1:8])
