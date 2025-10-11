#Para el avance 7 añadí listas anidades (matrices) para la selección de los temas dominados en el curso.
Nombre = input('¡Bienvenido al curso! ¿Cuál es tu nombre? \n')
Conocimiento = input('Hola ' + Nombre + ', ¿Tienes conocimientos previos de batería?').lower()

lecciones = [["Partes de la batería", '\nLección: Partes de la batería \n \
\nLa batería se compone principalmente de tambores, platillos y herrajes (soportes y pedales): \n \
Tambores: \n \
Son el elemento principal y consisten en una membrana (parche) tensada sobre un casco: \n \
Bombo: El tambor más grande, que se toca con un pedal de pie. Se encarga de producir las notas más graves \
y marcar el pulso rítmico. \n \
Caja o tarola: Un tambor poco profundo que se coloca entre las piernas  baterista. \
Se caracteriza por su sonido nítido y brillante, gracias a la bordona de alambres que tiene en la parte inferior. \n \
Toms: Tambores que complementan el ritmo de la caja y el bombo\n'],
             
             ["Cómo agarrar correctamente las baquetas", '\nLección: ¿Cómo agarrar correctamente las baquetas? \n \
\n1. Dónde Agarrar: El Punto de Gira \n \
Toma tu baqueta y sujétala a un tercio del final \n \
    Es decir, no la agarres justo al final (el "mango"), ni a la mitad. \n \
    Encuentra el punto donde la baqueta se siente equilibrada y puede rebotar fácilmente si golpeas algo. \n \
    Este es tu punto de control. \n \
\n2. Cómo Agarrar: El Agarre Pinza \n \
Usa solo dos dedos para sujetar este punto: \n \
    La yema de tu pulgar. \n \
    La yema de tu dedo índice (o el dedo del medio). \n \
    Imagina que estás haciendo una pinza con esos dos dedos. ¡Ellos hacen el trabajo principal! \n \
Regla de Oro: La pinza debe ser firme, pero no apretada. \
Debes agarrar lo suficiente para que la baqueta no se te caiga, pero lo suficientemente suave \
para que pueda moverse libremente y rebotar cuando golpeas. Si aprietas demasiado, te cansarás. \n \
\n3. ¿Qué hacen los otros tres dedos? \n \
    Simplemente descansan (abrazan) suavemente la baqueta. \n \
    Ayudan a controlarla, pero no hacen fuerza. La fuerza viene de tu muñeca, no de tu agarre. \n \
\n4. La Posición para Empezar \n \
    Pon las manos para que las palmas miren ligeramente hacia abajo (hacia el suelo). \n \
    Mantén los brazos y muñecas muy relajados.\n'],
             
             ["Cómo leer partituras de batería", '\nlección: ¿Cómo leer partituras de batería? \n \
\nLa partitura de batería usa cinco líneas, llamadas pentagrama, \
donde cada línea y cada espacio está asignado a una pieza específica de tu set. \
La forma más fácil de entender esto es que cuanto más alto está un símbolo en el pentagrama, \
más arriba o a la derecha está el instrumento en la batería real, y cuanto más bajo está, más \
cerca del suelo o del pedal está. \n \
\nEmpezando por la parte superior, los Platos son casi siempre representados por una "X". \
Por ejemplo, el Plato Hi-Hat (el que abres y cierras con el pedal) se escribe justo sobre \
la quinta línea (la más alta). El Plato Ride (el más grande, que usas para ritmos suaves) \
se encuentra un poco más abajo, en el cuarto espacio. Si ves una "X" más arriba de todo, \
por encima del pentagrama, normalmente es el Plato Crash (el que usas para acentuar un golpe fuerte). \n \
\nEn el medio de las líneas es donde se encuentran todos los Tambores. La pieza más importante, la Caja (Snare Drum), \n \
se escribe justo en el tercer espacio del pentagrama. Los Toms (los tambores que golpeas con las baquetas) \
se colocan en diferentes lugares: el Tom 1 (el más pequeño) se escribe en el segundo espacio, el Tom 2 (el mediano) \
se coloca en la tercera línea, y el Tom de Piso (Floor Tom, el más grande que está de pie) ocupa la cuarta línea. \n \
\nFinalmente, en la parte inferior de la partitura está todo lo que tocas con el pie. El Bombo (Kick Drum), \
que es el tambor más grande y suena grave, se representa debajo de la primera línea \
(el símbolo está en un espacio extra imaginario). El Pedal del Hi-Hat (el que usas para cerrar los platos con el pie) \
se encuentra justo en el primer espacio del pentagrama. Así, al ver la partitura, solo tienes que mirar la altura del \
símbolo: si está abajo, es el pie; si está en el medio, es la caja o un tom; y si está arriba con una "X", ¡es un plato!\n']]
            

if Conocimiento == 'si' or Conocimiento == 'sí':
    for fila in lecciones:
        print('Dominas el tema "' + fila[0] + '"?')
        respuesta = input().lower()

        if respuesta == 'sí' or respuesta == 'si':
            print('Perfecto! Nos saltaremos esta leccion')
            
        elif respuesta == 'no':
            print('No te preocupes!')
            print(fila[1])
        else:
            print('respuesta inválida. Debes decir si sí o si no')
else:
    print("No te preocupes, empezaremos desde 0")
    i = 0
    while i < len(lecciones):
        print(lecciones[i][1])
        i += 1
        

print('Perfecto! Ahora que ya sabes lo básico, podemos comenzar con la primera partitura: "Rock 1" \n \
\nRecuerda primero LEER la partitura, no intentes descifrar cómo sonaría porque eso solo te confundiría. \n \
Intenta primero entender lo que debes hacer para ahí ejecutarlo. Esta estructura está en un compás de 4/4, \
pero debes saber que hay más, y estas determinan cuántos pulsos o “golpes” se darían por tiempo. \n \
\nCONSEJO 1: No te preocupes si vas lento, y empieza paso por paso para ir acostumbrando a tu cuerpo \
y mejorar tu coordinación. \n \
Tiempo:  1 & 2 & 3 & 4 &\n \
Hi-Hats: x x x x x x x x\n \
Tarola:      0       0\n \
Bombo:   0       0\n')

print('Genial! Ahora vamos a jugar un poco con los bombos para así formar otros tres ritmos nuevos: \n \
\nRock 2: \n \
Tiempo:  1 & 2 & 3 & 4 &\n \
Hi-Hats: x x x x x x x x\n \
Tarola:      0       0\n \
Bombo:   0       0 0\n \
\nRock 3: \n \
Tiempo:  1 & 2 & 3 & 4 &\n \
Hi-Hats: x x x x x x x x\n \
Tarola:      0       0\n \
Bombo:   0     0 0\n \
\nRock 4: \n \
Tiempo:  1 & 2 & 3 & 4 &\n \
Hi-Hats: x x x x x x x x\n \
Tarola:      0       0\n \
Bombo:   0     0   0\n')

print('\nRecuerda primero leer, comprender bien la partitura y \
practicar cada instrumento por separado primero. \n \
\nCuando tengas cada uno por separado, practica únicamente la tarola y \
el bombo respetando los tiempo, por lo que es recomendable utilizar \
un metrónomo para no adelantarte o atrasarte. Cuando ya los domines, añade los Hi-Hats. \n \
Lo puedes ver complicado, pero recuerda que los Hi-Hats y la tarola son constantes, \
únicamente el bombo están cambiando\n.')

print('\nRETO: Cuando ya domines las cuatro, intenta unirlos, \
toca una octava de cada uno seguido. ¡Tu puedes!\n')

print('Los fills no son más que una pequeña desviación del \
ritmo principal (grooves). Suelen usarse para hacer transiciones entre \
ritmos o simplemente para darle un toque extra a la composición.')

print('\
Tiempo:  1 & 2 & 3 & 4 &\n \
Tarola:  0 0 0 0 0 0 0 0\n \
Hi-Hats: x   x   x   x\n')

print('Si te fijas, esta vez los Hi-Hats están debajo, lo que quiere \
decir que ya no usarás las manos para tocarlos, sino que está vez tu \
pie izquierdo ya no estará presionando el pedal siempre. \nPor otro lado, \
en este fill la tarola es la constante, para ello, empieza con la mano \
derecha y luego ve con la izquierda. Observa como los Hi-Hats únicamente \
los tocas cuando utilizas tu mano derecha, tener esto claro te ayudará \
con tu coordinación. Una vez domines el fill, incorpóralo con cada uno \
de los drum keys estudiados. Juega y crea tus propias combinaciones, \
como hacer cuatro veces el Rock 1, luego una vez el Rock 4 y por último \
el fill dos veces; o todos una vez; o hacer Rock 1, fill, Rock 2, fill, \
Rock 3, fill, Rock 4, fill… ¡Tu decides!')


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

print('EXAMEN FINAL: Responde las preguntas para que logres pasar el curso.\n')
preguntas = ["¿Cuál de las siguientes partes NO forma parte de una batería estándar? \nA) Bombo \nB) Hi-hat \nC) Maracas \nD) Tom\n",
             "Al sostener correctamente las baquetas, ¿cuál de estas afirmaciones es correcta? \nA) Se deben sostener con fuerza para que no se caigan \nB) Se deben sostener relajadas entre el pulgar y los dedos para permitir rebote \nC) Solo se debe usar el pulgar para controlarlas \nD) Se deben sostener paralelas al suelo en todo momento\n",
             "En una partitura de batería, el bombo se representa generalmente en: \nA) La línea inferior del pentagrama \nB) La línea superior del pentagrama \nC) Las notas con corcheas \nD) La línea del medio\n",
             "En la lectura de partituras de batería, el hi-hat cerrado suele representarse con: \nA) Una “x” sobre la línea superior \nB) Un círculo en la línea inferior \nC) Una línea ondulada en el pentagrama \nD) Una nota negra en la línea del medio\n",
             "¿Qué es un fill en la batería? \nA) Un ritmo principal de la canción \nB) Un pequeño solo o transición para conectar secciones \nC) Solo tocar hi-hat \nD) La técnica de sostener las baquetas\n",
             "Un groove en batería se define como: \nA) Una serie de fills aleatorios \nB) El patrón rítmico principal que mantiene la canción en tiempo \nC) Solo tocar bombo y caja sin hi-hat \nD) Improvisar sin seguir la partitura\n",
             "En un fill de batería, es común: \nA) Mantener siempre el patrón principal sin cambios \nB) Cambiar el ritmo y usar toms, caja o bombo para crear variación \nC) Solo tocar hi-hat abierto \nD) Evitar tocar bombo\n",
             "¿Cuál es la diferencia principal entre un groove y un fill? \nA) El groove es el patrón principal; el fill es una transición o adorno \nB) El groove es más rápido que el fill \nC) No hay diferencia \nD) El fill marca el tiempo principal\n",
             "¿Qué debes hacer al practicar una nueva partitura de Rock? \nA) Tocar lo más rápido posible desde el inicio \nB) Practicar lentamente, contar el tiempo y mantener consistencia \nC) Solo tocar bombo y hi-hat \nD) Improvisar sin seguir la partitura\n",
             "Pregunta DIFÍCIL (la respuesta correcta vale 2 puntos. Ojo: si la contestas mal se te restarán 2 puntos): \nCuando lees una partitura de batería y ves una “x” en la línea superior, generalmente indica: \nA) Bombo \nB) Caja \nC) Hi-hat \nD) Tom de piso\n"]

respuestas = ['c', 'b', 'a', 'a', 'b', 'b', 'b', 'a', 'b', 'c']

def n():
    Nota = 0
    for i in range(len(preguntas)):
        if i == 9:
            Nota += examen_preg_dificil(preguntas[i], respuestas[i])
        else:
            Nota += examen(preguntas[i], respuestas[i])
    return Nota

Nota = n()

while Nota <= 6:
    print("Tu puntaje final es:", Nota)
    print("Lo siento. Vuelve a tomar el examen para finalizar el curso")
    decision = str(input("¿Desea tomarlo nuevamente? \n")).lower()
    if decision == "si" or decision == "sí":
        Nota = 0
        Nota = n()
        if Nota < 0:
            Nota = 0
    else:
        print('Bueno, te lo pierdes!')
        break
    
if Nota >= 7:
    print("Tu puntaje final es:", Nota)
    print("¡Felicitaciones, haz finalizado correctamente el curso!")
