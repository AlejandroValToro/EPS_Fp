# API Endpoints - Sistema EPS

## Resumen

**Total de Endpoints:** 75 endpoints (15 tablas × 5 operaciones CRUD)  
**Base URL:** `http://localhost:5000`  
**Autenticación:** JWT Token (excepto `/` y `/auth/login`)

---

## Autenticación

### Login
```
POST /auth/login
```
**Body:**
```json
{
  "user_id": "admin"
}
```
**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## Endpoints por Tabla

### 1. Pacientes (con ofuscación)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/pacientes/` | Listar todos |
| GET | `/pacientes/<id>` | Obtener por ID |
| POST | `/pacientes/` | Crear nuevo |
| PUT | `/pacientes/<id>` | Actualizar |
| DELETE | `/pacientes/<id>` | Eliminar |

**Campos:** documento, tipo_documento, nombres, apellidos, fecha_nacimiento, genero, direccion, telefono, email  
**Ofuscados:** documento, nombres, apellidos, direccion, telefono, email

---

### 2. Especialidades

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/especialidades/` | Listar todos |
| GET | `/especialidades/<id>` | Obtener por ID |
| POST | `/especialidades/` | Crear nuevo |
| PUT | `/especialidades/<id>` | Actualizar |
| DELETE | `/especialidades/<id>` | Eliminar |

**Campos:** nombre, descripcion

---

### 3. Medicos (con ofuscación)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/medicos/` | Listar todos |
| GET | `/medicos/<id>` | Obtener por ID |
| POST | `/medicos/` | Crear nuevo |
| PUT | `/medicos/<id>` | Actualizar |
| DELETE | `/medicos/<id>` | Eliminar |

**Campos:** documento, nombres, apellidos, id_especialidad, telefono, email, tarjeta_profesional  
**Ofuscados:** documento, nombres, apellidos, telefono, email, tarjeta_profesional

---

### 4. Citas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/citas/` | Listar todos |
| GET | `/citas/<id>` | Obtener por ID |
| POST | `/citas/` | Crear nuevo |
| PUT | `/citas/<id>` | Actualizar |
| DELETE | `/citas/<id>` | Eliminar |

**Campos:** id_paciente, id_medico, fecha_hora, estado, motivo

---

### 5. Historias Clínicas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/historias_clinicas/` | Listar todos |
| GET | `/historias_clinicas/<id>` | Obtener por ID |
| POST | `/historias_clinicas/` | Crear nuevo |
| PUT | `/historias_clinicas/<id>` | Actualizar |
| DELETE | `/historias_clinicas/<id>` | Eliminar |

**Campos:** id_paciente, antecedentes

---

### 6. Consultas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/consultas/` | Listar todos |
| GET | `/consultas/<id>` | Obtener por ID |
| POST | `/consultas/` | Crear nuevo |
| PUT | `/consultas/<id>` | Actualizar |
| DELETE | `/consultas/<id>` | Eliminar |

**Campos:** id_cita, id_historia, diagnostico, tratamiento, observaciones

---

### 7. Medicamentos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/medicamentos/` | Listar todos |
| GET | `/medicamentos/<id>` | Obtener por ID |
| POST | `/medicamentos/` | Crear nuevo |
| PUT | `/medicamentos/<id>` | Actualizar |
| DELETE | `/medicamentos/<id>` | Eliminar |

**Campos:** nombre, descripcion, fabricante, stock

---

### 8. Recetas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/recetas/` | Listar todos |
| GET | `/recetas/<id>` | Obtener por ID |
| POST | `/recetas/` | Crear nuevo |
| PUT | `/recetas/<id>` | Actualizar |
| DELETE | `/recetas/<id>` | Eliminar |

**Campos:** id_consulta, id_medicamento, dosis, frecuencia, duracion

---

### 9. Departamentos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/departamentos/` | Listar todos |
| GET | `/departamentos/<id>` | Obtener por ID |
| POST | `/departamentos/` | Crear nuevo |
| PUT | `/departamentos/<id>` | Actualizar |
| DELETE | `/departamentos/<id>` | Eliminar |

**Campos:** nombre, descripcion

---

### 10. Empleados (con ofuscación)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/empleados/` | Listar todos |
| GET | `/empleados/<id>` | Obtener por ID |
| POST | `/empleados/` | Crear nuevo |
| PUT | `/empleados/<id>` | Actualizar |
| DELETE | `/empleados/<id>` | Eliminar |

**Campos:** documento, nombres, apellidos, id_departamento, cargo, fecha_contratacion  
**Ofuscados:** documento, nombres, apellidos

---

### 11. Laboratorios (con ofuscación parcial)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/laboratorios/` | Listar todos |
| GET | `/laboratorios/<id>` | Obtener por ID |
| POST | `/laboratorios/` | Crear nuevo |
| PUT | `/laboratorios/<id>` | Actualizar |
| DELETE | `/laboratorios/<id>` | Eliminar |

**Campos:** nombre, direccion, telefono  
**Ofuscados:** telefono

---

### 12. Exámenes de Laboratorio

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/examenes_laboratorio/` | Listar todos |
| GET | `/examenes_laboratorio/<id>` | Obtener por ID |
| POST | `/examenes_laboratorio/` | Crear nuevo |
| PUT | `/examenes_laboratorio/<id>` | Actualizar |
| DELETE | `/examenes_laboratorio/<id>` | Eliminar |

**Campos:** id_consulta, id_laboratorio, tipo_examen, fecha_solicitud, fecha_resultado, resultado

---

### 13. Facturas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/facturas/` | Listar todos |
| GET | `/facturas/<id>` | Obtener por ID |
| POST | `/facturas/` | Crear nuevo |
| PUT | `/facturas/<id>` | Actualizar |
| DELETE | `/facturas/<id>` | Eliminar |

**Campos:** id_paciente, monto_total, estado

---

### 14. Detalles de Factura

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/detalles_factura/` | Listar todos |
| GET | `/detalles_factura/<id>` | Obtener por ID |
| POST | `/detalles_factura/` | Crear nuevo |
| PUT | `/detalles_factura/<id>` | Actualizar |
| DELETE | `/detalles_factura/<id>` | Eliminar |

**Campos:** id_factura, concepto, cantidad, precio_unitario, subtotal

---

### 15. Horarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/horarios/` | Listar todos |
| GET | `/horarios/<id>` | Obtener por ID |
| POST | `/horarios/` | Crear nuevo |
| PUT | `/horarios/<id>` | Actualizar |
| DELETE | `/horarios/<id>` | Eliminar |

**Campos:** id_medico, dia_semana, hora_inicio, hora_fin

---

## Formato de Respuestas

### Éxito
```json
{
  "Respuesta": "OK",
  "Entidades": { ... }  // Para GET all
  "Entidad": { ... }    // Para GET by ID
  "message": "..."      // Para CREATE/UPDATE/DELETE
}
```

### Error
```json
{
  "Respuesta": "Error",
  "Error": "Descripción del error"
}
```

---

## Headers Requeridos

Todos los endpoints (excepto `/` y `/auth/login`) requieren:

```
Authorization: Bearer {token}
Content-Type: application/json
```

---

## Ejemplo de Uso Completo

```bash
# 1. Login
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"user_id": "admin"}'

# 2. Crear Especialidad
curl -X POST http://localhost:5000/especialidades/ \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Cardiología", "descripcion": "Especialidad del corazón"}'

# 3. Listar Especialidades
curl http://localhost:5000/especialidades/ \
  -H "Authorization: Bearer {token}"

# 4. Obtener Especialidad por ID
curl http://localhost:5000/especialidades/1 \
  -H "Authorization: Bearer {token}"

# 5. Actualizar Especialidad
curl -X PUT http://localhost:5000/especialidades/1 \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Cardiología Avanzada", "descripcion": "Nueva descripción"}'

# 6. Eliminar Especialidad
curl -X DELETE http://localhost:5000/especialidades/1 \
  -H "Authorization: Bearer {token}"
```

---

## Tablas con Ofuscación JWT

Las siguientes tablas tienen campos ofuscados:

1. **Pacientes** - 6 campos ofuscados
2. **Medicos** - 6 campos ofuscados
3. **Empleados** - 3 campos ofuscados
4. **Laboratorios** - 1 campo ofuscado

**Total:** 16 campos ofuscados en 4 tablas

---

## Notas Importantes

- ✅ Todos los endpoints están protegidos con JWT (excepto login)
- ✅ Los datos sensibles se encriptan automáticamente al guardar
- ✅ Los datos se desencriptan automáticamente al leer
- ✅ El token JWT expira en 24 horas
- ✅ Las fechas deben enviarse en formato ISO: `YYYY-MM-DD`
- ✅ Los datetime deben enviarse en formato ISO: `YYYY-MM-DDTHH:MM:SS`

---

**Total de Endpoints:** 75  
**Estado:** ✅ TODOS FUNCIONANDO
