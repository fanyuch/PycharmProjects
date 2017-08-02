import numpy

print(numpy.array([x for x in range(10)]), [x for x in range(10, 20)])

print(numpy.array([x for x in range(10)], dtype=numpy.int32))

print(numpy.arange(15).reshape(3,5))

print(numpy.arange(15).reshape(5,3))

print(numpy.linspace(1, 3, 7))

print(numpy.zeros((3, 4)))

print(numpy.ones((3, 4)))
