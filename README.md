# Avance-1
Contexto:
Mi proyecto será un curso de principiantes que enseñaría cómo tocar la batería. Explicaría paso a paso, desde lo más básico, como cuáles son las partes que conforman una batería, cómo sostener las baquetas o cómo leer las partituras de la batería; para finalmente dar un examen para evaluar los conocimientos obtenidos durante el curso. Pienso que sería interesante porque sería muy útil para personas que desean aprender a tocar algún instrumento pero no pueden pagar un curso o simplemente quieren buscar una forma más accesible de hacerlo: a través de un programa.

EO
Imprime “¡Bienvenido al curso! ¿Cuál es tu nombre?”
resp_nom = guardar nombre
Preguntar “¿Tienes conocimientos previos de batería?”
resp_con = guardar respuesta

Si res_con = Sí
    Imprime “Seleccione los temas que ya dominas: \
	    1. Partes de la batería \
	    2. Cómo agarrar correctamente las baquetas \
	    3. Cómo leer partituras de batería”
   
    val1 = Partes de la batería
    val2 = Cómo agarrar correctamente las baquetas
    val3 = Cómo leer partituras de batería
    con_pre = [val1, val2 , val3]
  
    Si con_pre = val1
        Omitir lección “Partes de la batería”
    Sino dar lección “Partes de la batería”

    Si con_pre = val2
        Omitir lección “Cómo agarrar correctamente las baquetas”
    Sino dar lección “Cómo agarrar correctamente las baquetas”

    Si con_pre = val3
        Omitir lección “Cómo leer partituras de batería”
    Sino dar lección “Cómo leer partituras de batería”

Sino res_con = No
    Dar las lecciones “Partes de la batería”, “Cómo agarrar correctamente las baquetas” y “Cómo leer partituras de batería”

Dar lección “Primera partitura : Rock 1”
    Imprime “Ahora aprenderás a tocar tu primera partitura. En la lección 3 aprendiste a cómo leer, ahora practicarás a tocarlas. Recuerda primero LEER la partitura, no intentes descifrar cómo sonaría porque eso solo te confundiría. Intenta primero entender lo que debes hacer para ahí ejecutarlo. Esta estructura está en un compás de 4/4, pero debes saber que hay más, y estas determinan cuántos pulsos o “golpes” se darían por tiempo.”
    Imprime “CONSEJO 1: No te preocupes si vas lento, y empieza paso por paso para ir acostumbrando a tu cuerpo y mejorar tu coordinación.”
    Imprime “Tiempo: 1      2      3      4
                    Hi-Hats: x  x  x  x  x  x  x  x
                    Tarola:           0              0
                    Bombo: 0              0”

    Imprime “Recuerda: Los Hi-Hats se tocan con la mano izquierda y que cuando están arriba de la partitura es porque están cerradas, por lo que mantén tu pie izquierdo en el pedal. La tarola se toca con la mano derecha y el bombo con el pie derecho”
    Imprime “CONSEJO 2: Antes de tocar y una vez hayas leídos analizado y entendido bien la partitura, asígnale un sonido a la tarola y el bombo, ay que estos son los que varían. Puede ser algo como “boom” para el bombo y “tap” para la tarola. Una vez lo tengas, practica instrumento por instrumento, no intentes unirlos todos juntos todavía, intenta dominar cada uno por separado. Luego, añade un sonido con la boca: cuando estés practicando la tarola, ve haciendo el sonido del bombo pero con tu boca, lo mismo cuando vayas a practicar el bombo. Y ahora sí: ¡Estás listo para unirlo todo! Ve al paso que necesites, no intentes acelerarte y recuerda que está bien confundirse.”
Fin lección “Primera partitura : Rock 1”

Dar lección “Segunda, tercera y cuarta partitura”
    Imprime “En la lección anterior aprendiste a tocar la primera partitura. En esta lección aprenderás a tocar otras nuevas tres.
    Imprime “Rock 2:
                   Tiempo: 1   &   2   &   3   &   4  &
                    Hi-Hats: x   x   x   x   x   x   x   x
                    Tarola:             0                  0
                    Bombo: 0                  0   0

                   Rock 3:
                   Tiempo: 1   &   2   &   3   &   4  &
                    Hi-Hats: x   x   x   x   x   x   x   x
                    Tarola:             0                  0
                    Bombo: 0             0   0

                   Rock 4:
                   Tiempo: 1   &   2   &   3   &   4  &
                    Hi-Hats: x   x   x   x   x   x   x   x
                    Tarola:             0                  0
                    Bombo: 0             0       0”
Imprime “CONSEJO: Recuerda primero leer, comprender bien la partitura y practicar cada instrumento por separado primero. Cuando tengas cada uno por separado, practica únicamente la tarola y el bombo respetando los tiempo, por lo que es recomendable utilizar un metrónomo para no adelantarte o atrasarte. Cuando ya los domines, añade los Hi-Hats. Lo puedes ver complicado, pero recuerda que los Hi-Hats son constantes, únicamente la Carola y el bombo están cambiando, pero si recuerdas como era el Rock 1, te darás cuenta que en estas nuevas partituras, la tarola sigue el mismo patrón en las cuatro, lo único que modificas es el bombo.”
Imprime “RETO: Cuando ya domines las cuatro, intenta unirlos, toca una octava de cada uno seguido. ¡Tu puedes!”
Fin lección “Segunda, tercera y cuarta partitura”

Dar lección “Fills”
    Imprime “En la lección anterior aprendiste otros tres Drum keys. En esta lección veremos qué son los fills. Los fills no son más que una pequeña desviación del ritmo principal (grooves). Suelen usarse para hacer transiciones entre ritmos o simplemente para darle un toque extra a la composición.”
    Imprime "Tiempo:  1 & 2 & 3 & 4 &
             Tom 1:       0 0     0 0
            Tarola:   x x     x x"
    Imprime “Una vez domines el fill, incorpóralo con cada uno de los drum keys estudiados. Juega y crea tus propias combinaciones, como hacer cuatro veces el Rock 1, luego una vez el Rock 4 y por último el fill dos veces; o todos una vez; o hacer Rock 1, fill, Rock 2, fill, Rock 3, fill, Rock 4, fill… ¡Tu decides!”
Fin lección “Fills”

Dar lección “Examen Final”
Nota = 0
    Imprime “¿Cuál de las siguientes partes NO forma parte de una batería estándar?
A) Bombo
B) Hi-hat
C) Maracas
D) Tom”
resp_1 = guardar respuesta
Si resp_1 = C) Maracas
    Nota = nota + 1
Sino Nota + 0

    Imprime “Al sostener correctamente las baquetas, ¿cuál de estas afirmaciones es correcta?
A) Se deben sostener con fuerza para que no se caigan
B) Se deben sostener relajadas entre el pulgar y los dedos para permitir rebote
C) Solo se debe usar el pulgar para controlarlas
D) Se deben sostener paralelas al suelo en todo momento”
resp_2 = guardar respuesta
Si resp_2 = B) Se deben sostener relajadas entre el pulgar y los dedos para permitir rebote
    Nota = nota + 1
Sino Nota + 0

    Imprime “En una partitura de batería, el bombo se representa generalmente en:
A) La línea inferior del pentagrama
B) La línea superior del pentagrama
C) Las notas con corcheas
D) La línea del medio”
resp_3 = guardar respuesta
Si resp_3 = A) La línea inferior del pentagrama
    Nota = nota + 1
Sino Nota + 0

Imprime “En la lectura de partituras de batería, el hi-hat cerrado suele representarse con:
A) Una “x” sobre la línea superior
B) Un círculo en la línea inferior
C) Una línea ondulada en el pentagrama
D) Una nota negra en la línea del medio”
resp_4 = guardar respuesta
Si resp_4 = A) Una “x” sobre la línea superior
    Nota = nota + 1
Sino Nota + 0

Imprime “¿Qué es un fill en la batería?
A) Un ritmo principal de la canción
B) Un pequeño solo o transición para conectar secciones
C) Solo tocar hi-hat
D) La técnica de sostener las baquetas”
resp_5 = guardar respuesta
Si resp_5 = B) Un pequeño solo o transición para conectar secciones
    Nota = nota + 1
Sino Nota + 0

Imprime “Un groove en batería se define como:
A) Una serie de fills aleatorios
B) El patrón rítmico principal que mantiene la canción en tiempo
C) Solo tocar bombo y caja sin hi-hat
D) Improvisar sin seguir la partitura”
resp_6 = guardar respuesta
Si resp_6 = B) El patrón rítmico principal que mantiene la canción en tiempo
    Nota = nota + 1
Sino Nota + 0

Imprime “En un fill de batería, es común:
A) Mantener siempre el patrón principal sin cambios
B) Cambiar el ritmo y usar toms, caja o bombo para crear variación
C) Solo tocar hi-hat abierto
D) Evitar tocar bombo”
resp_7 = guardar respuesta
Si resp_7 = B) Cambiar el ritmo y usar toms, caja o bombo para crear variación
    Nota = nota + 1
Sino Nota + 0

Imprime “¿Cuál es la diferencia principal entre un groove y un fill?
A) El groove es el patrón principal; el fill es una transición o adorno
B) El groove es más rápido que el fill
C) No hay diferencia
D) El fill marca el tiempo principal”
resp_8 = guardar respuesta
Si resp_8 = A) El groove es el patrón principal; el fill es una transición o adorno
    Nota = nota + 1
Sino Nota + 0

Imprime “¿Qué debes hacer al practicar una nueva partitura de Rock?
A) Tocar lo más rápido posible desde el inicio
B) Practicar lentamente, contar el tiempo y mantener consistencia
C) Solo tocar bombo y hi-hat
D) Improvisar sin seguir la partitura”
resp_9 = guardar respuesta
Si resp_9 = B) Practicar lentamente, contar el tiempo y mantener consistencia
    Nota = nota + 1
Sino Nota + 0

Imprime “Cuando lees una partitura de batería y ves una “x” en la línea superior, generalmente indica:
A) Bombo
B) Caja
C) Hi-hat
D) Tom de piso”
resp_10 = guardar respuesta
Si resp_10 = C) Hi-hat
    Nota = nota + 1
Sino Nota + 0

Mientras: 
	Nota <= 6
    Imprime “Lo siento. Vuelve a tomar el examen para finalizar el curso”
	repetir "Examen Final"
 Si Nota  >  6
   EF Imprime “¡Felicitaciones resp_nom, haz finalizado correctamente el curso”
