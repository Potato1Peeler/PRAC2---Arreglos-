import numpy as np
import time

empezar_tiempo= time.time()
Filas= int(input("Ingresa los alumnos que necesites:  "))
Columnas= int(input("Ingresa las materias que necesites: "))
matriz = np.random.randint(0, 101, size=(Filas, Columnas))

np.set_printoptions(threshold=np.inf, linewidth=np.inf, suppress=True)

print(matriz)
terminar_tiempo=time.time()
tiempo= terminar_tiempo - empezar_tiempo
print(f"\nEl programa tardo {tiempo}s en ejecutarse")

Buscar_Alumno=int(input("\nIngresa al Alumno que desea buscar (Empezando en 0): "))
Buscar_Materia=int(input("Ingresa la materia que desea buscar (Empezando en 0): "))
print("\nLa calificacion del alumno es de: ",matriz[Buscar_Alumno][Buscar_Materia])




