# Программа для создания миниатюр изображений и наложения текста с помощью модуля PIL

from PIL import Image, ImageDraw, ImageFont
import glob, os

size = 128, 128

def get_average_brightness(image):
    # Преобразуем в градации серого
    gray_image = image.convert('L')
    # Получаем размеры изображения
    width, height = gray_image.size
    # Вычисляем среднюю яркость
    pixels = list(gray_image.getdata())
    average_brightness = sum(pixels) / len(pixels)
    return average_brightness


for infile in glob.glob("./module11/img/*.png"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        watermark_image = im.copy()
        
        draw = ImageDraw.Draw(watermark_image)

        w, h = im.size
        x, y = int(w / 2), int(h / 2)
        font_size = min(x, y) // 6
            
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            print("Font file not found. Using default font.")
            font = ImageFont.load_default()

        # Получение средней яркости изображения
        average_brightness = get_average_brightness(im)

        # Устанавливаем цвет текста в зависимости от яркости
        if average_brightness < 128:  # Темное изображение
            text_color = (255, 255, 255)  # Белый цвет для темного изображения
        else:  # Светлое изображение
            text_color = (0, 0, 0)  # Черный цвет для светлого изображения
  
        # add Watermark
        draw.text((x, y), "Urban", fill=text_color, font=font, anchor='ms')
        watermark_image.save(file + ".watermark." + ext, "PNG")
        
        im.thumbnail(size)
        im.save(file + ".thumbnail", "PNG")