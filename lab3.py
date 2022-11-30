from PIL import Image, ImageDraw
import numpy as np


def rotation_matrix(angle):

    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])


n = 0
angle = 10 * (n + 1)
angle_rad = angle * np.pi / 180

center = np.array([480, 480])

with open('DS0.txt') as f:

    img = Image.new('RGB', (960, 960), '#ffffff')
    draw = ImageDraw.Draw(img)

    matrix = rotation_matrix(angle_rad)

    for i in f.readlines():
        coord = i.split(' ')
        
        point = np.array([float(coord[0]), float(coord[1])])

        rotated_point = np.matmul(matrix, point - center) + center

        draw.point((int(rotated_point[0]), int(rotated_point[1])), '#0000ff')

    img.save('image3.png')