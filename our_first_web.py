from pywebio.input import input
from pywebio.output import put_text, put_html, put_image, put_markdown
from pywebio import start_server


def main():
    # Заголовок
    put_html('<h1>УРА, ЛІТО!</h1>')


    put_text("""
    Літо настало, ура!
    Сонце світить нам щодня.
    Відпочинок чекає нас,
    Сміх і радість весь цей час! 😊🌞
    """)

    # Запрошення на введення текстових даних
    plans = input("Введіть ваші плани на літо")

    # Повідомлення про кількість символів
    put_text(f"Ви ввели {len(plans)} символів у ваших планах на літо.")

    # Фото, що відображає сподівання на літо
    put_image('https://example.com/your_summer_image.jpg')  # Замість URL вставте реальне посилання на зображення


if __name__ == '__main__':
    start_server(main, port=8080)
