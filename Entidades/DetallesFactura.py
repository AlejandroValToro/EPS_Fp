class DetallesFactura:
    id_detalle: int = 0
    id_factura: int = 0
    concepto: str = None
    cantidad: int = 0
    precio_unitario: float = 0.0
    subtotal: float = 0.0

    def GetId_detalle(self) -> int:
        return self.id_detalle

    def SetId_detalle(self, value: int) -> None:
        self.id_detalle = value

    def GetId_factura(self) -> int:
        return self.id_factura

    def SetId_factura(self, value: int) -> None:
        self.id_factura = value

    def GetConcepto(self) -> str:
        return self.concepto

    def SetConcepto(self, value: str) -> None:
        self.concepto = value

    def GetCantidad(self) -> int:
        return self.cantidad

    def SetCantidad(self, value: int) -> None:
        self.cantidad = value

    def GetPrecio_unitario(self) -> float:
        return self.precio_unitario

    def SetPrecio_unitario(self, value: float) -> None:
        self.precio_unitario = value

    def GetSubtotal(self) -> float:
        return self.subtotal

    def SetSubtotal(self, value: float) -> None:
        self.subtotal = value
