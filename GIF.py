
import imageio.v3 as iio

# Пути к файлам (замени если нужно)
filenames = ['One_pic.png', 'Second_pic.png']
images = [ ]
# Проверка существования
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

