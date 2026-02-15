#OR Code Generator 

# import qrcode as qr
# # make-- geneate qr , save -- in png format

# # img=qr.make("Text / link / Youtube/ Payment / URL")
# # img.save("pritvi.png")

# img=qr.make("https://youtu.be/jIQ0Dx-4peE?si=FKKoUVqpVxElW2WH")
# img.save("GUMAAN_by_Talha_Anjum.png")


import qrcode
from PIL import Image

qr= qrcode.QRCode(version=1, error_correction= qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data("https://")
img= qr.make_image(fill_color="red", back_color="black")
img.save("webpage.png")