from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# названия картинки и фона потому что заебал менять их каждый раз в центре кода
picture_name = "pic#1.jpg"
background_name = "background.jpg"

# директории с картинками и результатом потому что заебал все хранить в одной папке
picture_dir = os.getcwd() + "/pics"
result_dir = os.getcwd() + "/result"

# текста ОСНОВНОЙ ТЕГИ и ВРЕМЯ
text1 = "Советские школьники поймали на улице солиста Рамштайн и  хорошо наглумились над старым фошыздом своими 76 мм пушками от Т-34."
text2 = "Минет и сперма; Великовозрастное; Растреляли; Pussy; Повторили!; Анальное расследование; Немецкое; Групповая оргия; Танковое сражение на анальных просторах."
text3 = "1941:1945"

# [text, font_size, color, line_width, x_cord]
content = [[text1, 23, "#aa0000", 32, 20],
           [text2, 20, "#000000", 38, 25],
           [text3, 15, "#000000", 10, 370]]

# функция высчитывающая размер всего текста и при draw=true печатающая его на картинке
def text_pasting(draw=False):
    offset = 320
    for i in content:
        for line in textwrap.wrap(i[0], width=i[3]):
            if draw:
                result.text((i[4], offset), line, font=ImageFont.truetype("main_font.ttf", i[1]), fill=i[2])
            offset += ImageFont.truetype("main_font.ttf", i[1]).getsize(line)[1]
        offset += 15
    return offset

# открытие картинки и фона с новыми гибкими параметрами
picture = Image.open(f"{picture_dir}/{picture_name}")
background = Image.open(f"{picture_dir}/{background_name}")

# подгон нужных размеров для картинки и фона
background = background.resize((470, text_pasting()))
picture = picture.resize((440, 300))

# совмещение картинки и фона в окончательный пиздец
background.paste(picture, (15, 15))
result = ImageDraw.Draw(background)

# ну ты понял
text_pasting(draw=True)

background.save(f'{result_dir}/result_center.jpg', 'jpeg')
