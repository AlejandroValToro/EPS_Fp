class Citas:
    id_cita: int = 0
    id_paciente: int = 0
    id_medico: int = 0
    fecha_hora: str = None
    estado: str = None
    motivo: str = None

    def GetId_cita(self) -> int:
        return self.id_cita

    def SetId_cita(self, value: int) -> None:
        self.id_cita = value

    def GetId_paciente(self) -> int:
        return self.id_paciente

    def SetId_paciente(self, value: int) -> None:
        self.id_paciente = value

    def GetId_medico(self) -> int:
        return self.id_medico

    def SetId_medico(self, value: int) -> None:
        self.id_medico = value

    def GetFecha_hora(self) -> str:
        return self.fecha_hora

    def SetFecha_hora(self, value: str) -> None:
        self.fecha_hora = value

    def GetEstado(self) -> str:
        return self.estado

    def SetEstado(self, value: str) -> None:
        self.estado = value

    def GetMotivo(self) -> str:
        return self.motivo

    def SetMotivo(self, value: str) -> None:
        self.motivo = value
