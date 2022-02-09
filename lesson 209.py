from PIL import Image
import os

path = '.\Pokedex\squirtle.jpg'
im = Image.open(path)

# im.show()
f, e = os.path.splitext(path)
output = f + '.png'
im.save(output)
