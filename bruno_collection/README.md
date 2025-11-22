# Colección Bruno - Sistema EPS

## Cómo Usar

### 1. Abrir la Colección en Bruno

1. Abre Bruno
2. Click en "Open Collection"
3. Selecciona esta carpeta: `bruno_collection`

### 2. Ejecutar los Requests

Los requests están numerados en el orden correcto de ejecución:

#### Request 1: Login
- **URL:** `POST http://localhost:5000/auth/login`
- **Acción:** Obtiene el token JWT
- **Nota:** El token se guarda automáticamente en la variable `{{token}}`

#### Request 2: Crear Paciente
- **URL:** `POST http://localhost:5000/pacientes/`
- **Acción:** Crea un nuevo paciente
- **Nota:** Los datos sensibles se encriptan automáticamente

#### Request 3: Listar Pacientes
- **URL:** `GET http://localhost:5000/pacientes/`
- **Acción:** Lista todos los pacientes
- **Nota:** Copia el `id_paciente` del último paciente creado

#### Request 4: Buscar Paciente por ID
- **URL:** `GET http://localhost:5000/pacientes/36`
- **Acción:** Obtiene un paciente específico
- **IMPORTANTE:** Cambia `36` por el ID que copiaste en el paso 3

#### Request 5: Actualizar Paciente
- **URL:** `PUT http://localhost:5000/pacientes/36`
- **Acción:** Actualiza los datos del paciente
- **IMPORTANTE:** Cambia `36` por el ID correcto

#### Request 6: Eliminar Paciente
- **URL:** `DELETE http://localhost:5000/pacientes/36`
- **Acción:** Elimina el paciente
- **IMPORTANTE:** Cambia `36` por el ID correcto

### 3. Flujo Completo

```
1. Login → Obtiene token
2. Crear Paciente → Inserta registro
3. Listar Pacientes → Copia el ID
4. Actualiza el ID en los requests 4, 5 y 6
5. Buscar por ID → Verifica datos
6. Actualizar → Modifica datos
7. Eliminar → Borra registro
```

### 4. Verificar Ofuscación

Después de crear el paciente, verifica en MySQL:

```sql
SELECT id_paciente, documento, nombres, email 
FROM Pacientes 
WHERE id_paciente = {TU_ID};
```

Los campos deben mostrar JWTs (ej: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`)

## Troubleshooting

### Error: "getaddrinfo ENOTFOUND"
- ✅ Verifica que el servidor Flask esté corriendo: `python run.py`
- ✅ Verifica que la URL sea `http://localhost:5000`

### Error: "Connection refused"
- ✅ El servidor no está corriendo
- ✅ Ejecuta: `python run.py` desde la raíz del proyecto

### Error: "Unauthorized" o 401
- ✅ Ejecuta primero el request "1. Login"
- ✅ Verifica que el token se haya guardado

### Error: "Not Found" o 404
- ✅ Verifica que el ID del paciente sea correcto
- ✅ Ejecuta "3. Listar Pacientes" para obtener IDs válidos

## Campos del Paciente

### Campos Obligatorios
- `documento` (string)
- `tipo_documento` (string: "CC", "CE", "TI", "RC")
- `nombres` (string)
- `apellidos` (string)
- `fecha_nacimiento` (string: formato "YYYY-MM-DD")
- `genero` (string: "M", "F", "O")
- `direccion` (string)
- `telefono` (string)
- `email` (string)

### Campos Ofuscados (encriptados en BD)
- ✅ `documento`
- ✅ `nombres`
- ✅ `apellidos`
- ✅ `direccion`
- ✅ `telefono`
- ✅ `email`

## Notas

- El token JWT expira en 24 horas
- Los datos se encriptan automáticamente al guardar
- Los datos se desencriptan automáticamente al leer
- Todos los requests (excepto Login) requieren el token
