class ExamenesLaboratorio:
    id_examen: int = 0
    id_consulta: int = 0
    id_laboratorio: int = 0
    tipo_examen: str = None
    fecha_solicitud: str = None
    fecha_resultado: str = None
    resultado: str = None

    def GetId_examen(self) -> int:
        return self.id_examen

    def SetId_examen(self, value: int) -> None:
        self.id_examen = value

    def GetId_consulta(self) -> int:
        return self.id_consulta

    def SetId_consulta(self, value: int) -> None:
        self.id_consulta = value

    def GetId_laboratorio(self) -> int:
        return self.id_laboratorio

    def SetId_laboratorio(self, value: int) -> None:
        self.id_laboratorio = value

    def GetTipo_examen(self) -> str:
        return self.tipo_examen

    def SetTipo_examen(self, value: str) -> None:
        self.tipo_examen = value

    def GetFecha_solicitud(self) -> str:
        return self.fecha_solicitud

    def SetFecha_solicitud(self, value: str) -> None:
        self.fecha_solicitud = value

    def GetFecha_resultado(self) -> str:
        return self.fecha_resultado

    def SetFecha_resultado(self, value: str) -> None:
        self.fecha_resultado = value

    def GetResultado(self) -> str:
        return self.resultado

    def SetResultado(self, value: str) -> None:
        self.resultado = value
