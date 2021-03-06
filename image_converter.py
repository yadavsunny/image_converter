import os
from PIL import Image
import sys


path = sys.argv[1]
directory = sys.argv[2]


if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        print(filename)
        img = Image.open(f'{path}{filename}')
        clear_name = os.path.splitext(filename)[0]
        img.save(f'{directory}/{clear_name}.png', 'png')
        print("all done")
