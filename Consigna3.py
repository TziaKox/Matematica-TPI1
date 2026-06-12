m = [
    [120, 150, 110],
    [200, 180, 220],
    [90, 110, 95]
]
for i in range(3):
    sumafila = 0  
    for j in range(3):
        sumafila = sumafila + m[i][j]
    
    promediofila = sumafila / 3  
    print(f"Promedio de la fila {i + 1}: {promediofila}")

for i in range(3):
    sumacolumna = 0 
    for j in range(3):
        sumacolumna = sumacolumna + m[j][i] 
    
    promediocolumna = sumacolumna / 3 
    print(f"Promedio de la columna {i + 1}: {promediocolumna}")

mtranspuesta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        mtranspuesta[j][i] = m[i][j]

print("Matriz Transpuesta Correcta:")
for fila in mtranspuesta:
    print(fila)