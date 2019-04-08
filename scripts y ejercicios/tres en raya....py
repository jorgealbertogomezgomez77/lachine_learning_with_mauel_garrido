#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque


# In[2]:


turno = deque(["O", "X"])


# In[3]:


tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


# In[15]:


def cambiar_turno():
    turno.rotate()
    return turno[0]


# In[16]:


def mostrar_tablero():
    print("")
    for row in tablero:
        print([square for square in row])


# In[17]:


def procesar_posicion(posicion):
    fila, columna = posicion.split(",")
    return int(fila) - 1, int(columna) - 1


# In[18]:


def posicion_valida(posicion):
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False


# In[19]:


def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador


# In[20]:


def evaluar_victoria(j):
    if tablero[0] == [j, j, j] or tablero[1] == [j, j, j] or tablero[2] == [j, j, j]:
        return True
    elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
        return True
    elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
        return True
    elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
        return True
    elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
        return True
    elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
        return True
    return False
    


# In[21]:


def evaluar_empate():
    return set(tablero[0]).union(set(tablero[1])).union(set(tablero[2])) == set(["X", "O"])


# In[24]:


def juego():
    jugador = cambiar_turno()
    while True:
        posicion_str = input("Jugador {}, elige una posición (fila, columna) de 1 a 3. 'salir' o 'exit' para salir: ".format(jugador))
        if posicion_str == "salir" or posicion_str == "exit":
            print("Adios!")
            break
        try:
            posicion_procesada = procesar_posicion(posicion_str)
        except:
            print("Error, posición {} no es válida. formato debe ser (fila, columna)".format(posicion_str))
            continue
        if posicion_valida(posicion_procesada):
            actualizar_tablero(posicion_procesada, jugador)
            mostrar_tablero()
            if evaluar_victoria(jugador):
                print("Jugador {} ha ganado!. \nAdios!".format(jugador))
                break
            if evaluar_empate():
                print("Empate!.\nAdios!")
                break
            jugador = cambiar_turno()
        else:
            print("Posición {} no válida".format(posicion_str))
            
if __name__ == "__main__":
    juego()


# In[ ]:





# In[ ]:




