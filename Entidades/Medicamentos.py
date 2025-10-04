class Medicamentos:
    id_medicamento: int = 0
    nombre: str = None
    descripcion: str = None
    fabricante: str = None
    stock: int = 0

    def GetId_medicamento(self) -> int:
        return self.id_medicamento

    def SetId_medicamento(self, value: int) -> None:
        self.id_medicamento = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    def GetFabricante(self) -> str:
        return self.fabricante

    def SetFabricante(self, value: str) -> None:
        self.fabricante = value

    def GetStock(self) -> int:
        return self.stock

    def SetStock(self, value: int) -> None:
        self.stock = value
