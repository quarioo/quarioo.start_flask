from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def first_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_list = ['Человечество вырастает из детства.',
                      'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.',
                      'И начнем с Марса!',
                      'Присоединяйся!']

    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def image_mars():
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/riana.jpg')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <figcaption>подпись под картинкой</figcaption>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
