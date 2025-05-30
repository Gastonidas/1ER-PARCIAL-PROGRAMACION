#---------------------------------------------------------------------
# CREACION DE MATRICES Y ARRAYS
#---------------------------------------------------------------------
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    """Crea una matriz con valores iniciales y parametros solicitados

    Args:
        cantidad_filas (int): Cantidad de filas que queremos que tenga la matriz
        cantidad_columnas (int): Cantidad de columnas que queremos que tenga la matriz
        valor_inicial (any): Valor inicial de cada posicion de la matriz

    Returns:
        list: Devuelve la matriz
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        #matriz.append(fila)
        matriz += [fila]
        
    return matriz

def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    """Crea un array con valores iniciales y parametros solicitados

    Args:
        cantidad_elementos (int): Cantidad de elementos que queremos que tenga la matriz
        valor_inicial (any): Valor inicial de cada posicion del array

    Returns:
        list: Devuelve el array
    """
    array = [valor_inicial] * cantidad_elementos
    return array

#---------------------------------------------------------------------
# VALIDACIONES DE INGRESO DE DATOS
#---------------------------------------------------------------------

#Verificacion entrada Int
def verificar_int(entrada):
    """Verifica que la entrada sea un valor entero, sino sigue pidiendo la entrada hasta que el dato sea del tipo correcto

    Args:
        entrada (_type_): dato ingresado por el usuario

    Returns:
            devuelve el dato ingresado por el usuario solo si fue del tipo entero
    """
    entrada_cruda = input(entrada)
    while not es_entero(entrada_cruda):
        print("Error: Entrada no válida. Por favor, ingrese un número entero")
        entrada_cruda = input(entrada)
    return int(entrada_cruda)    

#Validacion numero Int
def es_entero(cadena:str) -> bool:
    """Verifica que el valor provisto sea un valor numerico

    Args:
        cadena (str): valor provisto por la funcion que esta llamando a esta funcion

    Returns:
        bool: retorna un valor verdadero si el valor provisto es un entero
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if valor_ascii > 57 or valor_ascii < 48:
                retorno = False
                break
    else:
        retorno = False 
    
    return retorno

#Verificacion entrada de nombres
def verificar_nombres(entrada):
    """Verifica que la entrada sea un string, sino sigue pidiendo la entrada hasta que el dato sea del tipo correcto

    Args:
        entrada (_type_): Dato ingresado por usuario

    Returns:
        devuelve el dato ingresado por el usuario solo si fue del tipo string
    """
    entrada_cruda = input(entrada)
    while not es_alfabetico(entrada_cruda):
        print("Error: Entrada no válida. Por favor, ingrese un nombre con mas de 3 letras")
        entrada_cruda = input(entrada)
    return (entrada_cruda)  

#Validacion String con al menos 3 letras
def es_alfabetico(cadena:str) -> bool:#verificacion string mayor a 3 letras
    """Verifica que el valor provisto sea un string con al menos 3 letras

    Args:
        cadena (str): valor provisto por la funcion que esta llamando a esta funcion

    Returns:
        bool: retorna un valor verdadero si el valor provisto es un string de al menos 3 caracteres
    """
    if len(cadena) > 2:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if (valor_ascii > 90 or valor_ascii < 65) and (valor_ascii > 122 or valor_ascii < 97):
                retorno = False
                break
    else:
        retorno = False 
    
    return retorno

#---------------------------------------------------------------------
# CARGA DE DATOS
#---------------------------------------------------------------------

#ESPECIFICA
def cargar_nombres_participantes(array_nombres:list) -> bool:
    """Carga los nombres de los participantes en un array previamente creado

    Args:
        array_nombres (list): Array donde van a ser guardados los nombres

    Returns:
        bool: devuelve un valor verdadero si los datos fueron correctamente ingresados al array provisto
    """
    if type(array_nombres) == list and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            #Pedir el dato
            nombre = verificar_nombres(f"Ingrese el nombre del participante {i + 1}: ")
            #Guardar ese dato en el array
            array_nombres[i] = nombre
        retorno = True    
    else:
        retorno = False
        
    return retorno

#ESPECIFICA 
def cargar_puntos(matriz_puntos:list, lista_nombres:list) -> bool:
    """Carga los puntajes de los participantes en una matriz previamente creada

    Args:
        matriz_puntos (list): Matriz donde van a ser guardados los puntajes
        lista_nombres (list): Array con los nombres de los participantes previamente guardados

    Returns:
        bool: devuelve un valor verdadero si los datos fueron correctamente ingresados a la matriz provista
    """
    if type(matriz_puntos) == list and len(matriz_puntos) > 0:
        retorno = True
    
        for fil in range(len(matriz_puntos)):
            matriz_puntos[fil][0] = lista_nombres[fil]
            for col in range(1,len(matriz_puntos[fil])):
                #Pedir el dato
                puntaje = verificar_int(f"Ingrese puntaje del participante {fil + 1} emitido por el Jurado {col}: ")
                while puntaje > 10 or puntaje < 1:
                      puntaje = verificar_int("Reingrese el puntaje (1-10): ")
                #Guardarlo en la matriz
                matriz_puntos[fil][col] = puntaje
    else:
        retorno = False
        
    return retorno

#---------------------------------------------------------------------
# FUNCIONES PARA MOSTRAR DATOS
#---------------------------------------------------------------------

#GENERAL
def mostrar_array(array:list) -> None:
    """Imprime los valores del array ingresado

    Args:
        array (list): Array ingresado
    """
    for i in range(len(array)):
        print(f"{array[i]}")

#GENERAL  
def mostrar_matriz(matriz:list) -> None:
    """Imprime los valores de la matriz ingresada

    Args:
        matriz (list): Matriz ingresada
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}",end=" ")
        print("")

#ESPECIFICA
def mostrar_puntaje(array_nombres:list,matriz_puntos:list,indice:int) -> bool:
    """Imprime los nombres de los participantes INDICADOS por el indice, junto con los puntajes que han obtenido

    Args:
        array_nombres (list): Array con los nombres de los participantes
        matriz_puntos (list): Matriz con los puntos de los participantes
        indice (int): fila que quiero mostrar de la matriz provista

    Returns:
        bool: Indica si la funcion se llevo a cabo satisfactoriamente o no
    """
    if type(matriz_puntos) == list and type(array_nombres) == list and len(matriz_puntos) > 0 and len(array_nombres) > 0 and (indice < len(array_nombres) and indice >= 0):
        # porcentaje = mostrar_promedio_puntaje (matriz_puntos)
        retorno = True
        print(f"PARTICIPANTES: {matriz_puntos[indice][0]}")
        print(f"PUNTUACION JURADO 1: {matriz_puntos[indice][1]}")
        print(f"PUNTUACION JURADO 2: {matriz_puntos[indice][2]}")
        print(f"PUNTUACION JURADO 3: {matriz_puntos[indice][3]}")
        prom= promediar (matriz_puntos[indice][1],matriz_puntos[indice][2],matriz_puntos[indice][3],3) 
             
        print(f"PUNTAJE promedio: {round(prom,2)}/10")
    else:
        retorno = False
        
    return retorno

#ESPECIFICA
def mostrar_puntajes(array_nombres:list,matriz_puntos:list) -> bool:
    """Imprime los nombres y los puntajes de TODOS los participantes, al recorrer la matriz con los datos de los mismos

    Args:
        array_nombres (list): Array con los nombres de los participantes
        matriz_puntos (list): Matriz con los puntos de los participantes

    Returns:
        bool: Indica si la funcion se llevo a cabo satisfactoriamente o no
    """
    if type(matriz_puntos) == list and type(array_nombres) == list and len(matriz_puntos) > 0 and len(array_nombres) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            mostrar_puntaje(array_nombres,matriz_puntos,i)
            print("")
    else:
        retorno = False
        
    return retorno

#---------------------------------------------------------------------
# FUNCIONES DE CALCULO
#---------------------------------------------------------------------

# ESPECIFICA
def promediar (item1:int, item2:int, item3:int, dividendo):
    """Realiza el promedio de los valores ingresados

    Args:
        item1 (int): Nota Jurado 1
        item2 (int): Nota Jurado 2
        item3 (int): Nota Jurado 3
        dividendo: Cantidad de notas recibidas

    Returns:
            Devuelve el promedio de los valores ingresados
    """
    resultado = (item1+item2+item3) /dividendo
    return resultado

#ESPECIFICA/GENERAL - PARAMETRIZADA
def mostrar_participantes_promedio_menor_que(matriz_puntos:list,array_nombres:list,promedio_limite:float) -> bool:
    """Muestra los participantes con un promedio menor al solicitado

    Args:
        matriz_puntos (list): Matriz con los puntos de los participantes 
        array_nombres (list): Array con los nombres de los participantes
        promedio_limite (float): Valor al cual deben ser inferiores los promedios

    Returns:
        bool: Indica si la funcion se llevo a cabo satisfactoriamente o no
    """
    retorno = False
    
    if type(matriz_puntos) == list and type(array_nombres) == list and len(matriz_puntos) > 0 and len(array_nombres) > 0:
        for i in range(len(matriz_puntos)):
            prom= promediar (matriz_puntos[i][1],matriz_puntos[i][2],matriz_puntos[i][3],3)
            if prom < promedio_limite:
                mostrar_puntaje(array_nombres,matriz_puntos,i)
                print("")
                retorno = True
                
    return retorno

def calcular_promedio(acumulador:float | int, contador:int) -> float | None:
    """Calcula el promedio de los valores ingresados

    Args:
        acumulador (float | int): Suma los valores ingresados
        contador (int): Almacena la cantidad de valores ingresados

    Returns:
        float | None: Devuelve el promedio de los valores ingresados
    """
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
        
    return promedio


def transponer_matriz_comprension(matriz):
    """Transpone la matriz ingresada

    Args:
        matriz: Matriz ingresada

    Returns:
            Devuelve la matriz transpuesta a la matriz ingresada
    """
    if not matriz or not matriz[0]: # Verifica si la matriz o su primera fila están vacías
        return []
    
    num_filas_original = len(matriz)
    num_columnas_original = len(matriz[0]) # Asume que todas las filas tienen la misma longitud
    
    # recorre  cada índice de columna de la matriz original para crear las nuevas filas
    matriz_transpuesta = []
    for indice_columna in range(num_columnas_original):#recorre de 0 a num columnas (0 - 4)
        nueva_fila = []                                 #Matriz donde guardo el array con las nuevas filas
        # recorre  cada índice de fila de la matriz original para tomar los elementos de la nueva columna
        for indice_fila in range(num_filas_original):   #desde 0 hasta len(matriz) (cantidad de ffilas matriz) (0-4)
            nueva_fila += [matriz[indice_fila][indice_columna]]  #matriz[0][0] / matriz[1][0] / matriz[2][0] // matriz[0][1] / matriz [1][1]
        matriz_transpuesta += [nueva_fila]               #agrega y guarda en la matriz transp. el array generado
        
    return matriz_transpuesta


def encontrar_participantes_con_mismo_puntaje(matriz_puntos: list) -> bool:
    """
    Busca y muestra participantes que tengan el mismo puntaje promedio.
    Compara a cada participante con los demás para encontrar coincidencias.

    Args:
        - matriz_puntos (list): La matriz que contiene los nombres y puntajes.
                                Se espera la estructura [nombre, p1, p2, p3].

    Returns:
        - bool: True si se encontró al menos un par de participantes con el mismo
                puntaje, False en caso contrario.
    """
    se_encontraron_coincidencias = False
    cantidad_participantes = len(matriz_puntos)

    # Usamos un bucle anidado para comparar cada participante con los siguientes
    # El segundo bucle empieza en i + 1 para no comparar a un participante consigo mismo ni comparar A-B y B-A o sea no repetir los pares
    
    for i in range(cantidad_participantes):
        for j in range(i + 1, cantidad_participantes):
            # Calculamos el promedio para el primer participante (i)
            promedio_i = promediar(matriz_puntos[i][1], matriz_puntos[i][2], matriz_puntos[i][3], 3)
            # Calculamos el promedio para el segundo participante (j)
            promedio_j = promediar(matriz_puntos[j][1], matriz_puntos[j][2], matriz_puntos[j][3], 3)

            if promedio_i == promedio_j:
                if not se_encontraron_coincidencias:
                    # Imprimir un encabezado solo la primera vez que encontramos una coincidencia
                    print("Se encontraron participantes con el mismo puntaje promedio:")
                
                nombre_i = matriz_puntos[i][0]
                nombre_j = matriz_puntos[j][0]
                print(f"- {nombre_i} y {nombre_j} tienen un promedio de {round(promedio_i, 2)} puntos.")
                
                se_encontraron_coincidencias = True
    
    return se_encontraron_coincidencias

def buscar_participante_por_nombre(matriz_puntos: list, array_nombres: list):
    """
    Solicita al usuario que ingrese un nombre, lo busca en la lista de
    participantes y, si lo encuentra, muestra todos sus datos y puntajes.

    Args:
        - matriz_puntos (list): La matriz con los datos de los puntajes.
        - array_nombres (list): El array que contiene solo los nombres.

    Returns:
        - None: La función imprime directamente el resultado en la consola. No devuelve nada
    """
    nombre_buscado = input("Ingrese el nombre del participante que desea buscar: ")
    
    encontrado = False
    indice_encontrado = -1

    for i in range(len(array_nombres)):
        if array_nombres[i] == nombre_buscado:
            encontrado = True
            indice_encontrado = i
      
            break
            
    if encontrado:
        print("\n--- Datos del Participante Encontrado ---")
   
        mostrar_puntaje(array_nombres, matriz_puntos, indice_encontrado)
    else:
        print(f"\nError: No se encontró a ningún participante con el nombre '{nombre_buscado}'.")


def mostrar_top_tres(matriz_puntos: list):
    """
    Ordena los participantes de mayor a menor según su puntaje promedio y
    muestra los tres primeros (el Top 3). 

    Args:
        - matriz_puntos (list): La matriz original con nombres y puntajes.

    Returns:
        - None: La función imprime directamente el resultado en la consola.
    """
    # Creamos una copia de la matriz para no modificar la original
    matriz_copia = []
    for i in range(len(matriz_puntos)):
        matriz_copia += [matriz_puntos[i]]

    n = len(matriz_copia)
    for i in range(n):
        for j in range(0, n - i - 1): #el menos es poruq tenemso que comparar 4 veces porque son 5 elemntos. si comparamos 5 veces se rompe
           
            promedio_j = promediar(matriz_copia[j][1], matriz_copia[j][2], matriz_copia[j][3], 3)
            promedio_j1 = promediar(matriz_copia[j+1][1], matriz_copia[j+1][2], matriz_copia[j+1][3], 3)
            
            # lo Resolvimos metiendo un intercambio en caso de que el actual sea menor, lo cambia por el mas alto comparado
            if promedio_j < promedio_j1:
                # Intercambio de las filas completas
                fila_temporal = matriz_copia[j]
                matriz_copia[j] = matriz_copia[j+1]
                matriz_copia[j+1] = fila_temporal

    print("--- 🏆 Top 3 de Participantes 🏆 ---")
    
    # Determinamos con la variable limite cuántos participantes mostrar (hasta un máximo de 3) 
    
    limite = 3
        
    for i in range(limite):
        nombre = matriz_copia[i][0]
        puntaje_prom = promediar(matriz_copia[i][1], matriz_copia[i][2], matriz_copia[i][3], 3)
        print(f"#{i+1}: {nombre} - promediar: {round(puntaje_prom, 2)}")
        print(f"   (Jurado 1: {matriz_copia[i][1]}, Jurado 2: {matriz_copia[i][2]}, Jurado 3: {matriz_copia[i][3]})")
        print("-" * 35)

# FUNCIÓN PARA EL PUNTO 12 (ORDEN ALFABÉTICO)
def mostrar_participantes_ordenados_alfabeticamente(matriz_puntos: list):
    """
    Ordena los participantes alfabéticamente de la A a la Z por su nombre y
    muestra la lista completa con sus datos. 

    Args:
        - matriz_puntos (list): La matriz original con nombres y puntajes.

    Returns:
        - None: La función imprime directamente el resultado en la consola.
    """
    # Creamos una copia de la matriz para no alterar el orden original
    matriz_copia = []
    for i in range(len(matriz_puntos)):
        matriz_copia += [matriz_puntos[i]]

    # Implementación del Ordenamiento Burbuja para ordenar de A a Z
    n = len(matriz_copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            nombre_j = matriz_copia[j][0]
            nombre_j1 = matriz_copia[j+1][0]
            
            # Si el nombre actual es "mayor" que el siguiente (viene después en el
            # alfabeto), los intercambiamos.
            if nombre_j > nombre_j1:
                fila_temporal = matriz_copia[j]
                matriz_copia[j] = matriz_copia[j+1]
                matriz_copia[j+1] = fila_temporal

    print("\n---  Participantes Ordenados Alfabéticamente (A-Z)  ---")
    for i in range(len(matriz_copia)):
        mostrar_puntaje(matriz_copia, matriz_copia, i)
        print("") # Para dar un espacio entre participantes

#---------------------------------------------------------------------
# 
#---------------------------------------------------------------------
# GENERAL - Función auxiliar para sumar elementos de un array
def sumar_elementos_array(array_numerico: list) -> float:
    """
    Suma todos los elementos numéricos de un array (lista).

    Args:
        - array_numerico (list): Una lista de números.

    Returns:
        - float: La suma total de los elementos.
    """
    acumulador = 0
    for i in range(len(array_numerico)):
        acumulador += array_numerico[i]
    return acumulador



def promediar_jurado(matriz_puntos: list, array_jurados: list) -> bool:
    """
    Calcula el puntaje promedio otorgado por cada jurado. Para ello, transpone
    la matriz de puntos y calcula el promedio de cada fila (que representa a un jurado).

    Args:
        - matriz_puntos (list): La matriz original con [nombre, p1, p2, p3].
        - array_jurados (list): El array vacío donde se guardarán los promedios de cada jurado.

    Returns:
        - bool: True si el cálculo se realizó con éxito.
    """
    matriz_transpuesta = transponer_matriz_comprension(matriz_puntos)
    
    # La primera fila (índice 0) de la transpuesta tiene nombres, la omitimos.
    # Recorremos a partir de la segunda fila (índice 1), que son los jurados.
    for i in range(1, len(matriz_transpuesta)):
        # Esta es la lista de todos los puntajes que dio un jurado
        puntajes_del_jurado = matriz_transpuesta[i]
        
        # Usamos nuestra función auxiliar para sumar los puntajes
        suma_de_puntajes = sumar_elementos_array(puntajes_del_jurado)
        cantidad_de_participantes = len(puntajes_del_jurado)
        
        # Usamos tu función para calcular el promedio
        promedio_final = calcular_promedio(suma_de_puntajes, cantidad_de_participantes)
        
        # Guardamos el promedio en la posición correcta del array de jurados
        array_jurados[i-1] = promedio_final
        print(f"PUNTAJE promedio JURADO {i}: {round(promedio_final, 2)}")
    
    return True


def mostrar_jurado_promedio_minimo(array_jurados: list) -> float:
    """
    Encuentra y muestra cuál fue el jurado que otorgó el promedio de puntajes más bajo.

    Args:
        - array_jurados (list): La lista con los promedios de cada jurado.

    Returns:
        - float: El valor del promedio más bajo encontrado.
    """
    minimo = array_jurados[0]
    indice_minimo = 0  #  Inicializamos el índice en 0.

    # Empezamos el bucle en 1, ya que el valor de la posición 0 ya está en 'minimo'.
    for i in range(1, len(array_jurados)):
        if array_jurados[i] < minimo:
            minimo = array_jurados[i]
            indice_minimo = i
            
    print(f"-> El jurado N°{indice_minimo + 1} fue el más estricto (promedio más bajo: {round(minimo, 2)}).")
    return minimo

def mostrar_jurado_promedio_maximo(array_jurados: list) -> float:
    """
    Encuentra y muestra cuál fue el jurado que otorgó el promedio de puntajes más alto.

    Args:
        - array_jurados (list): La lista con los promedios de cada jurado.

    Returns:
        - float: El valor del promedio más alto encontrado.
    """
    maximo = array_jurados[0]
    indice_maximo = 0  # : Inicializamos el índice en 0.

    for i in range(1, len(array_jurados)):
        if array_jurados[i] > maximo:
            maximo = array_jurados[i]
            indice_maximo = i
            
    print(f"-> El jurado N°{indice_maximo + 1} fue el más generoso (promedio más alto: {round(maximo, 2)}).")
    return maximo

