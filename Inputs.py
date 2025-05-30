import os
from Funciones import *

array_nombres = crear_array(5,"")
array_jurados = crear_array(3,"")
matriz_puntos = crear_matriz(5,4,0)

bandera_carga_nombres = False
bandera_carga_puntaje = False
bandera_carga_jurados = False
bandera_promedio = False

while True:
    print("--- MENÚ DEL CONCURSO ---")
    print("1. Cargar Nombres de Participantes")
    print("2. Cargar Puntajes de Jurados")
    print("3. Mostrar Puntaje Completo")
    print("4. Participantes con promedio menor a 4")
    print("5. Participantes con promedio menor a 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Jurado más generoso")
    print("9. Ver participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("--- PUNTOS EXTRAS ---")
    print("11. Mostrar Top 3 participantes (PUNTO EXTRA)")
    print("12. Mostrar participantes ordenados alfabéticamente (PUNTO EXTRA)")
    print("13. Salir")
    print("-" * 27)

    opcion = verificar_int("Su opcion: ")

    while opcion > 13 or opcion < 1:
        opcion = int(input("Reingrese su opcion (1-13): "))
        
    if opcion == 1:
        if cargar_nombres_participantes(array_nombres):
            print("Nombres cargados correctamente...")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error al realizar la carga")
            
    elif opcion == 2:
        if bandera_carga_nombres:
            if cargar_puntos(matriz_puntos, array_nombres):
                print("Carga exitosa de puntajes!")
                mostrar_matriz(matriz_puntos)
                bandera_carga_puntaje = True
            else:
                print("Error al realizar la carga")
        else:
            print("Error, debe cargar los nombres primero (Opción 1).")
            
    elif opcion == 3:
        if bandera_carga_puntaje:
            mostrar_puntajes(array_nombres, matriz_puntos)
            bandera_promedio = True 
        else:
            print("Error, debe cargar los puntajes primero (Opción 2).")

    elif opcion == 4:
        if bandera_promedio:
            mostrar_participantes_promedio_menor_que(matriz_puntos, array_nombres, 4)
        else:
            print("Error, debe mostrar los puntajes primero (Opción 3).")
            
    elif opcion == 5:
        if bandera_promedio:
            mostrar_participantes_promedio_menor_que(matriz_puntos, array_nombres, 8)
        else:
            print("Error, debe mostrar los puntajes primero (Opción 3).")
            
    elif opcion == 6:
        if bandera_promedio:
            promediar_jurado(matriz_puntos, array_jurados)
            bandera_carga_jurados = True
        else:
            print("Error, debe mostrar los puntajes primero (Opción 3).")
            
    elif opcion == 7:
        if bandera_carga_jurados:
            mostrar_jurado_promedio_minimo(array_jurados)
        else:
            print("Error, debe promediar los jurados primero (Opción 6).")
            
    elif opcion == 8:
        if bandera_carga_jurados:
            mostrar_jurado_promedio_maximo(array_jurados)
        else:
            print("Error, debe promediar los jurados primero (Opción 6).")

    elif opcion == 9:
        if bandera_carga_puntaje:
            if not encontrar_participantes_con_mismo_puntaje(matriz_puntos):
                print("Mensaje: No se encontraron participantes con puntajes promedio idénticos.")
        else:
            print("Error, debe cargar los puntajes primero (Opción 2).")

    elif opcion == 10:
        if bandera_carga_nombres:
            buscar_participante_por_nombre(matriz_puntos, array_nombres)
        else:
            print("Error, debe cargar los nombres primero (Opción 1).")
            
    elif opcion == 11:
        if bandera_carga_puntaje:
            mostrar_top_tres(matriz_puntos)
        else:
            print("Error, debe cargar los puntajes primero (Opción 2).")
            
    elif opcion == 12:
        if bandera_carga_puntaje:
            mostrar_participantes_ordenados_alfabeticamente(matriz_puntos)
        else:
            print("Error, debe cargar los puntajes primero (Opción 2).")

    elif opcion == 13: 
        print("Saliendo del programa...")
        break
    
    if opcion != 13: 
        input("\nToque cualquier tecla para continuar...")
   
    os.system("cls")
   