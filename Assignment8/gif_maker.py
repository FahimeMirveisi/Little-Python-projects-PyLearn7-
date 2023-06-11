import os
import imageio

file_list = sorted(os.listdir("../Assignment8/images"))

IMAGES = []
for file_name in file_list:

    file_path = "../Assignment8/images/" + file_name
    print(file_path)
    image = imageio.imread(file_path)
    IMAGES.append(image)

print(IMAGES)
imageio.mimsave("../Assignment8/outgif.gif",IMAGES)
