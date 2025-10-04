class HistoriasClinicas:
    id_historia: int = 0
    id_paciente: int = 0
    fecha_creacion: str = None
    antecedentes: str = None

    def GetId_historia(self) -> int:
        return self.id_historia

    def SetId_historia(self, value: int) -> None:
        self.id_historia = value

    def GetId_paciente(self) -> int:
        return self.id_paciente

    def SetId_paciente(self, value: int) -> None:
        self.id_paciente = value

    def GetFecha_creacion(self) -> str:
        return self.fecha_creacion

    def SetFecha_creacion(self, value: str) -> None:
        self.fecha_creacion = value

    def GetAntecedentes(self) -> str:
        return self.antecedentes

    def SetAntecedentes(self, value: str) -> None:
        self.antecedentes = value
