from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from camera import select_photo, take_photo
from emotion_analysis import analyze_emotion
from database import Database
import os


class EmotionRecognitionApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database('emotion_history.db')
        self.image_path = None

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Виджет для отображения изображения
        self.image = Image()
        layout.add_widget(self.image)

        # Кнопка для выбора фото из галереи
        btn_gallery = Button(text="Выбрать фото из галереи")
        btn_gallery.bind(on_press=self.select_photo)
        layout.add_widget(btn_gallery)

        # Кнопка для съемки фото
        btn_camera = Button(text="Сделать снимок")
        btn_camera.bind(on_press=self.take_photo)
        layout.add_widget(btn_camera)

        # Кнопка для просмотра истории
        btn_history = Button(text="Просмотр истории")
        btn_history.bind(on_press=self.show_history)
        layout.add_widget(btn_history)

        # Метка для отображения результата
        self.label = Label(text="Результат распознавания появится здесь")
        layout.add_widget(self.label)

        return layout

    def select_photo(self, instance):
        self.image_path = select_photo()
        if self.image_path:
            self.image.source = self.image_path
            self.detect_emotion()

    def take_photo(self, instance):
        self.image_path = take_photo()
        if self.image_path:
            self.image.source = self.image_path
            self.detect_emotion()

    def detect_emotion(self):
        if self.image_path:
            emotion = analyze_emotion(self.image_path)
            self.label.text = f"Распознанная эмоция: {emotion}"
            self.db.save_record(self.image_path, emotion)

    def show_history(self, instance):
        history = self.db.get_history()
        for record in history:
            print(record)


if __name__ == "__main__":
    EmotionRecognitionApp().run()
