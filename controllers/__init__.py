class paciente:
    def __init__(self, nombre, apellido, edad, numero_expediente, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.numero_expediente = numero_expediente
        self.genero = genero

class cita:
    def __init__(self, paciente, medico, fecha, hora, diagnostico, resultado):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.diagnostico = diagnostico
        self.resultado = resultado

class medico:
    def __init__(self, nombre, apellido, telefono, especialidad, citas):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.especialidad = especialidad
        self.citas = citas

class medicamento:
    def __init__(self, nombre, dosis, precio, stock):
        self.nombre = nombre
        self.dosis = dosis
        self.precio = precio
        self. stock = stock


