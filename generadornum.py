import qrcode;

def qrTelefono (numero):
    contenido = f"celular:{numero}"
    
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(contenido)
    qr.make(fit=True)
    
    imagen = qr.make_image(fill_color="black", back_color="white");
    return imagen

numTelefono = " 11-3633-2152 "


codigo_qr = qrTelefono(numTelefono);


qrImagen = "yourName.jpg"
codigo_qr.save(qrImagen)

print({qrImagen});
