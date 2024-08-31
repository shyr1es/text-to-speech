import asyncio
import edge_tts

VOICES = {
    '1': 'kk-KZ-AigulNeural',  # Казахский голос
    '2': 'en-US-GuyNeural',    # Английский голос
    '3': 'en-US-JennyNeural',  # Английский голос
    '4': 'ru-RU-DmitryNeural'  # Русский голос
}

def list_voices():
    print("Доступные голоса:")
    for key, value in VOICES.items():
        print(f"{key}. {value}")

async def text_to_speech(text, voice, output_file):
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        print(f"Файл успешно сохранен как {output_file}")
        return output_file
    except Exception as e:
        print(f"Ошибка при преобразовании текста в речь: {e}")
        return None

def main():
    # Вывод списка доступных голосов и выбор пользователя
    list_voices()
    voice_choice = input("Выберите голос (введите номер): ")
 #дефолт язык казахский
    voice = VOICES.get(voice_choice, 'kk-KZ-AigulNeural')


    text = input("Введите текст для преобразования в речь: ")
    output_file = input("Введите имя выходного файла (например, 'output.mp3'): ") or "test_kazakh.mp3"

#запуск асинхроннки
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        file_path = loop.run_until_complete(text_to_speech(text, voice, output_file))
    finally:
        loop.close()

if __name__ == "__main__":
    main()
