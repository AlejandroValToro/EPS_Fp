class Medicos:
    id_medico: int = 0
    documento: str = None
    nombres: str = None
    apellidos: str = None
    id_especialidad: int = 0
    telefono: str = None
    email: str = None
    tarjeta_profesional: str = None

    def GetId_medico(self) -> int:
        return self.id_medico

    def SetId_medico(self, value: int) -> None:
        self.id_medico = value

    def GetDocumento(self) -> str:
        return self.documento

    def SetDocumento(self, value: str) -> None:
        self.documento = value

    def GetNombres(self) -> str:
        return self.nombres

    def SetNombres(self, value: str) -> None:
        self.nombres = value

    def GetApellidos(self) -> str:
        return self.apellidos

    def SetApellidos(self, value: str) -> None:
        self.apellidos = value

    def GetId_especialidad(self) -> int:
        return self.id_especialidad

    def SetId_especialidad(self, value: int) -> None:
        self.id_especialidad = value

    def GetTelefono(self) -> str:
        return self.telefono

    def SetTelefono(self, value: str) -> None:
        self.telefono = value

    def GetEmail(self) -> str:
        return self.email

    def SetEmail(self, value: str) -> None:
        self.email = value

    def GetTarjeta_profesional(self) -> str:
        return self.tarjeta_profesional

    def SetTarjeta_profesional(self, value: str) -> None:
        self.tarjeta_profesional = value
