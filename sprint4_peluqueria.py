#Veterinaria Peludos

# Clase Dueño, con nombre, telefono y direccion, todos creados en la función init.
class Dueno:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self): # Funcion que une los datos del dueño en una sola cadena de caracteres.
        return f"Dueño: {self.nombre}, Tel: {self.telefono}, Dirección: {self.direccion}"


# Clase Mascota/ con nombre, especia, raza, edad y dueño de la mascota = objeto mascota
class Mascota:
    def __init__(self, nombre, especie, raza, edad, dueno):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueno = dueno  # Objeto de tipo Dueño
        self.consultas = []  # Lista para almacenar objetos de tipo Consulta

    def agregarconsulta(self, consulta):
        self.consultas.append(consulta)

    def mostrarhistorial(self): # Muestra el historial de consultas de la mascota, identificando por el nombre exacto.
        if not self.consultas:
            return "No hay consultas registradas para esta mascota."
        historial = f"Historial de {self.nombre}:\n"
        for c in self.consultas:
            historial += str(c) + "\n"
        return historial

    def __str__(self): # Funcion que une los datos de la mascota junto con el nombre del dueño.
        return f"{self.nombre} ({self.especie}, {self.raza}, {self.edad} años)\n{self.dueno}"


# Clase Consulta/ con fecha, motivo y diagnostico de la mascota = objeto consulta.
class Consulta:
    def __init__(self, fecha, motivo, diagnostico):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico

    def __str__(self): # Funcion str, que une los datos de la consulta en una sola cadena de caracteres.
        return f"[{self.fecha}] Motivo: {self.motivo} | Diagnóstico: {self.diagnostico}"


# ------------------------------
# Base de datos simulada (listas)
mascotasregistradas = []

# ------------------------------
# Funciones del menú de registrar/ se toman los datos del objeto mascota, nombre, especie, raza, edad. Y del dueño respectivamente.
def registrarmascota():
    print("\n--- Registrar Nueva Mascota ---")
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    print("\n--- Datos del Dueño ---")
    nombre_dueno = input("Nombre del dueño: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    # crear objetos, dueño y mascota, usando las clases de cada una.
    dueno = Dueno(nombre_dueno, telefono, direccion)
    mascota = Mascota(nombre, especie, raza, edad, dueno)
    mascotasregistradas.append(mascota)
    print(f"\n Mascota '{nombre}' registrada exitosamente.")

# -------------------------------
# Funcion registrarconsulta, donde se toma el nombre de la mascota, y valida que la mascota exista, si existe pide los demas datos necesarios.
def registrarconsulta():
    print("\n--- Registrar Consulta ---")
    nombre_mascota = input("Nombre de la mascota: ")
    mascota = buscarmascotapornombre(nombre_mascota)
    if mascota:
        fecha = input("Fecha de la consulta (DD/MM/AAAA): ")
        motivo = input("Motivo de la consulta: ")
        diagnostico = input("Diagnóstico: ")
        consulta = Consulta(fecha, motivo, diagnostico)
        mascota.agregarconsulta(consulta)
        print(f"\nConsulta registrada para {mascota.nombre}.")
    else:
        print("Mascota no encontrada.")

# Funcion listarmascotas, devuelve la lista de mascotas, separadas por 40 "-", si no hay mascotas devuelve un mensaje.
def listarmascotas():
    print("\n--- Lista de Mascotas Registradas ---")
    if not mascotasregistradas:
        print("No hay mascotas registradas.")
    else:
        for mascota in mascotasregistradas:
            print(mascota)
            print("-" * 40)


def verhistorial():
    print("\n--- Historial de Consultas ---")
    nombre_mascota = input("Nombre de la mascota: ")
    mascota = buscarmascotapornombre(nombre_mascota)
    if mascota:
        print(mascota.mostrarhistorial())
    else:
        print("Mascota no encontrada.")


def buscarmascotapornombre(nombre):
    for mascota in mascotasregistradas:
        if mascota.nombre.lower() == nombre.lower():
            return mascota
    return None


def menu():
    while True:
        print("\nClínica Veterinaria 'Amigos Peludos'")
        print("1. Registrar mascota")
        print("2. Registrar consulta")
        print("3. Listar mascotas")
        print("4. Ver historial de consultas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarmascota()
        elif opcion == "2":
            registrarconsulta()
        elif opcion == "3":
            listarmascotas()
        elif opcion == "4":
            verhistorial()
        elif opcion == "5":
            print("¡Gracias por usar el sistema de Amigos Peludos!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# ------------------------------
# Punto de entrada
if __name__ == "__main__":
    menu()
