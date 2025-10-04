class Laboratorios:
    id_laboratorio: int = 0
    nombre: str = None
    direccion: str = None
    telefono: str = None

    def GetId_laboratorio(self) -> int:
        return self.id_laboratorio

    def SetId_laboratorio(self, value: int) -> None:
        self.id_laboratorio = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetDireccion(self) -> str:
        return self.direccion

    def SetDireccion(self, value: str) -> None:
        self.direccion = value

    def GetTelefono(self) -> str:
        return self.telefono

    def SetTelefono(self, value: str) -> None:
        self.telefono = value
