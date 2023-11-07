import sympy as sp

def newton_method(func, x0, tolerance, max_iterations):
    x = sp.symbols('x')
    
    try:
        f = sp.sympify(func)
        df = sp.diff(f, x)
    except (sp.SympifyError, sp.DerivativeError):
        raise ValueError('La función o su derivada no se pueden procesar.')
    
    results = []
    
    for i in range(max_iterations):
        try:
            f_value = f.subs(x, x0).evalf()
            df_value = df.subs(x, x0).evalf()
        except (sp.SympifyError, sp.DerivativeError):
            raise ValueError('La función o su derivada no se pueden evaluar en x0.')

        results.append((i, x0, f_value, df_value))
        
        if abs(f_value) < tolerance:
            return results, x0
        
        if df_value == 0:
            raise ValueError('La derivada se hizo cero. No se puede continuar.')
        
        try:
            x1 = x0 - f_value / df_value
        except (sp.SympifyError, sp.DerivativeError):
            raise ValueError('Error al calcular la siguiente iteración.')

        if abs(x1 - x0) < tolerance:
            results.append((i+1, x1, f_value, df_value))
            return results, x1

        x0 = x1
    
    raise ValueError(f'El método de Newton no convergió después de {max_iterations} iteraciones.')

def main():
    func = input('Ingrese la función (por ejemplo, x**2 - 4): ')
    x0 = float(input('Ingrese el valor inicial x0: '))
    tolerance = float(input('Ingrese la tolerancia deseada: '))
    max_iterations = int(input('Ingrese el número máximo de iteraciones: '))

    try:
        results, result = newton_method(func, x0, tolerance, max_iterations)
        print(f'Solución encontrada en la iteración {results[-1][0]}: x = {result}')
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    main()
