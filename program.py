"""
Proyecto Final
Curso de batería para principiantes
El programa tiene como objetivo enseñar los conceptos 
básicos de la batería. Al final, el programa realiza
un examen para evaluar el conocimiento adquirido y 
muestra su calificación final. Mientras el usuario no 
pase el examen, se le da la oportunidad de seguirlo tomando.
"""

#bibliotecas
import webbrowser

"""
================== Lecciones iniciales  =====================================
"""
nombre = input('¡Bienvenido al curso! ¿Cuál es tu nombre? \n')
conocimiento = input('Hola ' + nombre + ', ¿Tienes conocimientos previos de batería?\n').lower()
"""
 (uso de variables, listas anidadas, condicionales, condicionales anidados y ciclos)
 pregunta al usuario por su nombre y si tiene conocimientos previos de batería.
 Si el usuario tiene conocimientos previos, se le pregunta si domina cada tema 
 de la lista, para así saltarlos, si no conoce ninguno se le dan todos los temas.
 Mientras no responda sí o no, se le indica que su respuesta es inválida.
"""

lecciones_iniciales = [
["""Partes de la batería""", 
 """Lección: Partes de la batería
La batería se compone principalmente de tambores, platillos y 
herrajes (soportes y pedales):

Tambores: Son el elemento principal y consisten en una membrana (parche) 
tensada sobre un casco:

- Bombo: El tambor más grande, que se toca con un pedal de pie. 
Se encarga de producir las notas más graves
y marcar el pulso rítmico.

- Caja o tarola: Un tambor poco profundo que se coloca entre 
las piernas del baterista.
Se caracteriza por su sonido nítido y brillante, gracias a la bordona 
de alambres que tiene en la parte inferior.

- Toms: Tambores que complementan el ritmo de la caja y el bombo\n"""],
             
["""Cómo agarrar correctamente las baquetas""",
 """Lección: ¿Cómo agarrar correctamente las baquetas?

1. Dónde Agarrar: El Punto de Gira
Toma tu baqueta y sujétala a un tercio del final
    Es decir, no la agarres justo al final (el "mango"), ni a la mitad.
    Encuentra el punto donde la baqueta se siente equilibrada y 
    puede rebotar fácilmente si golpeas algo.
    Este es tu punto de control.
    
2. Cómo Agarrar: El Agarre Pinza
Usa solo dos dedos para sujetar este punto:
    La yema de tu pulgar.
    La yema de tu dedo índice (o el dedo del medio).
    Imagina que estás haciendo una pinza con esos dos dedos. 
    ¡Ellos hacen el trabajo principal!
Regla de Oro: La pinza debe ser firme, pero no apretada.
Debes agarrar lo suficiente para que la baqueta no se te caiga, 
pero lo suficientemente suave para que pueda moverse libremente 
y rebotar cuando golpeas. Si aprietas demasiado, te cansarás.

3. ¿Qué hacen los otros tres dedos?
    Simplemente descansan (abrazan) suavemente la baqueta.
    Ayudan a controlarla, pero no hacen fuerza. La fuerza 
    viene de tu muñeca, no de tu agarre.
    
4. La Posición para Empezar
    Pon las manos para que las palmas miren ligeramente hacia 
    abajo (hacia el suelo). Mantén los brazos y muñecas 
    muy relajados.\n"""],
             
["""Cómo leer partituras de batería""", 
 """lección: ¿Cómo leer partituras de batería?
La partitura de batería usa cinco líneas, llamadas pentagrama,
donde cada línea y cada espacio está asignado a una pieza 
específica de tu set. La forma más fácil de entender esto es que 
cuanto más alto está un símbolo en el pentagrama, más arriba o a la 
derecha está el instrumento en la batería real, y cuanto más bajo 
está, más cerca del suelo o del pedal está.

Empezando por la parte superior, los Platos son casi siempre 
representados por una "X". Por ejemplo, el Plato Hi-Hat 
(el que abres y cierras con el pedal) se escribe justo sobre
la quinta línea (la más alta). El Plato Ride (el más grande, 
que usas para ritmos suaves) se encuentra un poco más abajo, 
en el cuarto espacio. Si ves una "X" más arriba de todo, por encima 
del pentagrama, normalmente es el Plato Crash (el que usas para 
acentuar un golpe fuerte). En el medio de las líneas es donde 
se encuentran todos los Tambores. La pieza más importante, la Caja 
(Snare Drum), se escribe justo en el tercer espacio del pentagrama. 
Los Toms (los tambores que golpeas con las baquetas)se colocan en 
diferentes lugares: el Tom 1 (el más pequeño) se escribe en el 
segundo espacio, el Tom 2 (el mediano) se coloca en la tercera 
línea, y el Tom de Piso (Floor Tom, el más grande que está de pie) 
ocupa la cuarta línea.

Finalmente, en la parte inferior de la partitura está 
todo lo que tocas con el pie. El Bombo (Kick Drum), que es el 
tambor más grande y suena grave, se representa debajo de la 
primera línea (el símbolo está en un espacio extra imaginario). 
El Pedal del Hi-Hat (el que usas para cerrar los platos con el pie) 
se encuentra justo en el primer espacio del pentagrama. Así, al ver 
la partitura, solo tienes que mirar la altura del símbolo: si está 
abajo, es el pie; si está en el medio, es la caja o un tom; y si 
está arriba con una "X", ¡es un plato!\n"""]]

while conocimiento != 'sí' and conocimiento != 'si' and conocimiento != 'no':
        conocimiento = input('respuesta inválida. Debes decir si sí o si no\n').lower()

if conocimiento == 'si' or conocimiento == 'sí':
    for fila in lecciones_iniciales:
        print('Dominas el tema "' + fila[0] + '"?')
        respuesta = input().lower()

        if respuesta == 'sí' or respuesta == 'si':
            print('Perfecto! Nos saltaremos esta lección')
                
        elif respuesta == 'no':
            print('No te preocupes!')
            print(fila[1])
        else:
            print('respuesta inválida. Debes decir si sí o si no')
elif conocimiento == 'no':
    print("No te preocupes, empezaremos desde 0")
    i = 0
    while i < len(lecciones_iniciales):
        print(lecciones_iniciales[i][1])
        i += 1

"""
================== Lecciones =====================================
"""

"""
 (uso de listas, listas anidadas, funciones, condicionales, condicionales anidados, ciclos y ciclos anidados)
 Se crea la lista de lecciones finales, cada lección es un string.
 """
lecciones_finales = [
"""Excelente! Ahora que ya sabes lo básico, 
podemos comenzar con la primera partitura: "Rock 1"
Recuerda primero LEER la partitura, no intentes 
descifrar cómo sonaría porque eso solo te confundiría.
Intenta primero entender lo que debes hacer para ahí 
ejecutarlo. Esta estructura está en un compás de 4/4, 
pero debes saber que hay más, y estas determinan 
cuántos pulsos o “golpes” se darían por tiempo.
CONSEJO 1: No te preocupes si vas lento, y empieza 
paso por paso para ir acostumbrando a tu cuerpo
y mejorar tu coordinación.
Tiempo:  1 & 2 & 3 & 4 &
Hi-Hats: x   x   x   x 
Tarola:      0       0
Bombo:   0       0""", 

"""Genial! Ahora vamos a jugar un poco con los bombos 
para así formar otros tres ritmos nuevos:
Rock 2:
Tiempo:  1 & 2 & 3 & 4 &
Hi-Hats: x x x x x x x x
Tarola:      0       0
Bombo:   0       0 0

Rock 3:
Tiempo:  1 & 2 & 3 & 4 &
Hi-Hats: x x x x x x x x
Tarola:      0       0
Bombo:   0     0 0
 
Rock 4:
Tiempo:  1 & 2 & 3 & 4 &
Hi-Hats: x x x x x x x x
Tarola:      0       0
Bombo:   0     0   0

Recuerda primero leer, comprender bien la partitura 
y practicar cada instrumento por separado primero.
Cuando tengas cada uno por separado, practica 
únicamente la tarola y el bombo respetando los tiempos, 
por lo que es recomendable utilizar un metrónomo 
para no adelantarte o atrasarte. Cuando ya los domines, 
añade los Hi-Hats. Lo puedes ver complicado, pero 
recuerda que los Hi-Hats y la tarola son constantes,
únicamente el bombo están cambiando.

RETO: Cuando ya domines las cuatro, intenta unirlos,
toca una octava de cada uno seguido. ¡Tu puedes!""",

"""Los fills no son más que una pequeña desviación del
ritmo principal (grooves). Suelen usarse para hacer 
transiciones entre ritmos o simplemente para darle 
un toque extra a la composición.

Tiempo:  1 & 2 & 3 & 4 &
Tom 1:       0 0     0 0
Tarola:  x x     x x

Una vez domines el fill, incorpóralo 
con cada uno de los drum keys estudiados. Juega y crea 
tus propias combinaciones, como hacer cuatro veces el 
Rock 1, luego una vez el Rock 4 y por último el fill 
dos veces; o todos una vez; o hacer Rock 1, fill, 
Rock 2, fill, Rock 3, fill, Rock 4, fill… ¡Tu decides!"""]

videos = [['https://youtu.be/HqQT28ro4q8?si=e2s1JW1k4DQDrWjw'], 
          ['https://youtu.be/G4k9l4pCqt0?si=_qm9A1QrSH3QqDpC', 
          'https://youtu.be/Y4Crq9UmAA8?si=a4tXLwteDuT7AFcR', 
          'https://youtu.be/gI8IpM5hq74?si=lv5qonCrzyQAzgpb'], 
          ['https://youtu.be/sZx7Z_4--Yg?si=GCTWOoTrxnUNvmDD']]

def reproducir_video(url_video):
    """Abre un video de YouTube en el navegador web predeterminado."""
    return webbrowser.open(url_video)

def lecciones(leccion, video):
    """
    recibe: leccion (cada lección de la lista) string y video (lista de videos) string
    Imprime lección y pregunta si el usuario está listo para la siguiente.
    Si responde que sí, continua con la siguiente lección; si responde que no 
    se le pregunta si desea ver un video de la lección, si responde que sí 
    se lo muestra y le pide que luego de ver el video diga listo/a para continuar; 
    y si responde que no continua con la siguiente lección.
    Mientras no responda sí o no, se le indica que su respuesta es inválida.
    Se llama a la función con la lista de lecciones y la lista de videos.
    """
    for i in range(len(leccion)):
        print(leccion[i])
        option = input('List@ para la siguiente lección? (responde sí o no)\n').lower()
        
        if option == 'sí' or option == 'si':
            continue
        elif option == 'no':
            respuesta = input("Te gustaría ver un video del tema?\n").lower()
            if respuesta == 'sí' or respuesta == 'si':
                for url in videos[i]:
                    reproducir_video(url)
                respuesta = input('Cuando termines de ver el video, debes decir "listo" o "lista" para continuar\n').lower()
                while respuesta != 'lista' and respuesta != 'listo':
                    respuesta = input('respuesta inválida. Debes decir "listo" o "lista"\n').lower()

            elif respuesta == 'no':
                continue
            
            else:
                while option != 'sí' and option != 'si' and option != 'no':
                    option = input('respuesta inválida. Debes decir si sí o si no\n').lower()
    
        else:
            while option != 'sí' and option != 'si' and option != 'no':
                option = input('respuesta inválida. Debes decir si sí o si no\n').lower()
                if option == 'sí' or option == 'si':
                    continue
                
lecciones(lecciones_finales, videos)

"""
========  parte principal del programa ========================================
"""
#creación de funciones para el examen final
def examen(pregunta, respuesta_correcta):
    """
    (uso de funciones y condicionales)
    recibe: pregunta (string), respuesta_correcta (string)
    Imprime la pregunta y recibe la respuesta del usuario.
    Si la respuesta es correcta, imprime "¡correcto!", de lo contrario
    imprime "¡incorrecto!"
    devuelve: 1 si es correcta, 0 si es incorrecta.
    """
    respuesta = str(input(pregunta))
    if respuesta.lower() == respuesta_correcta:
        print("¡correcto!")
        return 1
    else:
        print("¡incorrecto!")
        return 0

def examen_preg_dificil(pregunta, respuesta_correcta):
    """
    (uso de funciones y condicionales)
    recibe: pregunta (string), respuesta_correcta (string)
    Imprime la pregunta y recibe la respuesta del usuario.
    Si la respuesta es correcta, imprime "¡correcto!", de lo contrario
    imprime "¡incorrecto!"
    devuelve: 2 si es correcta, -2 si es incorrecta.
    """
    respuesta = str(input(pregunta))
    if respuesta.lower() == respuesta_correcta:
        print("¡correcto!")
        return 2
    else:
        print("¡incorrecto!")
        return -2

print("""\nEXAMEN FINAL: AHORA TENDRÁS UN EXAMEN PARA PONER
A PRUEBA LO APRENDIDO DURANTE ESTE CURSO.
Responde las preguntas para que logres pasar el curso.\n""")

"""
================== preguntas del examen =======================================
"""

"""
(uso de diccionarios)
"""

preguntas = {
"¿Cuál de las siguientes partes NO forma parte de una batería \
estándar? \nA) Bombo \nB) Hi-hat \nC) Maracas \nD) Tom\n": 'c',

"Al sostener correctamente las baquetas, ¿cuál de estas afirmaciones \
es correcta? \nA) Se deben sostener con fuerza para que no se caigan \
\nB) Se deben sostener relajadas entre el pulgar y los dedos para \
permitir rebote \nC) Solo se debe usar el pulgar para controlarlas \
\nD) Se deben sostener paralelas al suelo en todo momento\n": 'b',

"En una partitura de batería, el bombo se representa generalmente \
en: \nA) La línea inferior del pentagrama \nB) La línea superior del \
pentagrama \nC) Las notas con corcheas \nD) La línea del medio\n": 'a',

"En la lectura de partituras de batería, el hi-hat cerrado suele \
representarse con: \nA) Una “x” sobre la línea superior \nB) Un círculo \
en la línea inferior \nC) Una línea ondulada en el pentagrama \nD) Una \
nota negra en la línea del medio\n": 'a',

"¿Qué es un fill en la batería? \nA) Un ritmo principal de la canción \
\nB) Un pequeño solo o transición para conectar secciones \nC) Solo \
tocar hi-hat \nD) La técnica de sostener las baquetas\n": 'b',

"Un groove en batería se define como: \nA) Una serie de fills aleatorios \
\nB) El patrón rítmico principal que mantiene la canción en tiempo \nC) \
Solo tocar bombo y caja sin hi-hat \nD) Improvisar sin seguir la \
partitura\n": 'b',

"En un fill de batería, es común: \nA) Mantener siempre el patrón principal \
sin cambios \nB) Cambiar el ritmo y usar toms, caja o bombo para crear \
variación \nC) Solo tocar hi-hat abierto \nD) Evitar tocar bombo\n": 'b',

"¿Cuál es la diferencia principal entre un groove y un fill? \nA) El groove \
es el patrón principal; el fill es una transición o adorno \nB) El groove \
es más rápido que el fill \nC) No hay diferencia \nD) El fill marca el \
tiempo principal\n": 'a',

"¿Qué debes hacer al practicar una nueva partitura de Rock? \nA) Tocar lo más \
rápido posible desde el inicio \nB) Practicar lentamente, contar el tiempo \
y mantener consistencia \nC) Solo tocar bombo y hi-hat \nD) Improvisar \
sin seguir la partitura\n": 'b',

"Pregunta DIFÍCIL (la respuesta correcta vale 2 puntos. Ojo: si la contestas \
mal se te restarán 2 puntos): \nCuando lees una partitura de batería y ves \
una “x” en la línea superior, generalmente indica: \nA) Bombo \nB) Caja \
\nC) Hi-hat \nD) Tom de piso\n": 'c'
             }
 #calcular la nota final del examen
def n(question):
    """
    (uso de funciones, ciclos y condicionales)
    recibe: question (diccionario con las preguntas y respuestas correctas)
    empieza la nota en 0 y un índice en 0
    recorre cada clave (pregunta) del diccionario
    si el índice es 9 (pregunta difícil) llama a la función examen_preg_dificil
    si no, llama a la función examen
    suma la nota obtenida en cada pregunta a la nota total y aumenta 1 a índice, 
    para recorer a la siguiente.
    devuelve: la nota obtenida
    """
    nota = 0
    indice = 0
    for clave in preguntas:
        respuesta = preguntas[clave]
        if indice == 9:
            nota += examen_preg_dificil(clave, respuesta)
        else:
            nota += examen(clave, respuesta)
        indice += 1
    return nota

nota = n(preguntas)

"""
================== resultado del examen =======================================
"""

"""
(uso de ciclos y condicionales)
Se imprime la nota final obtenida en el examen.
Mientras que esta sea menor o igual a 6, se le indica 
que no ha pasado el examen y se le da la opción de volverlo a tomar.
Si decide tomarlo nuevamente, la nota se reinicia a 0 y se llama a la 
función n para volver a tomarlo. Si decide no tomarlo, se le indica que
se lo pierde.
Si la nota es menor a 0, se convierte a 0. 
Si la nota es mayor o igual a 7, se le indica que ha pasado el examen 
y se le felicita.
"""
while nota <= 6:
    if nota < 0:
            nota = 0
    print("Tu puntaje final es:", nota)
    print("Lo siento. Vuelve a tomar el examen para finalizar el curso")
    decision = str(input("¿Desea tomarlo nuevamente? \n")).lower()
    if decision == "si" or decision == "sí":
        nota = 0
        nota = n(preguntas)
    
    else:
        print('Bueno, te lo pierdes!')
        break

if nota >= 7:
    print("Tu puntaje final es:", nota)
    print("¡Felicitaciones,", nombre, "haz finalizado correctamente el curso!")
