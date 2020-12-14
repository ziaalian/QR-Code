import os
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=QO6gasg2f8M&ab_channel=AishaSaleous")
img.save("qr.png", "PNG")
os.system("open qr.png")
