import math

# Definir la función y sus derivadas
def f(x):
    return math.cos(x)

def f_prime(x):
    return -math.sin(x)

def f_double_prime(x):
    return -math.cos(x)

def f_triple_prime(x):
    return math.sin(x)

# Parámetros iniciales
x0 = math.pi / 3  # valor de x0 = pi/3
f0 = f(x0)  # f(pi/3) = cos(pi/3)
x1 = math.pi / 4  # queremos conocer f(pi/4)
h = x1 - x0  # h = x1 - x0

# Iteración de orden 1
f_order1 = f(x0) + f_prime(x0) * h
error1 = abs(f(x1) - f_order1)

# Iteración de orden 2
f_order2 = f(x0) + f_prime(x0) * h + (f_double_prime(x0) / math.factorial(2)) * (h**2)
error2 = abs(f(x1) - f_order2)

# Iteración de orden 3
f_order3 = (f(x0) + f_prime(x0) * h + (f_double_prime(x0) / math.factorial(2)) * (h**2) +
            (f_triple_prime(x0) / math.factorial(3)) * (h**3))
error3 = abs(f(x1) - f_order3)

# Mostrar resultados
print(f"Valor de f(pi/4) real: {f(x1):.6f}")
print(f"Aproximación de orden 1: {f_order1:.6f}, Error: {error1:.6f}")
print(f"Aproximación de orden 2: {f_order2:.6f}, Error: {error2:.6f}")
print(f"Aproximación de orden 3: {f_order3:.6f}, Error: {error3:.6f}")

# Criterio de error (detener cuando el error es menor a 0.0005)
tolerance = 0.0005
if error3 < tolerance:
    print("El error está dentro del límite de tolerancia en la iteración 3.")
else:
    print("El error no cumple con la tolerancia.")
