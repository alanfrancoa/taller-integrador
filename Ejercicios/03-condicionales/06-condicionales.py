'''
Cond6. Escribir la función de dos argumentos reales positivos p, q, que calcule y regrese la raíz más grande de la ecuación x2 − 2p x − q = 0 
'''

from math import *  # Importamos el módulo math para usar la función sqrt

def raizMayor(p, q):
    """
    Calcula la raíz más grande de la ecuación cuadrática: x² - 2px - q = 0
    
    Parámetros:
    p (float): Coeficiente lineal (debe ser positivo)
    q (float): Término independiente (debe ser positivo)
    
    Retorna:
    float: La raíz más grande de la ecuación
    """
    
    # La ecuación es de la forma: x² - 2px - q = 0
    # Que corresponde a: ax² + bx + c = 0, donde:
    # a = 1, b = -2p, c = -q
    
    # Calculamos el discriminante simplificado:
    # Para esta ecuación específica, el discriminante (b²-4ac) se reduce a:
    # (-2p)² - 4(1)(-q) = 4p² + 4q = 4(p² + q)
    # Al sacar raíz cuadrada: √(4(p² + q)) = 2√(p² + q)
    # Pero como luego dividimos entre 2a (que es 2), se simplifica a √(p² + q)
    discriminante = sqrt(p**2 + q)  # Calculamos √(p² + q)
    
    # Aplicamos la fórmula cuadrática simplificada para esta ecuación:
    # x = [2p ± 2√(p² + q)] / 2 = p ± √(p² + q)
    # La raíz mayor es la que usa el signo positivo:
    return p + discriminante  # x = p + √(p² + q)

# Valores de entrada para prueba
print(raizMayor(1, 1))  # Ecuación: x² - 2x - 1 = 0
# Soluciones: 1 ± √(1+1) → 1 + √2 ≈ 2.4142 (mayor)
#             1 - √2 ≈ -0.4142 (menor)
# Debería imprimir aproximadamente 2.4142

print(raizMayor(3, 4))  # Ecuación: x² - 6x - 4 = 0
# Soluciones: 3 ± √(9+4) → 3 + √13 ≈ 6.6055 (mayor)
#             3 - √13 ≈ -0.6055 (menor)
# Debería imprimir aproximadamente 6.6055