class Empleados:
    id_empleado: int = 0
    documento: str = None
    nombres: str = None
    apellidos: str = None
    id_departamento: int = 0
    cargo: str = None
    fecha_contratacion: str = None

    def GetId_empleado(self) -> int:
        return self.id_empleado

    def SetId_empleado(self, value: int) -> None:
        self.id_empleado = value

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

    def GetId_departamento(self) -> int:
        return self.id_departamento

    def SetId_departamento(self, value: int) -> None:
        self.id_departamento = value

    def GetCargo(self) -> str:
        return self.cargo

    def SetCargo(self, value: str) -> None:
        self.cargo = value

    def GetFecha_contratacion(self) -> str:
        return self.fecha_contratacion

    def SetFecha_contratacion(self, value: str) -> None:
        self.fecha_contratacion = value
