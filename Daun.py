import numpy as np
import imageio.v3 as img

image_path = "Kenikir.jpeg"
image = img.imread(image_path)

if len(image.shape) < 3 or image.shape[2] != 3:
    print("Format gambar harus RGB")
    exit()

red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

image_red = np.zeros_like(image)
image_red[:, :, 0] = red  

image_green = np.zeros_like(image)
image_green[:, :, 1] = green 

image_blue = np.zeros_like(image)
image_blue[:, :, 2] = blue  

gray = 0.299 * red + 0.587 * green + 0.114 * blue

image_gray = np.zeros_like(image)
image_gray[:, :, 0] = gray
image_gray[:, :, 1] = gray
image_gray[:, :, 2] = gray


threshold = 100  
bw_image = np.where(image_gray[:, :, 0] > threshold, 255, 0)  

img.imwrite("Merah.jpg", image_red)
img.imwrite("Hijau.jpg", image_green)
img.imwrite("Biru.jpg", image_blue)
img.imwrite("Grayscale.jpg", image_gray.astype(np.uint8))
img.imwrite("Hitam Putih.jpg", bw_image.astype(np.uint8))

print("Proses Done Ngabb")