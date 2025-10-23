# Curso de batería
####Contexto

Muchos jóvenes quisieran aprender a tocar la batería, pero ya sea por cuestiones económicas o por tiempo, no pueden pagar un curso. 

Este proyecto tiene como objetivo brindar las bases de cómo tocar la batería para principiantes. Explicando paso a paso, desde lo más básico, como cuáles son las partes que conforman una batería, cómo sostener las baquetas o cómo leer las partituras de la batería; hasta temas más complejos, como cómo tocar ciertos ritmos en la batería. Finalmente, dará un examen para ver los conocimientos adquiridos.

- Para la realización de este proyecto se utilizó la biblioteca webbrowser, que sirve para acceder a URLs. Esta fue utilizada con el objetivo de proporcionar ayuda extra (videos) si el usuario no entendía la explicación del curso. Primero accedí a la biblioteca importándola para que Python reconozca sus funciones, luego creé una función para acceder a cada video, devolviendo cada elemento de una lista. Además, utilicé .open() para así abrir cada URL en una nueva página en el navegador predeterminado. Por último, mandé a llamar a la función creada, con la lista de los videos para que los reprodujera si el usuario los quería ver.

- Asimismo, también se usó la biblioteca de time para controlar el tiempo en el programa. Comúnmente, cuando se manda a imprimir algún mensaje en consola y el programa sigue con más instrucciones, todo se ejecuta instantáneamente. Sin embargo, como quería mostrar un mensaje en pantalla antes de mostrar un video, necesitaba que el programa esperara unos segundos para que así el usuario lo pueda leer con claridad. De lo contrario, el mensaje simplemente se imprime y seguido a eso se ejecuta la siguiente línea de código, sin esperar, haciendo que el usuario no tenga tiempo de leer el mensaje completo. Para lograr esa pausa, primero, accedí a la biblioteca de time importándola para que Python reconozca sus funciones; luego dentro de mi función para la reproducción de videos, usé time.sleep() después del mensaje, que sirve para suspender la ejecución del programa por la cantidad de segundos dada (que es el número que se coloca entre los paréntesis).

- Finalmente, también se usó la biblioteca de sys para forzar al programa a que cierre. En la parte final del programa, cuando revela la nota del examen y este obtiene 6 o menos, se le pregunta al usuario si lo quiere volver a tomar, y si el usuario entra una respuesta inválida y luego dice que no quiere volver a tomar el examen, se hubiera repetido un mensaje que no correspondía. Gracias al sys.exit, el programa se cierra y no lo muestra. Para eso, primero importé la biblioteca de sys, para que python reconozca sus funciones (esta biblioteca lo que permite es que el programa interactúe directamente con el sistema operativos), y luego dentro del ciclo while en la sección de notas, usé sys.exit() que sirve para cerrar el programa sin importar en qué parte del código se encuentre.

------------
### Algoritmo
    EO = Imprime“¡Bienvenido al curso! ¿Cuál es tu nombre?"
	resp_nom = guardar nombre
	Imprime“¿Tienes conocimientos previos de batería?”
	resp_con = guardar resp_con
	Si res_con = sí:
		Imprime“Dominas el tema 'Partes de la batería'? "
		dominar_1 = guardar dorminar_1
		Si dominar_1 = sí:
			Saltar lección
		Imprime“Dominas el tema 'Cómo agarrar correctamente las baquetas'? "
		dominar_2 = guardar dominar_2
		Si dominar_2 = sí:
			Saltar lección
		Imprime“Dominas el tema 'Cómo leer partituras de batería'? "
		dominar_3 = guardar dominar_3
		Si dominar_3 = sí:
			Saltar lección

	Si resp_con = no:
		Dar las lecciones: 
			  "Partes de la batería"
			“Cómo agarrar correctamente las baquetas"
			“Cómo leer partituras de batería”

    Dar lección “Primera partitura : Rock 1” 
	Imprime“Excelente! Ahora que ya sabes lo básico,
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
	Bombo:   0       0"

    Fin lección “Primera partitura : Rock 1”
    
    Imprime "List@ para la siguiente lección? (responde sí o no)". resp_video = guardar respuesta 
	Si resp_video == 'si' 
		continuar leccion 
	else if resp_video == 'no' 
		imprime "Te gustaría ver un video del tema?" 
		si respuesta == 'si' 
			mostrar video 
			else if respuesta == 'no' 
				continuar leccion 
	Mientras respuesta no igual a sí o no
		imprime 'respuesta invalida. debes decir si sí o si no'
	
    Dar lección “Segunda, tercera y cuarta partitura"
	Imprime “Genial! Ahora vamos a jugar un poco con los bombos 
	para así formar otros tres ritmos nuevos:
	Rock 2:
	Tiempo:  1 & 2 & 3 & 4 &
	Hi-Hats:  x  x x  x x  x  x x
	Tarola:          0           0
	Bombo:  0           0 0
	
	Rock 3:
	Tiempo:  1 & 2 & 3 & 4 &
	Hi-Hats:  x  x x  x x  x  x x
	Tarola:          0           0
	Bombo:  0        0 0
	
	Rock 4:
	Tiempo:  1 & 2 & 3 & 4 &
	Hi-Hats:  x  x x  x  x x  x x
	Tarola:          0           0
	Bombo:  0        0    0
	
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
	toca una octava de cada uno seguido. ¡Tu puedes!
	
	Fin lección“Segunda, tercera y cuarta partitura”
    
	Imprime "List@ para la siguiente lección? (responde sí o no)". resp_video = guardar respuesta 
	Si resp_video == 'si' 
		continuar leccion 
	else if resp_video == 'no' 
		imprime "Te gustaría ver un video del tema?" 
		si respuesta == 'si' 
			mostrar video 
			else if respuesta == 'no' 
				continuar leccion 
	Mientras respuesta no igual a sí o no
		imprime 'respuesta invalida. debes decir si sí o si no'
	
    
    Dar lección “Fills” 
	Imprime “Los fills no son más que una pequeña desviación del ritmo principal (grooves). Suelen usarse para hacer transiciones entre ritmos o simplemente para darle un toque extra a la composición.
	Tiempo:  1 & 2 & 3 & 4 &
	Tom 1:          0 0        0 0
	Tarola:    x x        x x
	
	Una vez domines el fill, incorpóralo 
	con cada uno de los drum keys estudiados. Juega y crea 
	tus propias combinaciones, como hacer cuatro veces el 
	Rock 1, luego una vez el Rock 4 y por último el fill 
	dos veces; o todos una vez; o hacer Rock 1, fill, 
	Rock 2, fill, Rock 3, fill, Rock 4, fill… ¡Tu decides!” 
	Fin lección “Fills”
    
	Imprime "List@ para la siguiente lección? (responde sí o no)". resp_video = guardar respuesta 
	Si resp_video == 'si' 
		continuar leccion 
	else if resp_video == 'no' 
		imprime "Te gustaría ver un video del tema?" 
		si respuesta == 'si' 
			mostrar video 
			else if respuesta == 'no' 
				continuar leccion 
	Mientras respuesta no igual a sí o no
		imprime 'respuesta invalida. debes decir si sí o si no'
    
    Dar lección “Examen Final” 
	Nota = 0 
	Imprime “¿Cuál de las siguientes partes NO forma parte de una batería estándar? 	A) Bombo 
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
    
    Imprime“En la lectura de partituras de batería, el hi-hat cerrado suele representarse con: 
	A) Una “x” sobre la línea superior 
	B) Un círculo en la línea inferior 
	C) Una línea ondulada en el pentagrama
	D) Una nota negra en la línea del medio” resp_4 = guardar respuesta 
	Si resp_4 = A) Una “x” sobre la línea superior 
		Nota = nota + 1
		Sino Nota + 0
    
    Imprime “¿Qué es un fill en la batería? 	A) Un ritmo principal de la canción 
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
	Si resp_8 = A) El groove es el patrón principal; el fill es una transición o adorno 		Nota = nota + 1 
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
    
    Imprime “Pregunta DIFÍCIL (la respuesta correcta vale 2 puntos. Ojo: si la contestas mal se te restarán 2 puntos): Cuando lees una partitura de batería y ves una “x” en la línea superior, generalmente indica: 
	A) Bombo 
	B) Caja 
	C) Hi-hat 
	D) Tom de piso” 
	resp_10 = guardar respuesta 
	Si resp_10 = C) Hi-hat 
		Nota = nota + 2 
		Sino Nota -2
    
    Mientras: Nota <= 6 
		Imprime “Lo siento. Vuelve a tomar el examen para finalizar el curso. Desea tomarlo nuevamente?"
		decision = guardar decision
		si decision = si
			repetir "Examen Final" 
		si decision = no
			Imprime "Bueno, te lo pierdes!"
		Mientras decision no sea "si" o "no"
			Imprime "Respuesta inválida. Debes decir si sí o si no"
	Si Nota >= 7 
	EF = Imprime “¡Felicitaciones resp_nom, haz finalizado correctamente el curso”

##### Instrucciones
Descarga el código, luego, ejecútalo en tu IDE de preferencia, o bien, en terminal.

#####Referencias:

webbrowser — Controlador de navegador web conveniente — documentación de Python - 3.10.19. (n.d.). https://docs.python.org/es/3.10/library/webbrowser.html

time — Time access and conversions. (n.d.). Python Documentation. https://docs.python.org/3/library/time.html

sys — System-specific parameters and functions. (n.d.-b). Python Documentation. https://docs.python.org/3/library/sys.html
