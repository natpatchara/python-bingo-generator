import sys
import glob
from textwrap import fill
from PIL import Image,ImageDraw,ImageFont
import random

def draw_table(draw,posx,posy,rows,cols,size):
    for y in range(rows+1):
        draw.line(((posx,posy+y*size),(posx+cols*size,posy+y*size)),fill="black",width=2)
    for x in range(cols+1):
        draw.line(((posx+x*size,posy),(posx+x*size,posy+rows*size)),fill="black",width=2)

def create_bingo_card(rows,cols,size,images):
    # create blank card
    new_image = Image.new('RGB', (cols*size+50, rows*size+75), (255,255,255))
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype(font='font/THSarabun.ttf', size=42)

    #create random seed
    range_im = random.sample(range(len(images)), rows*cols)
    #draw image
    i = 0
    for y in range(rows):
        if i >= len(images):
            break
        y *= size
        for x in range(cols):
            x *= size
            id = range_im[i]
            img = images[id]
            new_image.paste(img, (x+25, y+50, x+size+25, y+size+50))
            i += 1

    #draw card title
    draw.text(((cols*size+50)/2,25),"ความรู้วัคซีน",fill = (0,0,0), font=font, anchor="mm")
    #draw table
    draw_table(draw, 25, 50, rows, cols, size)

    # save it
    return new_image
