class Factura:
  def __init__(self, ID, vendedor, fecha_compra):
      self.ID = ID
      self.vendedor = vendedor
      self.fecha_compra = fecha_compra

  def print_vendedor(self):
      print("Vendedor:", self.vendedor)

  def print_fecha_compra(self):
      print("Fecha de compra:", self.fecha_compra)

class DetalleFactura(Factura):
  def __init__(self, ID, vendedor, fecha_compra, producto, precio, cantidad):
      super().__init__(ID, vendedor, fecha_compra)
      self.producto = producto
      self.precio = precio
      self.cantidad = cantidad

  def calcular_total(self):
      total = self.precio * self.cantidad
      return total

  def print_producto(self):
      print("Producto:", self.producto)

  def print_precio(self):
      print("Precio:", self.precio)

  def print_cantidad(self):
      print("Cantidad:", self.cantidad)

# Resultado
factura = Factura(ID=1, vendedor="Ryan", fecha_compra="2024-03-04")
factura.print_vendedor()
factura.print_fecha_compra()

detalle_factura = DetalleFactura(ID=2, vendedor="Pedro", fecha_compra="2024-03-05", producto="Producto1", precio=10, cantidad=2)
detalle_factura.print_vendedor()
detalle_factura.print_fecha_compra()
detalle_factura.print_producto()
detalle_factura.print_precio()
detalle_factura.print_cantidad()

total_compra = detalle_factura.calcular_total()
print("Total de la compra:", total_compra)