from ClasesExamenes import *

pregunta1 = Pregunta("¿Cuál es la capital de España?", "Madrid", 1)
pregunta2 = Pregunta("¿Quién pintó La Mona Lisa?", "Leonardo da Vinci", 2)
pregunta3 = Pregunta("¿En qué año llegó el hombre a la luna?", "1969", 3)

enunciado = Enunciado("Examen de cultura general")
enunciado.agregar_pregunta(pregunta1)
enunciado.agregar_pregunta(pregunta2)
enunciado.agregar_pregunta(pregunta3)

examen = Examen(enunciado)
examen.responder(1, "Barcelona")
examen.responder(2, "Pablo Picasso")
examen.responder(3, "1968")

print("ID del examen:", examen.id)
print("Nombre del enunciado:", examen.enunciado.nombre)
print("Respuestas del examen:")
for pregunta, respuesta in examen.respuestas.items():
    print(pregunta.texto + " - Respuesta: " + respuesta)
