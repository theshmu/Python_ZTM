import sys
import os
from PIL import Image

input_path = sys.argv[1]
output_path = sys.argv[2]

if os.path.exists(input_path) is False:
    while True:
        input_path = input('Input path does not exist. please enter a valid input path. ')
        if os.path.exists(input_path):
            break
        else:
            continue

for file in os.listdir(input_path):
    if os.path.isdir(file):
        continue
    f, e = os.path.splitext(file)
    if e == '.png':
        continue
    im = Image.open(input_path + '\\' + file)
    if os.path.exists(output_path) is False:
        os.makedirs(output_path)

    im.save(output_path + '\\' + f + '.png')
