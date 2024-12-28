from PIL import Image
import numpy as np
import sys
import interpreter

def load_image(path):
    img = Image.open(path).convert('RGB')
    data = np.array(img)
    height, width, _ = data.shape

    result = [[None for y in range(height)] for x in range(width)]
    

    for x in range(width):
        for y in range(height):
            result[x][y] = tuple(data[y, x])  
    
    return result

prg = load_image(sys.argv[1])
interp = interpreter.Interpreter(prg)
interp.execute()