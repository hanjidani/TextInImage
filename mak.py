from PIL import Image, ImageFont, ImageDraw 
import cv2
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np
location = ((1997, 1300))
file_name = 'sample.jpg'
image = Image.open(file_name) 
font = ImageFont.truetype('vazir.ttf', 80, encoding='unic')
draw = ImageDraw.Draw(image) 
text = 'دهقانيييييييييييييييييي'
reshaped_text = arabic_reshaper.reshape(text) # correct its shape
bidi_text = get_display(reshaped_text) # correct its direction

draw.text(location, bidi_text,(0, 0, 0), font = font, align='center', dir='rtl', anchor='mm') 
open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("kos.jpg", img=open_cv_image)
im = image.convert("RGB")
im.save("kos.pdf")
# cv2.imshow('open_cv_image',open_cv_image)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()
# image.show()
