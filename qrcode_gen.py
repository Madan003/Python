import qrcode

url = input("Enter the Url: ").strip()
file_path = "qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code Generated Successfully!")