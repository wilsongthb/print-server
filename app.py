from flask import Flask, request, jsonify
from escpos.printer import Usb

app = Flask(__name__)``

# Configura los IDs de tu impresora USB (busca estos valores con 'lsusb' en Linux o en las propiedades del dispositivo en Windows)
USB_VENDOR_ID = 0x04b8  # Ejemplo: Epson
USB_PRODUCT_ID = 0x0e15 # Ejemplo: TM-T20
USB_INTERFACE = 0       # Usualmente 0

def send_to_printer(lines, cut_command):
    try:
        printer = Usb(USB_VENDOR_ID, USB_PRODUCT_ID, interface=USB_INTERFACE)
        for line in lines:
            printer.text(line + '\n')
        if cut_command:
            printer.cut()
        printer.close()
        return True
    except Exception as e:
        print(f"Error al imprimir: {e}")
        return False

@app.route('/print', methods=['POST'])
def print_ticket():
    data = request.get_json()
    if not data or 'lines' not in data or 'cut' not in data:
        return jsonify({'error': 'Formato inválido'}), 400

    lines = data['lines']
    cut = data['cut']

    if not isinstance(lines, list) or not isinstance(cut, bool):
        return jsonify({'error': 'Datos incorrectos'}), 400

    success = send_to_printer(lines, cut)
    if success:
        return jsonify({'status': 'impreso'}), 200
    else:
        return jsonify({'error': 'No se pudo imprimir'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)