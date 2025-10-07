from Repositorios.Conexion import SessionLocal, PacientesRepositorio, Pacientes, inicializar_db
from datetime import datetime

def main():

    inicializar_db()

    db_session = SessionLocal()

    try:
        repo_pacientes = PacientesRepositorio(db_session)

        print("Creando un nuevo paciente")
        nuevo_paciente = Pacientes(
            documento="123456978",
            tipo_documento="CE",
            nombres="andres",
            apellidos="parcerito",
            fecha_nacimiento=datetime(1992, 8, 14).date(),
            genero="F",
            direccion="holaholahola",
            telefono="321457568",
            email="hombe.lopez@example.com"
        )
        if repo_pacientes.crear(nuevo_paciente):
            print("Paciente creado exitosamente.")
        else:
            print("Falló la creación del paciente.")

        print("Consultando todos los pacientes")
        lista_pacientes = repo_pacientes.leer_todos()

        if not lista_pacientes:
            print("No se encontraron pacientes.")
        else:
            print(f"Se encontraron {len(lista_pacientes)} pacientes:")
            for paciente in lista_pacientes:
                print(f"  - ID: {paciente.id_paciente}, Nombre: {paciente.nombres} {paciente.apellidos}")

        print("Buscando paciente con ID 1.")
        paciente_uno = repo_pacientes.leer_por_id(1)
        if paciente_uno:
            print(f"Encontrado: {paciente_uno.nombres} {paciente_uno.apellidos}")
        else:
            print("No se encontró paciente con ID 1.")

        # --- Prueba de Eliminación ---
        # (Cuidado: esto borrará un registro)
        # print("Eliminando paciente con ID 2.")
        # if repo_pacientes.eliminar(2):
        #     print("Paciente con ID 2 eliminado exitosamente.")
        # else:
        #     print("Falló la eliminación del paciente con ID 2.")

    except Exception as e:
        print(f"Ocurrió un error durante la prueba: {e}")
    finally:
        print("Prueba finalizada. Cerrando sesión.")
        db_session.close()

if __name__ == "__main__":
    main()