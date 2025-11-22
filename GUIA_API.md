# Guía para Probar la API Flask

## 1. Iniciar el Servidor

```bash
python run.py
```

El servidor estará disponible en: `http://localhost:5000`

---

## 2. Probar los Endpoints

### 2.1. Verificar que el servidor está corriendo

**Request:**
```bash
curl http://localhost:5000/
```

**Respuesta esperada:**
```
EPS API is running!
```

---

### 2.2. LOGIN - Obtener Token JWT

**Request:**
```bash
curl -X POST http://localhost:5000/auth/login ^
  -H "Content-Type: application/json" ^
  -d "{\"user_id\": \"admin\"}"
```

**Respuesta esperada:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**IMPORTANTE:** Copia el token para usarlo en las siguientes peticiones.

---

### 2.3. CREATE - Crear Paciente

**Request:**
```bash
curl -X POST http://localhost:5000/pacientes/ ^
  -H "Authorization: Bearer TU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": \"1234567890\", \"tipo_documento\": \"CC\", \"nombres\": \"Juan Carlos\", \"apellidos\": \"Perez Garcia\", \"fecha_nacimiento\": \"1990-05-15\", \"genero\": \"M\", \"direccion\": \"Calle 123 #45-67\", \"telefono\": \"3001234567\", \"email\": \"juan.perez@email.com\"}"
```

**Respuesta esperada:**
```json
{
  "message": "Paciente creado exitosamente",
  "Respuesta": "OK"
}
```

---

### 2.4. READ ALL - Listar Todos los Pacientes

**Request:**
```bash
curl http://localhost:5000/pacientes/ ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

**Respuesta esperada:**
```json
{
  "Entidades": {
    "0": {
      "id_paciente": 1,
      "documento": "1234567890",
      "nombres": "Juan Carlos",
      ...
    }
  },
  "Respuesta": "OK"
}
```

**Nota:** Los datos sensibles estarán desencriptados en la respuesta.

---

### 2.5. READ BY ID - Leer Paciente Específico

**Request:**
```bash
curl http://localhost:5000/pacientes/1 ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

Reemplaza `1` con el ID del paciente que quieres consultar.

**Respuesta esperada:**
```json
{
  "Entidad": {
    "id_paciente": 1,
    "documento": "1234567890",
    "nombres": "Juan Carlos",
    ...
  },
  "Respuesta": "OK"
}
```

---

### 2.6. UPDATE - Actualizar Paciente

**Request:**
```bash
curl -X PUT http://localhost:5000/pacientes/1 ^
  -H "Authorization: Bearer TU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": \"9876543210\", \"tipo_documento\": \"CC\", \"nombres\": \"Juan Carlos ACTUALIZADO\", \"apellidos\": \"Perez Garcia\", \"fecha_nacimiento\": \"1990-05-15\", \"genero\": \"M\", \"direccion\": \"Avenida 100 #50-25\", \"telefono\": \"3009999999\", \"email\": \"juan.updated@email.com\"}"
```

**Respuesta esperada:**
```json
{
  "message": "Paciente actualizado exitosamente",
  "Respuesta": "OK"
}
```

---

### 2.7. DELETE - Eliminar Paciente

**Request:**
```bash
curl -X DELETE http://localhost:5000/pacientes/1 ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

**Respuesta esperada:**
```json
{
  "message": "Paciente eliminado exitosamente",
  "Respuesta": "OK"
}
```

---

## 3. Usando Postman o Insomnia (Recomendado)

Si tienes Postman o Insomnia instalado, es más fácil probar:

### Configuración:

1. **Base URL:** `http://localhost:5000`

2. **Headers comunes:**
   - `Content-Type: application/json`
   - `Authorization: Bearer {token}`

3. **Colección de requests:**

| Método | Endpoint | Body | Descripción |
|--------|----------|------|-------------|
| POST | `/auth/login` | `{"user_id": "admin"}` | Obtener token |
| GET | `/pacientes/` | - | Listar todos |
| GET | `/pacientes/1` | - | Leer por ID |
| POST | `/pacientes/` | JSON del paciente | Crear |
| PUT | `/pacientes/1` | JSON del paciente | Actualizar |
| DELETE | `/pacientes/1` | - | Eliminar |

---

## 4. Verificar Ofuscación en la Base de Datos

Mientras la API está corriendo, puedes verificar en MySQL que los datos están encriptados:

```sql
SELECT id_paciente, documento, nombres, email 
FROM Pacientes 
LIMIT 1;
```

**Resultado esperado:**
- Los campos `documento`, `nombres`, `email` deben mostrar JWTs (cadenas largas que empiezan con `eyJ`)
- La API los desencripta automáticamente al leerlos

---

## 5. Endpoints Disponibles

| Método | Ruta | Requiere Token | Descripción |
|--------|------|----------------|-------------|
| GET | `/` | No | Verificar servidor |
| POST | `/auth/login` | No | Obtener token JWT |
| GET | `/pacientes/` | Sí | Listar todos los pacientes |
| GET | `/pacientes/<id>` | Sí | Obtener paciente por ID |
| POST | `/pacientes/` | Sí | Crear nuevo paciente |
| PUT | `/pacientes/<id>` | Sí | Actualizar paciente |
| DELETE | `/pacientes/<id>` | Sí | Eliminar paciente |

---

## 6. Ejemplo Completo de Flujo

```bash
# 1. Obtener token
curl -X POST http://localhost:5000/auth/login -H "Content-Type: application/json" -d "{\"user_id\": \"admin\"}"

# Respuesta: {"token": "eyJhbGci..."}
# Copia el token

# 2. Crear paciente
curl -X POST http://localhost:5000/pacientes/ -H "Authorization: Bearer eyJhbGci..." -H "Content-Type: application/json" -d "{\"documento\": \"1234567890\", \"tipo_documento\": \"CC\", \"nombres\": \"Test\", \"apellidos\": \"User\", \"fecha_nacimiento\": \"1990-01-01\", \"genero\": \"M\", \"direccion\": \"Test\", \"telefono\": \"123\", \"email\": \"test@test.com\"}"

# 3. Listar pacientes
curl http://localhost:5000/pacientes/ -H "Authorization: Bearer eyJhbGci..."

# 4. Leer paciente por ID
curl http://localhost:5000/pacientes/1 -H "Authorization: Bearer eyJhbGci..."

# 5. Actualizar paciente
curl -X PUT http://localhost:5000/pacientes/1 -H "Authorization: Bearer eyJhbGci..." -H "Content-Type: application/json" -d "{\"documento\": \"999\", \"tipo_documento\": \"CC\", \"nombres\": \"Updated\", \"apellidos\": \"User\", \"fecha_nacimiento\": \"1990-01-01\", \"genero\": \"M\", \"direccion\": \"New\", \"telefono\": \"999\", \"email\": \"new@test.com\"}"

# 6. Eliminar paciente
curl -X DELETE http://localhost:5000/pacientes/1 -H "Authorization: Bearer eyJhbGci..."
```

---

## 7. Notas Importantes

- ✅ Todos los endpoints (excepto `/` y `/auth/login`) requieren autenticación con JWT
- ✅ Los datos sensibles se encriptan automáticamente al guardar
- ✅ Los datos se desencriptan automáticamente al leer
- ✅ El token JWT expira en 24 horas
- ✅ Los campos con ofuscación: documento, nombres, apellidos, direccion, telefono, email
