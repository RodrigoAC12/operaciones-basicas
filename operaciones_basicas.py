"""
Módulo que proporciona clases para realizar operaciones matemáticas básicas y calcular promedios.
"""

class OperacionesBasicas:
    """
    Clase que proporciona operaciones matemáticas básicas como suma y resta.

    Atributos:
        resultado (int, float): Almacena el resultado de la última operación realizada.
    """

    def __init__(self):
        """
        Inicializa la clase con un resultado en 0.
        """
        self.resultado = 0

    def sumar(self, a, b):
        """
        Suma dos números y almacena el resultado.

        Parámetros:
            a (int, float): Primer número a sumar.
            b (int, float): Segundo número a sumar.
        """
        self.resultado = a + b

    def restar(self, a, b):
        """
        Resta dos números y almacena el resultado.

        Parámetros:
            a (int, float): Minuendo.
            b (int, float): Sustraendo.
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """
        Retorna el resultado de la última operación realizada.

        Retorna:
            int, float: Resultado almacenado.
        """
        return self.resultado


class CalculadoraPromedio:
    """
    Clase que permite calcular el promedio de una lista de valores numéricos.

    Atributos:
        valores (list): Lista de números sobre los que se calculará el promedio.
    """

    def __init__(self, valores):
        """
        Inicializa la clase con una lista de valores.

        Parámetros:
            valores (list): Lista de números.
        """
        self.valores = valores

    def calcular_promedio(self):
        """
        Calcula el promedio de los valores almacenados.

        Retorna:
            float: El promedio de los valores.
        """
        suma_total = sum(self.valores)
        return suma_total / len(self.valores)

    def obtener_cantidad_valores(self):
        """
        Retorna la cantidad de valores en la lista.

        Retorna:
            int: Número de elementos en la lista.
        """
        return len(self.valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora = CalculadoraPromedio(NUMEROS)
    promedio_calculado = calculadora.calcular_promedio()
    print(f"El promedio de los números es: {promedio_calculado}")
