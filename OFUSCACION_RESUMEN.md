# Resumen de Ofuscación de Datos - Sistema EPS

## Descripción General

Este documento describe qué campos están ofuscados (usando JWT) en cada una de las 15 tablas del sistema EPS.

## Método de Ofuscación

Se utiliza **JWT (JSON Web Tokens)** con el algoritmo HS256 para ofuscar datos sensibles. La clave secreta se encuentra en `app/config.py` como `SECRET_KEY`.

### Funciones de Ofuscación

- **Encriptación**: `Security.encrypt_value(value)` - Convierte el valor en un JWT
- **Desencriptación**: `Security.decrypt_value(encrypted_value)` - Extrae el valor original del JWT

## Tablas y Campos Ofuscados

### 1. **Pacientes** ✅ CON OFUSCACIÓN
**Campos ofuscados:**
- `documento` - Número de documento de identidad
- `nombres` - Nombres del paciente
- `apellidos` - Apellidos del paciente
- `direccion` - Dirección de residencia
- `telefono` - Número de teléfono
- `email` - Correo electrónico

**Justificación:** Datos personales sensibles protegidos por leyes de privacidad (GDPR, HIPAA, etc.)

---

### 2. **Especialidades** ❌ SIN OFUSCACIÓN
**Campos:** `nombre`, `descripcion`

**Justificación:** Información pública que no contiene datos personales

---

### 3. **Medicos** ✅ CON OFUSCACIÓN
**Campos ofuscados:**
- `documento` - Número de documento de identidad
- `nombres` - Nombres del médico
- `apellidos` - Apellidos del médico
- `telefono` - Número de teléfono
- `email` - Correo electrónico
- `tarjeta_profesional` - Número de tarjeta profesional

**Justificación:** Datos personales del médico que deben ser protegidos

---

### 4. **Citas** ❌ SIN OFUSCACIÓN
**Campos:** `id_paciente`, `id_medico`, `fecha_hora`, `estado`, `motivo`

**Justificación:** Información de citas que solo contiene referencias (IDs) y fechas

---

### 5. **HistoriasClinicas** ❌ SIN OFUSCACIÓN
**Campos:** `id_paciente`, `fecha_creacion`, `antecedentes`

**Justificación:** Los antecedentes médicos podrían ofuscarse en producción, pero para este proyecto académico se mantienen sin ofuscar

---

### 6. **Consultas** ❌ SIN OFUSCACIÓN
**Campos:** `id_cita`, `id_historia`, `diagnostico`, `tratamiento`, `observaciones`, `fecha_consulta`

**Justificación:** Similar a historias clínicas, información médica que en producción podría requerir ofuscación adicional

---

### 7. **Medicamentos** ❌ SIN OFUSCACIÓN
**Campos:** `nombre`, `descripcion`, `fabricante`, `stock`

**Justificación:** Información de catálogo público

---

### 8. **Recetas** ❌ SIN OFUSCACIÓN
**Campos:** `id_consulta`, `id_medicamento`, `dosis`, `frecuencia`, `duracion`, `fecha_receta`

**Justificación:** Información de prescripción médica vinculada a consultas

---

### 9. **Departamentos** ❌ SIN OFUSCACIÓN
**Campos:** `nombre`, `descripcion`

**Justificación:** Información organizacional pública

---

### 10. **Empleados** ✅ CON OFUSCACIÓN
**Campos ofuscados:**
- `documento` - Número de documento de identidad
- `nombres` - Nombres del empleado
- `apellidos` - Apellidos del empleado

**Justificación:** Datos personales de empleados que deben ser protegidos

---

### 11. **Laboratorios** ✅ CON OFUSCACIÓN (PARCIAL)
**Campos ofuscados:**
- `telefono` - Número de teléfono del laboratorio

**Campos sin ofuscar:**
- `nombre` - Nombre del laboratorio
- `direccion` - Dirección del laboratorio

**Justificación:** El teléfono se considera dato de contacto sensible, mientras que nombre y dirección son información pública

---

### 12. **ExamenesLaboratorio** ❌ SIN OFUSCACIÓN
**Campos:** `id_consulta`, `id_laboratorio`, `tipo_examen`, `fecha_solicitud`, `fecha_resultado`, `resultado`

**Justificación:** Información de exámenes vinculada a consultas

---

### 13. **Facturas** ❌ SIN OFUSCACIÓN
**Campos:** `id_paciente`, `fecha_emision`, `monto_total`, `estado`

**Justificación:** Información financiera vinculada a pacientes por ID

---

### 14. **DetallesFactura** ❌ SIN OFUSCACIÓN
**Campos:** `id_factura`, `concepto`, `cantidad`, `precio_unitario`, `subtotal`

**Justificación:** Detalles de facturación

---

### 15. **Horarios** ❌ SIN OFUSCACIÓN
**Campos:** `id_medico`, `dia_semana`, `hora_inicio`, `hora_fin`

**Justificación:** Información de horarios de atención

---

## Resumen Estadístico

- **Total de tablas:** 15
- **Tablas con ofuscación:** 4 (Pacientes, Medicos, Empleados, Laboratorios)
- **Tablas sin ofuscación:** 11
- **Total de campos ofuscados:** 16 campos

## Implementación Técnica

### Repositorios con Ofuscación

Los siguientes repositorios implementan ofuscación:

1. `app/repositories/pacientes_v2.py` - PacientesRepositorioModified
2. `app/repositories/medicos.py` - MedicosRepositorio
3. `app/repositories/empleados.py` - EmpleadosRepositorio
4. `app/repositories/laboratorios.py` - LaboratoriosRepositorio

### Flujo de Datos

**Al CREAR/ACTUALIZAR:**
1. El usuario envía datos en texto plano
2. El repositorio encripta los campos sensibles usando JWT
3. Los datos encriptados se guardan en la base de datos

**Al LEER:**
1. Los datos encriptados se leen de la base de datos
2. El repositorio base (`RepositorioBase`) desencripta automáticamente los campos marcados como `encrypted_fields`
3. Los datos se devuelven al usuario en texto plano

### Configuración

La lista de campos encriptados se define en el constructor de cada repositorio:

```python
class PacientesRepositorioModified(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Pacientes, 
                        encrypted_fields=['documento', 'nombres', 'apellidos', 
                                        'direccion', 'telefono', 'email'])
```

## Validación

Para validar que la ofuscación funciona correctamente, ejecutar:

```bash
python tests/comprehensive_validation.py
```

Este script:
- Prueba CRUD para todas las 15 tablas
- Verifica que los datos se encripten en la BD
- Verifica que los datos se desencripten correctamente al leer
- Genera un reporte detallado de éxito/fallo

## Notas para Producción

⚠️ **IMPORTANTE:** Este es un proyecto académico. Para producción se recomienda:

1. Usar variables de entorno para `SECRET_KEY` y `ENCRYPTION_KEY`
2. Considerar ofuscar campos adicionales como diagnósticos y tratamientos
3. Implementar rotación de claves
4. Usar algoritmos de encriptación más robustos (AES-256)
5. Implementar auditoría de acceso a datos sensibles
6. Cumplir con regulaciones locales de protección de datos (GDPR, HIPAA, etc.)
