from escpos.printer import Usb

# Configura los IDs de tu impresora USB (ajusta si es necesario)
USB_VENDOR_ID = 0x04b8  # Epson
USB_PRODUCT_ID = 0x0e15 # TM-T20II
USB_INTERFACE = 0       # Usualmente 0

try:
    printer = Usb(USB_VENDOR_ID, USB_PRODUCT_ID, interface=USB_INTERFACE)
    printer.text("=== Prueba de conexión Epson TM-T20II ===\n\n")
    printer.set(bold=True)
    printer.text("Texto en negrita\n")
    printer.set(bold=False, italic=True)
    printer.text("Texto en cursiva\n")
    printer.set(italic=False, font='b')
    printer.text("Texto en fuente B\n")
    printer.set(font='a')
    printer.text("Texto en fuente A\n")
    printer.set(align='center')
    printer.text("Texto centrado\n")
    printer.set(align='left')
    printer.text("\n--- Fin de la prueba ---\n\n")
    printer.cut()
    printer.close()
    print("Prueba enviada correctamente.")
except Exception as e:
    print(f"Error al conectar o imprimir: {e}")