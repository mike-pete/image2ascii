from PIL import Image

try: imageFile = sys.argv[1]
except: imageFile = 'ross.png'

image = Image.open(imageFile)
X,Y = image.size
image = image.convert('RGB')

# lazy conversion of rgb to ascii
def rgb2char(rgb):
    r,g,b = rgb
    avg = int((r+g+b)/3)
    characters = '''%@#|>/;:"',. '''
    maths = 256/len(characters)
    return characters[int(avg/maths)]*2

ascii = ''
# loop through pixels
for y in range(1,Y):
    for x in range(1,X):
        # get rgb value of current pixel
        rgb = image.getpixel((x, y))
        ascii += rgb2char(rgb)
    ascii += '\n' 


with open("index.html","w") as f:
    f.write('''
    <!DOCTYPE html>
    <html>
        <head>
            <link href="https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap" rel="stylesheet">
                <style>
                *{
                    margin:0;
                    font-family:"Courier New", Courier, monospace;
                    font-family: 'Roboto Mono', monospace;
                    font-size:2px;
                    white-space: pre;
                    line-height: 1.2;    
                }
            </style>
        </head>
        <body>
            <p>''' + ascii + '''<p>
        </body>
    </html>''')
    
