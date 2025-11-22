# Sistema EPS - Guía de Uso

## 📋 Descripción

Sistema de gestión para una EPS (Entidad Promotora de Salud) con API REST implementada en Flask. Incluye CRUD completo para 15 entidades y ofuscación de datos sensibles usando JWT.

---

## 🚀 Inicio Rápido

### 1. Requisitos Previos

- Python 3.8+
- MySQL 5.7+ o MariaDB
- Bruno (cliente API) o Postman

### 2. Instalación

```bash
# Instalar dependencias
pip install flask sqlalchemy pymysql cryptography pyjwt colorama

# Configurar base de datos
mysql -u user_ptyhon -p EPS < script.sql
```

### 3. Configuración

Editar `app/config.py` con tus credenciales de MySQL:

```python
DB_USER = "user_ptyhon"
DB_PASSWORD = "Clas3s1Nt2024_!"
DB_HOST = "localhost"
DB_PORT = "3307"
DB_NAME = "EPS"
```

### 4. Ejecutar el Servidor

```bash
python run.py
```

El servidor estará disponible en: `http://localhost:5000`

---

## 🧪 Probar con Bruno

### Paso 1: Abrir Bruno

1. Abre Bruno
2. Click en "Open Collection"
3. Selecciona la carpeta `bruno_collection`

### Paso 2: Flujo de Prueba CRUD

La colección incluye 6 requests en orden:

1. **Login** - Obtener token JWT
2. **Crear Paciente** - Insertar nuevo paciente
3. **Listar Pacientes** - Ver todos los pacientes
4. **Buscar por ID** - Obtener paciente específico
5. **Actualizar Paciente** - Modificar datos del paciente
6. **Eliminar Paciente** - Borrar el paciente

### Paso 3: Ejecutar las Pruebas

1. Ejecuta "1. Login" - El token se guardará automáticamente
2. Ejecuta "2. Crear Paciente" - Crea un nuevo paciente
3. Ejecuta "3. Listar Pacientes" - Verifica que se creó
4. **IMPORTANTE:** Copia el `id_paciente` del último paciente
5. Actualiza el ID en los requests 4, 5 y 6 (reemplaza `36` con el ID real)
6. Ejecuta "4. Buscar por ID" - Verifica los datos
7. Ejecuta "5. Actualizar Paciente" - Modifica los datos
8. Ejecuta "6. Eliminar Paciente" - Elimina el registro

---

## 📚 Documentación

- **`API_ENDPOINTS.md`** - Lista completa de los 75 endpoints disponibles
- **`OFUSCACION_RESUMEN.md`** - Detalles sobre qué campos están ofuscados
- **`VALIDACION_FINAL.md`** - Reporte de validación del sistema
- **`GUIA_API.md`** - Ejemplos de uso con curl

---

## 🗂️ Estructura del Proyecto

```
EPS_Fp/
├── app/
│   ├── models/
│   │   └── models.py              # 15 modelos de datos
│   ├── repositories/              # 15 repositorios (acceso a datos)
│   │   ├── base.py                # Repositorio base con desencriptación
│   │   ├── pacientes_v2.py        # Con ofuscación
│   │   ├── medicos.py             # Con ofuscación
│   │   ├── empleados.py           # Con ofuscación
│   │   ├── laboratorios.py        # Con ofuscación
│   │   └── [11 repositorios más]
│   ├── routes/                    # 15 archivos de rutas (endpoints)
│   │   ├── auth.py                # Autenticación
│   │   ├── pacientes_v2.py        # CRUD Pacientes
│   │   └── [14 rutas más]
│   ├── utils/
│   │   ├── security.py            # Funciones de encriptación JWT
│   │   └── decorators.py          # Decoradores de autenticación
│   ├── config.py                  # Configuración
│   └── __init__.py                # Inicialización de Flask
├── bruno_collection/              # Colección de Bruno para pruebas
│   ├── 1. Login.bru
│   ├── 2. Crear Paciente.bru
│   ├── 3. Listar Pacientes.bru
│   ├── 4. Buscar Paciente por ID.bru
│   ├── 5. Actualizar Paciente.bru
│   └── 6. Eliminar Paciente.bru
├── script.sql                     # Script de creación de BD
├── run.py                         # Punto de entrada
└── README.md                      # Este archivo
```

---

## 🔐 Seguridad y Ofuscación

### Tablas con Ofuscación JWT

1. **Pacientes** (6 campos): documento, nombres, apellidos, direccion, telefono, email
2. **Medicos** (6 campos): documento, nombres, apellidos, telefono, email, tarjeta_profesional
3. **Empleados** (3 campos): documento, nombres, apellidos
4. **Laboratorios** (1 campo): telefono

**Total:** 16 campos ofuscados en 4 tablas

### Funcionamiento

- **Al guardar:** Los datos sensibles se encriptan automáticamente con JWT
- **Al leer:** Los datos se desencriptan automáticamente
- **En la BD:** Los datos se almacenan como JWTs (ej: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`)

---

## 📊 Endpoints Disponibles

### Resumen

- **Total de endpoints:** 75 (15 tablas × 5 operaciones)
- **Autenticación:** JWT Token (excepto `/` y `/auth/login`)
- **Base URL:** `http://localhost:5000`

### Operaciones CRUD por Tabla

Cada tabla tiene 5 endpoints:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/{tabla}/` | Listar todos |
| GET | `/{tabla}/<id>` | Obtener por ID |
| POST | `/{tabla}/` | Crear nuevo |
| PUT | `/{tabla}/<id>` | Actualizar |
| DELETE | `/{tabla}/<id>` | Eliminar |

### Tablas Disponibles

1. `/pacientes/` - Pacientes
2. `/especialidades/` - Especialidades
3. `/medicos/` - Médicos
4. `/citas/` - Citas
5. `/historias_clinicas/` - Historias Clínicas
6. `/consultas/` - Consultas
7. `/medicamentos/` - Medicamentos
8. `/recetas/` - Recetas
9. `/departamentos/` - Departamentos
10. `/empleados/` - Empleados
11. `/laboratorios/` - Laboratorios
12. `/examenes_laboratorio/` - Exámenes de Laboratorio
13. `/facturas/` - Facturas
14. `/detalles_factura/` - Detalles de Factura
15. `/horarios/` - Horarios

Ver `API_ENDPOINTS.md` para detalles completos.

---

## 🎯 Características

- ✅ CRUD completo para 15 entidades
- ✅ Autenticación JWT
- ✅ Ofuscación de datos sensibles (16 campos)
- ✅ Stored Procedures de MySQL
- ✅ Arquitectura en capas (Models, Repositories, Routes)
- ✅ Validación de datos
- ✅ Manejo de errores
- ✅ Documentación completa

---

## 🛠️ Tecnologías

- **Backend:** Flask (Python)
- **ORM:** SQLAlchemy
- **Base de Datos:** MySQL
- **Seguridad:** JWT (PyJWT)
- **Ofuscación:** JWT HS256

---

## 📝 Ejemplo de Uso

### Con curl

```bash
# 1. Login
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"user_id": "admin"}'

# 2. Crear paciente
curl -X POST http://localhost:5000/pacientes/ \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "documento": "1234567890",
    "tipo_documento": "CC",
    "nombres": "Juan",
    "apellidos": "Perez",
    "fecha_nacimiento": "1990-01-01",
    "genero": "M",
    "direccion": "Calle 123",
    "telefono": "3001234567",
    "email": "juan@email.com"
  }'

# 3. Listar pacientes
curl http://localhost:5000/pacientes/ \
  -H "Authorization: Bearer {token}"
```

### Con Bruno

1. Importa la colección desde `bruno_collection/`
2. Ejecuta los requests en orden
3. El token se guarda automáticamente

---

## ⚠️ Notas

- Este es un proyecto académico
- Las claves están hardcodeadas (en producción usar variables de entorno)
- El token JWT expira en 24 horas
- Las fechas deben enviarse en formato ISO: `YYYY-MM-DD`

---

## 📞 Soporte

Para más información, consulta:
- `API_ENDPOINTS.md` - Documentación completa de endpoints
- `GUIA_API.md` - Ejemplos con curl
- `OFUSCACION_RESUMEN.md` - Detalles de ofuscación

---

**Estado:** ✅ Sistema completo y funcional  
**Versión:** 1.0  
**Fecha:** 2025-11-22
