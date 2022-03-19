import sys
import glob
from PIL import Image
from source.bingo_generator import *

'''# for test only
#sys.argv += ['images/dot-*.png', 2, 3]

# get arguments
pattern = sys.argv[1]
rows = int(sys.argv[2])
cols = int(sys.argv[3])
size = int(sys.argv[4])
#range_im = [i for i in range(rows*cols)]

# get filenames

filenames = glob.glob(pattern)
range_im = random.sample(range(len(filenames)), rows*cols)
# load images and resize to (100, 100)
images = [Image.open(name).resize((size, size)) for name in filenames]

# create empty image to put thumbnails
new_image = Image.new('RGB', (cols*size+50, rows*size+75), (255,255,255))
draw = ImageDraw.Draw(new_image)
font = ImageFont.truetype(font='font/THSarabun.ttf', size=42)

# put thumbnails
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

draw.text(((cols*size+50)/2,25),"ความรู้วัคซีน",fill = (0,0,0), font=font, anchor="mm")

def draw_table(draw,posx,posy,rows,cols,size):
    for y in range(rows+1):
        draw.line(((posx,posy+y*size),(posx+cols*size,posy+y*size)),fill="black",width=2)
    for x in range(cols+1):
        draw.line(((posx+x*size,posy),(posx+x*size,posy+rows*size)),fill="black",width=2)

draw_table(draw, 25, 50, rows, cols, size)


# save it
new_image.save('output.jpg')'''

# get arguments
pattern = sys.argv[1]
rows = int(sys.argv[2])
cols = int(sys.argv[3])
size = int(sys.argv[4])
num_card = int(sys.argv[5])
#range_im = [i for i in range(rows*cols)]

#load resource
# get filenames
filenames = glob.glob(pattern)
# load images and resize to (100, 100)
images = [Image.open(name).resize((size, size)) for name in filenames]

for i in range(num_card):
    card = create_bingo_card(rows,cols,size,images)
    card.save(f'output/card_{i+1}.jpg')
