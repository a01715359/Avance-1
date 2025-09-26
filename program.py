
#AVANCE 5: Para el avance 5 seleccioné añadir while al mismo código del "Examen Final"
Nota_final = 0
def examen(pregunta, respuesta_correcta):
    respuesta = str(input(pregunta))
    if respuesta.lower() == respuesta_correcta:
        print("¡correcto!")
        return 1
    else:
        print("¡incorrecto!")
        return 0
def examen_preg_dificil(pregunta, respuesta_correcta):
    respuesta = str(input(pregunta))
    if respuesta.lower() == respuesta_correcta:
        print("¡correcto!")
        return 2
    else:
        print("¡incorrecto!")
        return -2

def preguntas():
    Nota = 0
    Nota += examen("Pregunta 1: ¿Cuál de las siguientes partes NO forma parte de una batería estándar? \nA) Bombo \nB) Hi-hat \nC) Maracas \nD) Tom\n", "c")
    Nota += examen("Pregunta 2: Al sostener correctamente las baquetas, ¿cuál de estas afirmaciones es correcta? \nA) Se deben sostener con fuerza para que no se caigan \nB) Se deben sostener relajadas entre el pulgar y los dedos para permitir rebote \nC) Solo se debe usar el pulgar para controlarlas \nD) Se deben sostener paralelas al suelo en todo momento\n", "b")
    Nota += examen("Pregunta 3: En una partitura de batería, el bombo se representa generalmente en: \nA) La línea inferior del pentagrama \nB) La línea superior del pentagrama \nC) Las notas con corcheas \nD) La línea del medio\n", "a")
    Nota += examen("Pregunta 4: En la lectura de partituras de batería, el hi-hat cerrado suele representarse con: \nA) Una “x” sobre la línea superior \nB) Un círculo en la línea inferior \nC) Una línea ondulada en el pentagrama \nD) Una nota negra en la línea del medio\n", "a")
    Nota += examen("Pregunta 5: ¿Qué es un fill en la batería? \nA) Un ritmo principal de la canción \nB) Un pequeño solo o transición para conectar secciones \nC) Solo tocar hi-hat \nD) La técnica de sostener las baquetas\n", "b")
    Nota += examen("Pregunta 6: Un groove en batería se define como: \nA) Una serie de fills aleatorios \nB) El patrón rítmico principal que mantiene la canción en tiempo \nC) Solo tocar bombo y caja sin hi-hat \nD) Improvisar sin seguir la partitura\n", "b")
    Nota += examen("Pregunta 7: En un fill de batería, es común: \nA) Mantener siempre el patrón principal sin cambios \nB) Cambiar el ritmo y usar toms, caja o bombo para crear variación \nC) Solo tocar hi-hat abierto \nD) Evitar tocar bombo\n", "b")
    Nota += examen("Pregunta 8: ¿Cuál es la diferencia principal entre un groove y un fill? \nA) El groove es el patrón principal; el fill es una transición o adorno \nB) El groove es más rápido que el fill \nC) No hay diferencia \nD) El fill marca el tiempo principal\n", "a")
    Nota += examen("Pregunta 9: ¿Qué debes hacer al practicar una nueva partitura de Rock? \nA) Tocar lo más rápido posible desde el inicio \nB) Practicar lentamente, contar el tiempo y mantener consistencia \nC) Solo tocar bombo y hi-hat \nD) Improvisar sin seguir la partitura\n", "b")
    Nota += examen_preg_dificil("Pregunta DIFÍCIL (la respuesta correcta vale 2 puntos. Ojo: si la contestas mal se te restarán 2 puntos): \nCuando lees una partitura de batería y ves una “x” en la línea superior, generalmente indica: \nA) Bombo \nB) Caja \nC) Hi-hat \nD) Tom de piso\n", "c")
    return Nota

Nota_final = preguntas()

if Nota_final < 0:
        Nota_final = 0

# Lo que intenté hacer aquí es crear un ciclo que haga que el usuario pueda tomar el examen otra vez mientras saque menos de 7 puntos
while Nota_final <= 6:
    print("Tu puntaje final es:", Nota_final)
    print("Lo siento. Vuelve a tomar el examen para finalizar el curso")
    decision = str(input("¿Desea tomarlo nuevamente? \n")).lower()
    if decision == "si" or decision == "sí":
       Nota_final = preguntas()
       if Nota_final < 0:
            Nota_final = 0
    else:
        print("¡Gracias por participar!")
        break

if Nota_final > 6:
    print("Tu puntaje final es:", Nota_final)
    print("¡Felicitaciones, haz finalizado correctamente el curso!")
