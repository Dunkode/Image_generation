from PIL import ImageFont, ImageDraw
from utils import textProcessor as tp

def drawTextOnImage(pillow_img, text_write, max_char):
    width = 10
    height = calculateHeight(pillow_img.size[1], text_write, max_char)
    draw = ImageDraw.Draw(pillow_img)
    font  = ImageFont.truetype('./fonts/TIMESI.TTF', 30)

    
    draw.text((width, 
    height), 
          text_write, 
          font=font, 
          fill='#000000')

def drawNumberOfImage(pillow_img, number):
    width = 397
    height = 77
    draw = ImageDraw.Draw(pillow_img)
    font  = ImageFont.truetype('./fonts/TIMESBI.TTF', 32)

    
    draw.text((width - len(number) * 2, (height//2)), 
                f'~{number}', 
                font=font, 
                fill='#000000')

def calculateHeight(height, text, max_char):
    qtd_lines = tp.calculeLineBrokes(text, max_char)
    height = height//2

    if (qtd_lines > 8):
        for i in range(0, qtd_lines - 8):
            if i < 3:
                height -= 32
        return height

    else:
        return height


