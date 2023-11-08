# MetodoNewton_Python
Codigo en Python para Matematicas IV del Methodo de Newton
## Guia de Usuario 
Guía de Usuario: Aplicación del Método de Newton
1.	Inicio de la Aplicación:
   - Asegúrate de que tienes instalado Python y el módulo SymPy en tu entorno de desarrollo.
	Se descarga de este enlace: https://www.python.org/downloads/
	Se instala SymPy con este comando: pip install sympy
   - Ejecuta el programa y se mostrará un mensaje de bienvenida.
	El comando para ejecutar es: python app.py 
2. Ingresar la Función:
   - Debes ingresar una función matemática en la variable `x`, como una expresión algebraica.
   - Ejemplo válido: `x**2 - 4`.
   - Ejemplo no válido (error de sintaxis): `2x + 3`.
   - Ejemplo no válido (función desconocida): `sin(x) / log(x)`.
3. Ingresar el Valor Inicial (x0):
   - Ingresa un número real como valor inicial (x0) para comenzar el cálculo.
   - Ejemplo válido (entero): `5`.
   - Ejemplo no válido (no numérico): `abc`.
   - Ejemplo no válido (fuera de rango): `-3` con un rango mínimo permitido de `0`.
4. Ingresar la Tolerancia Deseada:
   - Ingresa un número real positivo como la tolerancia deseada.
   - Ejemplo válido (decimal): `0.001`.
   - Ejemplo no válido (no numérico): `xyz`.
   - Ejemplo no válido (fuera de rango): `-0.001` con un rango mínimo permitido de `0`.
5. Ingresar el Número Máximo de Iteraciones:
   - Ingresa un número entero positivo como el número máximo de iteraciones permitidas.
   - Ejemplo válido (entero): `10`.
   - Ejemplo no válido (no numérico): `abc`.
   - Ejemplo no válido (fuera de rango): `-5` con un rango mínimo permitido de `1`.
6. Resultados:
   - El programa calculará la solución utilizando el Método de Newton.
   - Mostrará información sobre cada iteración y el resultado final si se encuentra una solución.
   - Si el método no converge, mostrará un mensaje indicando que no se encontró una solución.
Esta guía te ayudará a utilizar la aplicación de manera efectiva, validando las entradas y obteniendo resultados precisos utilizando el Método de Newton para encontrar soluciones a ecuaciones no lineales.

## Ejemplos para ingresar
Ejemplos para ingresar en la aplicación de consola
Ejemplos completos para ingresar en la aplicación, incluyendo la función, el valor inicial, la tolerancia y el número máximo de iteraciones:
1. Funciones Lineales:
   - Función lineal simple: `2*x - 4`.
   - Valor inicial (x0): `1.5`.
   - Tolerancia: `0.0001`.
   - Número máximo de iteraciones: `10`.
2. Funciones Cuadráticas:
   - Ecuación cuadrática simple: `x**2 - 9`.
   - Valor inicial (x0): `3.0`.
   - Tolerancia: `0.001`.
   - Número máximo de iteraciones: `15`.
3. Funciones Trigonométricas:
   - Función trigonométrica simple: `sin(x) - 0.5`.
   - Valor inicial (x0): `1.0`.
   - Tolerancia: `0.0001`.
   - Número máximo de iteraciones: `10`.
4. Funciones Exponenciales:
   - Ecuación exponencial simple: `2*exp(x) - 5`.
   - Valor inicial (x0): `1.0`.
   - Tolerancia: `0.001`.
   - Número máximo de iteraciones: `12`.
5. Funciones Trascendentales:
   - Ecuación trascendental simple: `log(x) - 1`.
   - Valor inicial (x0): `2.0`.
   - Tolerancia: `0.0001`.
   - Número máximo de iteraciones: `10`.
 
6. Ecuaciones que no convergen:
   - Función sin raíces reales: `x**2 + 1`.
   - Valor inicial (x0): `0.5`.
   - Tolerancia: `0.0001`.
   - Número máximo de iteraciones: `15`.

   - Función con raíz múltiple: `(x - 2)**3`.
   - Valor inicial (x0): `2.0`.
   - Tolerancia: `0.001`.
   - Número máximo de iteraciones: `5`.


