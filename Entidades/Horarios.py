class Horarios:
    id_horario: int = 0
    id_medico: int = 0
    dia_semana: str = None
    hora_inicio: str = None
    hora_fin: str = None

    def GetId_horario(self) -> int:
        return self.id_horario

    def SetId_horario(self, value: int) -> None:
        self.id_horario = value

    def GetId_medico(self) -> int:
        return self.id_medico

    def SetId_medico(self, value: int) -> None:
        self.id_medico = value

    def GetDia_semana(self) -> str:
        return self.dia_semana

    def SetDia_semana(self, value: str) -> None:
        self.dia_semana = value

    def GetHora_inicio(self) -> str:
        return self.hora_inicio

    def SetHora_inicio(self, value: str) -> None:
        self.hora_inicio = value

    def GetHora_fin(self) -> str:
        return self.hora_fin

    def SetHora_fin(self, value: str) -> None:
        self.hora_fin = value
