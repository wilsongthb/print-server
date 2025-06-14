from escpos.printer import Usb
from datetime import datetime

# Reemplaza con los IDs correctos de tu impresora (ver `lsusb` en Linux)
VENDOR_ID = 0x04b8
PRODUCT_ID = 0x0e15

# Crear impresora USB
printer = Usb(VENDOR_ID, PRODUCT_ID)

# === CABECERA ===
printer.set(align='center', text_type='B')
printer.text("PARA MESA\n")

# Número de mesa con fondo negro (negrita, doble tamaño)
printer.set(align='center', width=2, height=2, invert=True)
printer.text("880001\n")

printer.set(align='center')
printer.text("----------------------------------------\n")

# === DATOS DE LA ORDEN ===
printer.set(align='left', text_type='A')
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
printer.text(f"Fecha:     {fecha}\n")
printer.text("Cajero:    Caja Puno Centro\n")

# === PRODUCTOS ===
printer.text("02 1/8 A LA BRASA - SALCEDO      S/ 18.00\n")

# === TOTALES ===
printer.text("\n")
printer.text("Total                         S/ 18.00\n")
printer.text("Total Bruto                  S/ 20.00\n")
printer.text("Vuelto                        S/ 2.00\n")

printer.text("\n")
# === MENSAJE FINAL ===
printer.set(align='center')
printer.text("----------------------------------------\n")
printer.set(align='center', text_type='B')
printer.text("No es comprobante de pago valido para\n")
printer.text("efecto tributario, canjear por Boleta\n")

# Cortar papel
printer.cut()