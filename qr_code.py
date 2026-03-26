import qrcode
x=qrcode.QRCode()
msg="Life is about to live!!!"
x.add_data(msg)
x.make(fit=True)
res=x.make_image(fill_color="black",back_color="white")
res.save("life.png")
print("Created SUccessfully!!")
