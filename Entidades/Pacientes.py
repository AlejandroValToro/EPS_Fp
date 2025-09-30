class Pacientes:
    id_paciente: int = 0
    documento: str = None
    tipo_documento: str = None
    nombres: str = None
    apellidos: str = None
    fecha_nacimiento: str = None
    genero: str = None
    direccion: str = None
    telefono: str = None
    email: str = None
    fecha_registro: str = None

    def GetId_paciente(self) -> int:
        return self.id_paciente

    def SetId_paciente(self, value: int) -> None:
        self.id_paciente = value

    def GetDocumento(self) -> str:
        return self.documento

    def SetDocumento(self, value: str) -> None:
        self.documento = value

    def GetTipo_documento(self) -> str:
        return self.tipo_documento

    def SetTipo_documento(self, value: str) -> None:
        self.tipo_documento = value

    def GetNombres(self) -> str:
        return self.nombres

    def SetNombres(self, value: str) -> None:
        self.nombres = value

    def GetApellidos(self) -> str:
        return self.apellidos

    def SetApellidos(self, value: str) -> None:
        self.apellidos = value

    def GetFecha_nacimiento(self) -> str:
        return self.fecha_nacimiento

    def SetFecha_nacimiento(self, value: str) -> None:
        self.fecha_nacimiento = value

    def GetGenero(self) -> str:
        return self.genero

    def SetGenero(self, value: str) -> None:
        self.genero = value

    def GetDireccion(self) -> str:
        return self.direccion

    def SetDireccion(self, value: str) -> None:
        self.direccion = value

    def GetTelefono(self) -> str:
        return self.telefono

    def SetTelefono(self, value: str) -> None:
        self.telefono = value

    def GetEmail(self) -> str:
        return self.email

    def SetEmail(self, value: str) -> None:
        self.email = value

    def GetFecha_registro(self) -> str:
        return self.fecha_registro

    def SetFecha_registro(self, value: str) -> None:
        self.fecha_registro = value
