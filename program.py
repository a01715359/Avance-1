Nota = 0
print("Pregunta 1: ¿Cuál de las siguientes partes NO forma parte de una batería estándar? \
A) Bombo \
B) Hi-hat \
C) Maracas \
D) Tom")
resp_1 = str(input())
if resp_1 == "c" or resp_1 == "C":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")
        
print("Pregunta 2: Al sostener correctamente las baquetas, ¿cuál de estas afirmaciones es correcta? \
A) Se deben sostener con fuerza para que no se caigan \
B) Se deben sostener relajadas entre el pulgar y los dedos para permitir rebote \
C) Solo se debe usar el pulgar para controlarlas \
D) Se deben sostener paralelas al suelo en todo momento")
resp_2 = str(input())
if resp_2 == "B" or resp_2 == "b":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")

print("Pregunta 3: En una partitura de batería, el bombo se representa generalmente en: \
A) La línea inferior del pentagrama \
B) La línea superior del pentagrama \
C) Las notas con corcheas \
D) La línea del medio")
resp_3 = str(input())
if resp_3 == "A" or resp_3 == "a":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")

print("Pregunta 4: En la lectura de partituras de batería, el hi-hat cerrado suele representarse con: \
A) Una “x” sobre la línea superior \
B) Un círculo en la línea inferior \
C) Una línea ondulada en el pentagrama \
D) Una nota negra en la línea del medio")
resp_4 = str(input())
if resp_4 == "A" or resp_4 == "a":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")

print("Pregunta 5: ¿Qué es un fill en la batería? \
A) Un ritmo principal de la canción \
B) Un pequeño solo o transición para conectar secciones \
C) Solo tocar hi-hat \
D) La técnica de sostener las baquetas")
resp_5 = str(input())
if resp_5 == "B" or resp_5 == "b":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")

print("Pregunta 6: Un groove en batería se define como: \
A) Una serie de fills aleatorios \
B) El patrón rítmico principal que mantiene la canción en tiempo \
C) Solo tocar bombo y caja sin hi-hat \
D) Improvisar sin seguir la partitura")
resp_6 = str(input())
if resp_6 == "B" or resp_6 == "b":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")

print("Pregunta 7: En un fill de batería, es común: \
A) Mantener siempre el patrón principal sin cambios \
B) Cambiar el ritmo y usar toms, caja o bombo para crear variación \
C) Solo tocar hi-hat abierto \
D) Evitar tocar bombo")
resp_7 = str(input())
if resp_7 == "B" or resp_7 == "b":
    Nota +=1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")

print("Pregunta 8: ¿Cuál es la diferencia principal entre un groove y un fill? \
A) El groove es el patrón principal; el fill es una transición o adorno \
B) El groove es más rápido que el fill \
C) No hay diferencia \
D) El fill marca el tiempo principal")
resp_8 = str(input())
if resp_8 == "A" or resp_8 == "a":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")
    
print("Pregunta 9: ¿Qué debes hacer al practicar una nueva partitura de Rock? \
A) Tocar lo más rápido posible desde el inicio \
B) Practicar lentamente, contar el tiempo y mantener consistencia \
C) Solo tocar bombo y hi-hat \
D) Improvisar sin seguir la partitura")
resp_9 = str(input())
if resp_9 == "B" or resp_9 == "b":
    Nota += 1
    print("¡correcto!")
else:
    Nota += 0
    print("¡incorrecto!")
    
print("Pregunta DIFÍCIL (la respuesta correcta vale 2 puntos. Ojo: si la contestas mal se te restarán 2 puntos): \
Cuando lees una partitura de batería y ves una “x” en la línea superior, generalmente indica: \
A) Bombo \
B) Caja \
C) Hi-hat \
D) Tom de piso")
resp_10 = str(input())
if resp_10 == "C" or resp_10 == "c":
    Nota += 2
    print("¡correcto!")
else:
    Nota -= 2
    print("¡incorrecto!")
    
if Nota <= 6:
    print("Lo siento. Vuelve a tomar el examen para finalizar el curso")
    
if Nota >= 7:
    print("¡Felicitaciones, haz finalizado correctamente el curso!")
