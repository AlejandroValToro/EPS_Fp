# 🧪 Guía de Pruebas con Bruno

## Paso a Paso para Probar el Sistema EPS

---

## 1️⃣ Abrir Bruno

1. Abre la aplicación **Bruno**
2. Click en **"Open Collection"**
3. Navega a la carpeta del proyecto:
   ```
   c:\Users\Diego\Documents\proyecto_integrador_EPS\EPS_Fp\bruno_collection
   ```
4. Selecciona la carpeta `bruno_collection`

---

## 2️⃣ Verificar que el Servidor Está Corriendo

Antes de empezar, asegúrate de que el servidor Flask esté corriendo:

```bash
python run.py
```

Deberías ver:
```
 * Running on http://127.0.0.1:5000
```

---

## 3️⃣ Flujo de Prueba CRUD Completo

### Request 1: Login

**Objetivo:** Obtener el token JWT de autenticación

1. Click en **"1. Login"**
2. Click en **"Send"**
3. Verifica la respuesta:
   ```json
   {
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
   }
   ```
4. ✅ El token se guarda automáticamente en la variable `{{token}}`

---

### Request 2: Crear Paciente

**Objetivo:** Insertar un nuevo paciente con datos ofuscados

1. Click en **"2. Crear Paciente"**
2. Revisa el body (ya está configurado):
   ```json
   {
     "documento": "1234567890",
     "tipo_documento": "CC",
     "nombres": "Juan Carlos",
     "apellidos": "Perez Garcia",
     "fecha_nacimiento": "1990-05-15",
     "genero": "M",
     "direccion": "Calle 123 #45-67",
     "telefono": "3001234567",
     "email": "juan.perez@email.com"
   }
   ```
3. Click en **"Send"**
4. Verifica la respuesta:
   ```json
   {
     "message": "Paciente creado exitosamente",
     "Respuesta": "OK"
   }
   ```
5. ✅ **Status: 201 Created**

---

### Request 3: Listar Pacientes

**Objetivo:** Ver todos los pacientes y obtener el ID del recién creado

1. Click en **"3. Listar Pacientes"**
2. Click en **"Send"**
3. Verifica la respuesta:
   ```json
   {
     "Entidades": {
       "0": {
         "id_paciente": 36,
         "documento": "1234567890",
         "nombres": "Juan Carlos",
         "apellidos": "Perez Garcia",
         ...
       }
     },
     "Respuesta": "OK"
   }
   ```
4. 📝 **IMPORTANTE:** Copia el `id_paciente` (ej: 36)
5. ✅ **Nota:** Los datos están desencriptados en la respuesta

---

### Request 4: Buscar Paciente por ID

**Objetivo:** Obtener un paciente específico

1. Click en **"4. Buscar Paciente por ID"**
2. **ACTUALIZA EL ID** en la URL:
   - Cambia `/pacientes/36` por `/pacientes/{TU_ID}`
3. Click en **"Send"**
4. Verifica la respuesta:
   ```json
   {
     "Entidad": {
       "id_paciente": 36,
       "documento": "1234567890",
       "nombres": "Juan Carlos",
       ...
     },
     "Respuesta": "OK"
   }
   ```
5. ✅ **Status: 200 OK**

---

### Request 5: Actualizar Paciente

**Objetivo:** Modificar los datos del paciente

1. Click en **"5. Actualizar Paciente"**
2. **ACTUALIZA EL ID** en la URL:
   - Cambia `/pacientes/36` por `/pacientes/{TU_ID}`
3. Revisa el body (ya está configurado con datos actualizados):
   ```json
   {
     "documento": "9876543210",
     "tipo_documento": "CC",
     "nombres": "Juan Carlos ACTUALIZADO",
     "apellidos": "Perez Garcia",
     "fecha_nacimiento": "1990-05-15",
     "genero": "M",
     "direccion": "Avenida 100 #50-25",
     "telefono": "3209999999",
     "email": "juan.updated@email.com"
   }
   ```
4. Click en **"Send"**
5. Verifica la respuesta:
   ```json
   {
     "message": "Paciente actualizado exitosamente",
     "Respuesta": "OK"
   }
   ```
6. ✅ **Status: 200 OK**

---

### Request 6: Eliminar Paciente

**Objetivo:** Borrar el paciente de la base de datos

1. Click en **"6. Eliminar Paciente"**
2. **ACTUALIZA EL ID** en la URL:
   - Cambia `/pacientes/36` por `/pacientes/{TU_ID}`
3. Click en **"Send"**
4. Verifica la respuesta:
   ```json
   {
     "message": "Paciente eliminado exitosamente",
     "Respuesta": "OK"
   }
   ```
5. ✅ **Status: 200 OK**

---

## 4️⃣ Verificar Ofuscación en la Base de Datos

### Mientras el paciente existe (después del paso 2 o 5)

Abre MySQL y ejecuta:

```sql
SELECT id_paciente, documento, nombres, email 
FROM Pacientes 
WHERE id_paciente = 36;  -- Usa tu ID
```

**Resultado esperado:**
```
+-------------+--------------------------------------------------+--------------------------------------------------+
| id_paciente | documento                                        | nombres                                          |
+-------------+--------------------------------------------------+--------------------------------------------------+
| 36          | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRh... | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRh... |
+-------------+--------------------------------------------------+--------------------------------------------------+
```

✅ **Los datos están encriptados como JWTs en la base de datos**

### En la API (respuesta de Bruno)

Los mismos datos se retornan desencriptados:
```json
{
  "documento": "1234567890",
  "nombres": "Juan Carlos",
  "email": "juan.perez@email.com"
}
```

✅ **La API desencripta automáticamente los datos**

---

## 5️⃣ Resumen del Flujo

| Paso | Request | Acción | Resultado |
|------|---------|--------|-----------|
| 1 | Login | Obtener token | Token guardado automáticamente |
| 2 | Crear | Insertar paciente | Datos encriptados en BD |
| 3 | Listar | Ver todos | Datos desencriptados en respuesta |
| 4 | Buscar | Obtener por ID | Datos desencriptados |
| 5 | Actualizar | Modificar datos | Nuevos datos encriptados |
| 6 | Eliminar | Borrar registro | Paciente eliminado |

---

## 6️⃣ Campos Ofuscados

En el paciente, estos campos se encriptan:
- ✅ `documento`
- ✅ `nombres`
- ✅ `apellidos`
- ✅ `direccion`
- ✅ `telefono`
- ✅ `email`

Campos sin encriptar:
- `tipo_documento`
- `fecha_nacimiento`
- `genero`

---

## 7️⃣ Códigos de Respuesta

| Código | Significado | Cuándo aparece |
|--------|-------------|----------------|
| 200 | OK | GET, PUT, DELETE exitosos |
| 201 | Created | POST exitoso |
| 404 | Not Found | ID no existe |
| 500 | Server Error | Error en el servidor |

---

## 8️⃣ Troubleshooting

### Error: "Failed to fetch"
- ✅ Verifica que el servidor esté corriendo (`python run.py`)
- ✅ Verifica que la URL sea `http://localhost:5000`

### Error: "Unauthorized" o 401
- ✅ Ejecuta primero el request "1. Login"
- ✅ Verifica que el token se haya guardado

### Error: "Not Found" o 404
- ✅ Verifica que el ID del paciente sea correcto
- ✅ Ejecuta "3. Listar Pacientes" para obtener IDs válidos

---

## 9️⃣ Probar Otras Tablas

Puedes crear requests similares para otras tablas:

### Ejemplo: Especialidades

```
POST http://localhost:5000/especialidades/
Authorization: Bearer {{token}}

{
  "nombre": "Cardiología",
  "descripcion": "Especialidad del corazón"
}
```

Ver `API_ENDPOINTS.md` para todos los endpoints disponibles.

---

## 🎯 Checklist de Prueba Exitosa

- [ ] ✅ Login ejecutado correctamente
- [ ] ✅ Paciente creado (Status 201)
- [ ] ✅ Paciente listado (aparece en la lista)
- [ ] ✅ Paciente encontrado por ID (Status 200)
- [ ] ✅ Paciente actualizado (Status 200)
- [ ] ✅ Datos verificados en MySQL (encriptados)
- [ ] ✅ Paciente eliminado (Status 200)

---

**¡Listo!** Has probado exitosamente el flujo CRUD completo con ofuscación de datos. 🎉
