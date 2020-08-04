from PIL import Image, ImageDraw, ImageFont
import os

background_name = "background.jpg"

picture_dir = os.getcwd() + "/pics"
result_dir = os.getcwd() + "/result"

background = Image.open(f"{picture_dir}/{background_name}")
background = background.resize((470, 600))

result = ImageDraw.Draw(background)

background.save(f'{result_dir}/align_test.jpg', 'jpeg')
