from gradient import Gradient
from NewtonMethod import NewtonMethod
from BinaryS import BinarySearch

print("Градиентный спуск")
g = Gradient(5, 5)
g.solve()

print("\nМетод Ньютона")
n = NewtonMethod(2)
n.solve()

print("\nМетод бинарного поиска:")
b = BinarySearch(0, 4)
b.solve()