from PIL import Image, ImageDraw, ImageFont
import textwrap

text1 = "Советские школьники поймали на  улице солиста Рамштайн и  хорошо наглумились над старым фошыздом своими 76 мм пушками от Т-34."
text2 = "Минет и сперма;Великовозрастное; Растреляли; Pussy; Повторили!; Анальное расследование; Немецкое; Групповая оргия; Танковое сражение на анальных просторах."
text3 = "1941:1945"

# [text, font_size, color, line_width, x_cord]
content = [[text1, 23, "#aa0000", 36, 25],
           [text2, 20, "#000000", 40, 25],
           [text3, 15, "#000000", 10, 400]]

def text_pasting(draw=False):
    offset = 320
    for i in content:
        for line in textwrap.wrap(i[0], width=i[3]):
            if draw:
                result.text((i[4], offset), line, font=ImageFont.truetype("comic.ttf", i[1]), fill=i[2])
            offset += ImageFont.truetype("main_font.ttf", i[1]).getsize(line)[1]
        offset += 15
    return offset

picture = Image.open("pics/pic#1.jpg")
background = Image.open("pics/background.jpg")

background = background.resize((470, text_pasting()))
picture = picture.resize((440, 300))

background.paste(picture, (15, 15))
result = ImageDraw.Draw(background)

text_pasting(draw=True)

background.save('result/text_result.jpg', 'jpeg')
