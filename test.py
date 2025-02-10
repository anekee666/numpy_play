from PIL import Image
import numpy as np

def image_to_numpy(image_path):
    with Image.open(image_path) as img:
        return np.array(img)

def numpy_to_image(np_array, output_path):

    img = Image.fromarray(np_array)
    img.save(output_path)

array=image_to_numpy("1.jpg")
array[0:100,0:100,0]=0
#array[0:100,0:100,1]=0
array[0:100,0:100,2]=0
print(array[:,:,0].shape)
numpy_to_image(array,"2.jpg")