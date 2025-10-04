class Facturas:
    id_factura: int = 0
    id_paciente: int = 0
    fecha_emision: str = None
    monto_total: float = 0.0
    estado: str = None

    def GetId_factura(self) -> int:
        return self.id_factura

    def SetId_factura(self, value: int) -> None:
        self.id_factura = value

    def GetId_paciente(self) -> int:
        return self.id_paciente

    def SetId_paciente(self, value: int) -> None:
        self.id_paciente = value

    def GetFecha_emision(self) -> str:
        return self.fecha_emision

    def SetFecha_emision(self, value: str) -> None:
        self.fecha_emision = value

    def GetMonto_total(self) -> float:
        return self.monto_total

    def SetMonto_total(self, value: float) -> None:
        self.monto_total = value

    def GetEstado(self) -> str:
        return self.estado

    def SetEstado(self, value: str) -> None:
        self.estado = value
