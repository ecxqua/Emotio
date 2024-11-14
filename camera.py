from plyer import filechooser, camera
from kivy.utils import platform
import os

def select_photo():
    """
    Функция для выбора изображения из галереи.
    Возвращает путь к выбранному изображению.
    """
    if platform == 'android':
        # Открываем галерею и выбираем файл
        file_path = filechooser.open_file(title="Выберите фото", multiple=False)
        if file_path:
            return file_path[0]  # Возвращаем путь к выбранному изображению
    else:
        print("Выбор фото из галереи поддерживается только на Android")
        return None

def take_photo():
    """
    Функция для съемки фотографии с камеры.
    Возвращает путь к сохраненному изображению.
    """
    if platform == 'android':
        # Сохраняем фото в файле и возвращаем его путь
        image_path = os.path.join(os.getenv('EXTERNAL_STORAGE'), "photo.jpg")
        camera.take_picture(filename=image_path, on_complete=lambda *args: print("Фото сохранено"))
        return image_path
    else:
        print("Съемка фото поддерживается только на Android")
        return None
