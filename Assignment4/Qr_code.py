import qrcode

name = input("Enter your name: ")
phone_num = input("Enter your phone number: ")

qr_str = name + ' | ' + phone_num
img = qrcode.make(qr_str)
img.save("name_phone_qrcode.png")
