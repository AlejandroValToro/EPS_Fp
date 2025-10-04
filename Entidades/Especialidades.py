class Especialidades:
    id_especialidad: int = 0
    nombre: str = None
    descripcion: str = None

    def GetId_especialidad(self) -> int:
        return self.id_especialidad

    def SetId_especialidad(self, value: int) -> None:
        self.id_especialidad = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value
