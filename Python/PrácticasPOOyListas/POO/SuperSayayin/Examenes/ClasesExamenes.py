class Pregunta:
    def __init__(self, texto, respuesta_correcta, dificultad=0):
        self.texto = texto
        self.respuesta_correcta = respuesta_correcta
        self.dificultad = dificultad
    
class Enunciado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []
    
    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
    
    def obtener_pregunta(self, numero):
        if numero < 1 or numero > len(self.preguntas):
            return None
        return self.preguntas[numero-1]
    
    def permutar_pregunta(self, numero1, numero2):
        if numero1 < 1 or numero1 > len(self.preguntas) or numero2 < 1 or numero2 > len(self.preguntas):
            return False
        self.preguntas[numero1-1], self.preguntas[numero2-1] = self.preguntas[numero2-1], self.preguntas[numero1-1]
        return True
    
    def borrar_pregunta_numero(self, numero):
        if numero < 1 or numero > len(self.preguntas):
            return False
        self.preguntas.pop(numero-1)
        return True
    
    def borrar_pregunta(self, pregunta):
        if pregunta in self.preguntas:
            self.preguntas.remove(pregunta)
            return True
        return False
    
    def contiene_pregunta(self, pregunta):
        return pregunta in self.preguntas
        
class Examen:
    contador_id = 1
    
    def __init__(self, enunciado):
        self.id = Examen.contador_id
        Examen.contador_id += 1
        self.enunciado = enunciado
        self.respuestas = {}
    
    def responder(self, numero_pregunta, respuesta):
        pregunta = self.enunciado.obtener_pregunta(numero_pregunta)
        if pregunta is None:
            return False
        self.respuestas[pregunta] = respuesta
        return True
