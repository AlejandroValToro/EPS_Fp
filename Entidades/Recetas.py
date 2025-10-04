class Recetas:
    id_receta: int = 0
    id_consulta: int = 0
    id_medicamento: int = 0
    dosis: str = None
    frecuencia: str = None
    duracion: str = None
    fecha_receta: str = None

    def GetId_receta(self) -> int:
        return self.id_receta

    def SetId_receta(self, value: int) -> None:
        self.id_receta = value

    def GetId_consulta(self) -> int:
        return self.id_consulta

    def SetId_consulta(self, value: int) -> None:
        self.id_consulta = value

    def GetId_medicamento(self) -> int:
        return self.id_medicamento

    def SetId_medicamento(self, value: int) -> None:
        self.id_medicamento = value

    def GetDosis(self) -> str:
        return self.dosis

    def SetDosis(self, value: str) -> None:
        self.dosis = value

    def GetFrecuencia(self) -> str:
        return self.frecuencia

    def SetFrecuencia(self, value: str) -> None:
        self.frecuencia = value

    def GetDuracion(self) -> str:
        return self.duracion

    def SetDuracion(self, value: str) -> None:
        self.duracion = value

    def GetFecha_receta(self) -> str:
        return self.fecha_receta

    def SetFecha_receta(self, value: str) -> None:
        self.fecha_receta = value
