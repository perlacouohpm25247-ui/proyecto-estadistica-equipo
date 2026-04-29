def suma(a, b):
    """
    Devuelve el resultado de la suma de dos números.
    Args:
        a (float): Primer valor a sumar.
        b (float): Segundo valor a sumar.
    Returns:
        float: Resultado de la suma.
    """
    rest = a + b
    return rest

def resta(a, b):
    """
    Devuelve el resultado de la resta de dos números.
    Args:
        a (float): Primer valor (minuendo).
        b (float): Segundo valor (sustraendo).
    Returns:
        float: Resultado de la resta.
    """
    rest = a - b
    return rest

def multiplicacion(a, b):
    """
    Devuelve el resultado de la multiplicación de dos números.
    Args:
        a (float): Primer valor a multiplicar.
        b (float): Segundo valor a multiplicar.
    Returns:
        float: Resultado de la multiplicación.
    """
    rest = a * b
    return rest

def division(a, b):
    """
    Devuelve el resultado de la división de dos números.
    Args:
        a (float): Dividendo.
        b (float): Divisor.
    Returns:
        float o str: Resultado de la división o mensaje de error si b es 0.
    """
    if b == 0:
        return "Error: No se puede dividir por cero"
    rest = a / b
    return rest


# --- PROGRAMA PRINCIPAL ---

def main():
    print("--- Analizador de datos v1.0 ---")
    
    datos = [10, 20, 30, 40, 50, 60] # Datos de prueba
    
    # Se usa f-string (la 'f' antes de las comillas) para mostrar la variable
    print(f"Datos a procesar: {datos}")

    # Ejemplo de llamadas a las funciones:
    print("\nEjemplos de cálculos con los datos:")
    
    v1 = datos[0] # 10
    v2 = datos[1] # 20
    
    print(f"Suma ({v1} + {v2}): {suma(v1, v2)}")
    print(f"Resta ({v1} - {v2}): {resta(v1, v2)}")
    print(f"Multiplicación ({v1} * {v2}): {multiplicacion(v1, v2)}")
    print(f"División ({v1} / {v2}): {division(v1, v2)}")

if __name__ == "__main__":
    main()