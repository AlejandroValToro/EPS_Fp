class Departamentos:
    id_departamento: int = 0
    nombre: str = None
    descripcion: str = None

    def GetId_departamento(self) -> int:
        return self.id_departamento

    def SetId_departamento(self, value: int) -> None:
        self.id_departamento = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value
