from deepface import DeepFace

def analyze_emotion(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'])
        emotion = result['dominant_emotion']
        return emotion
    except Exception as e:
        print(f"Ошибка анализа эмоций: {e}")
        return "Неизвестно"
