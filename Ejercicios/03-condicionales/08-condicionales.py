"""
Cond8. Función característica del intervalo [a, b]

Dados tres números reales a, b, x:
- Devuelve 1 si x pertenece al intervalo cerrado [a, b] (es decir, si a ≤ x ≤ b)
- Devuelve 0 en cualquier otro caso

Ejemplos:
1. Entrada: -3.0, 7.5, 5.0 → Salida: 1 (5.0 está entre -3.0 y 7.5)
2. Entrada: 7.5, -3.0, 5.0 → Salida: 0 (a > b, intervalo no válido)
3. Entrada: -3.0, 7.5, -5.0 → Salida: 0 (-5.0 fuera del intervalo)
"""

def enIntervalo(a, b, x):
    """
    Determina si x está en el intervalo cerrado [a, b]
    
    Parámetros:
    a (float): Límite inferior del intervalo
    b (float): Límite superior del intervalo
    x (float): Valor a verificar
    
    Retorna:
    int: 1 si x está en [a, b], 0 en caso contrario
    
    Observación:
    - Si a > b, el intervalo [a, b] no contiene ningún valor (siempre retorna 0)
    - La comparación a ≤ x ≤ b se evalúa correctamente en Python
    """
    # La expresión a <= x <= b verifica ambas condiciones simultáneamente:
    # 1. Que x sea mayor o igual que a (a <= x)
    # 2. Que x sea menor o igual que b (x <= b)
    # Python evalúa esto de manera óptima como (a <= x) and (x <= b)
    return 1 if a <= x <= b else 0

# Casos de prueba
print(enIntervalo(-3.0, 7.5, 5.0))   # 1 (5.0 ∈ [-3.0, 7.5])
print(enIntervalo(7.5, -3.0, 5.0))   # 0 (intervalo [7.5, -3.0] no existe)
print(enIntervalo(-3.0, 7.5, -5.0))  # 0 (-5.0 ∉ [-3.0, 7.5])