import qrcode

image = qrcode.make("https://google.com")

image.save("qr_code.png")
print("QR code Generated Successfully!")