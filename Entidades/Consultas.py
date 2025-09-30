class Consultas:
    id_consulta: int = 0
    id_cita: int = 0
    id_historia: int = 0
    diagnostico: str = None
    tratamiento: str = None
    observaciones: str = None
    fecha_consulta: str = None

    def GetId_consulta(self) -> int:
        return self.id_consulta

    def SetId_consulta(self, value: int) -> None:
        self.id_consulta = value

    def GetId_cita(self) -> int:
        return self.id_cita

    def SetId_cita(self, value: int) -> None:
        self.id_cita = value

    def GetId_historia(self) -> int:
        return self.id_historia

    def SetId_historia(self, value: int) -> None:
        self.id_historia = value

    def GetDiagnostico(self) -> str:
        return self.diagnostico

    def SetDiagnostico(self, value: str) -> None:
        self.diagnostico = value

    def GetTratamiento(self) -> str:
        return self.tratamiento

    def SetTratamiento(self, value: str) -> None:
        self.tratamiento = value

    def GetObservaciones(self) -> str:
        return self.observaciones

    def SetObservaciones(self, value: str) -> None:
        self.observaciones = value

    def GetFecha_consulta(self) -> str:
        return self.fecha_consulta

    def SetFecha_consulta(self, value: str) -> None:
        self.fecha_consulta = value
