import numpy as np
import matplotlib.pyplot as plt
import math

# Definir la función original
def f(x):
    return np.sin(x)

# Función para calcular la Serie de Taylor de sin(x) hasta un número de términos dado
def taylor_sin(x, n_terms):
    approximation = 0
    for n in range(n_terms):
        term = ((-1)**n) * (x**(2*n + 1)) / math.factorial(2*n + 1)
        approximation += term
    return approximation

# Crear un rango de valores para x
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Evaluar la función original
y_real = f(x)

# Aproximaciones de la serie de Taylor con diferentes órdenes
y_taylor_3 = taylor_sin(x, 3)  # Taylor hasta el término 3
y_taylor_5 = taylor_sin(x, 5)  # Taylor hasta el término 5
y_taylor_7 = taylor_sin(x, 7)  # Taylor hasta el término 7
y_taylor_9 = taylor_sin(x, 9)  # Taylor hasta el término 9

# Crear gráficos
plt.figure(figsize=(10, 6))
plt.plot(x, y_real, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y_taylor_3, label='Taylor Orden 3', linestyle='--', color='red')
plt.plot(x, y_taylor_5, label='Taylor Orden 5', linestyle='--', color='orange')
plt.plot(x, y_taylor_7, label='Taylor Orden 7', linestyle='--', color='green')
plt.plot(x, y_taylor_9, label='Taylor Orden 9', linestyle='--', color='purple')

# Configurar el gráfico
plt.title('Aproximaciones de la Serie de Taylor de sin(x) alrededor de x=0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
