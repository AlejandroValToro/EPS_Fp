# Importar los componentes necesarios
from Repositorios.Conexion import SessionLocal, PacientesRepositorio, Pacientes, inicializar_db
from datetime import datetime

def main():

    # Verifica la conexión
    inicializar_db()

    db_session = SessionLocal()

    try:
        repo_pacientes = PacientesRepositorio(db_session)

        # --- Prueba de Creación ---
        print("\n[Prueba de Creación] Creando un nuevo paciente via SP...")
        nuevo_paciente = Pacientes(
            documento="123456978",
            tipo_documento="CE",
            nombres="Alejo",
            apellidos="Valencia",
            fecha_nacimiento=datetime(1995, 8, 22).date(),
            genero="F",
            direccion="Calle Falsa Viva 742",
            telefono="3219876543",
            email="oelo.lopez@example.com"
        )
        if repo_pacientes.crear(nuevo_paciente):
            print("Paciente creado exitosamente.")
        else:
            print("Falló la creación del paciente.")

        # --- Prueba de Lectura ---
        print("\n[Prueba de Lectura] Consultando todos los pacientes via SP...")
        lista_pacientes = repo_pacientes.leer_todos()

        if not lista_pacientes:
            print("No se encontraron pacientes.")
        else:
            print(f"Se encontraron {len(lista_pacientes)} pacientes:")
            for paciente in lista_pacientes:
                print(f"  - ID: {paciente.id_paciente}, Nombre: {paciente.nombres} {paciente.apellidos}")

        # --- Prueba de Lectura por ID ---
        print("\n[Prueba de Lectura por ID] Buscando paciente con ID 1...")
        paciente_uno = repo_pacientes.leer_por_id(1)
        if paciente_uno:
            print(f"Encontrado: {paciente_uno.nombres} {paciente_uno.apellidos}")
        else:
            print("No se encontró paciente con ID 1.")

    except Exception as e:
        print(f"\nOcurrió un error durante la prueba: {e}")
    finally:
        print("\n--- Prueba finalizada. Cerrando sesión. ---")
        db_session.close()

if __name__ == "__main__":
    main()