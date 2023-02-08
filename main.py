from flask import Flask, url_for, request

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


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Колонизация</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" type="text/css"/>
                </head>
                  <body>
                    <h1>Hello, world!</h1>
                    <img src="{url_for('static', filename='img/riana.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
                </body>
                </html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Колонизация</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" type="text/css"/>
                </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert alert-dark" role="alert">
                      Передо мной интересная фотография
                    </div>
                    <div class="alert alert-success" role="alert">
                      На ней изображен(а) {planet_name}
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Давайте рассмотрим изображение внимательнее.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      На переднем плане мы видим несколько кратеров
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Они довольно большие и глубокие.
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
                </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def austronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="ru">
                    
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Пример формы</title>
                    </head>
                    
                    <body>
                        <div class="title">
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                        </div>
                    
                        <form class="login_form" method="post">
                            <div class="form-group">
                                <div class="form-floating">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <label for="floatingInput">Введите фамилию</label>
                                </div>
                                <div class="form-floating">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="floatingInput">Введите имя</label>
                                </div>
                            </div>
                    
                            <div class="form-group">
                                <div class="form-floating">
                                    <input type="email" class="form-control" id="input-email" placeholder="Введите адресс электронной почты" name="email">
                                    <label for="floatingInput">Введите адресс электронной почты</label>
                                </div>
                            </div>
                    
                            <div class="form-group">
                                <label for="educationSelect">Какое у вас образование</label>
                                <select class="form-select" name="education">
                                    <option value="1">Общее</option>
                                    <option value="2">Профессиональное</option>
                                    <option value="3">Дополнительное</option>
                                </select>
                            </div>
                    
                            <div class="form-group">
                                <label for="workCheck">Какие у вас есть профессии?</label>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Инженер-исследователь
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Пилот
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Строитель
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Экзобиолог
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Врач
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Инженер по терраформированию
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Климатолог
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Специалист по радиационной защите
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Астрогеолог
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Гляциолог
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Инженер жизнеобеспечения
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Метеоролог
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Оператор марсохода
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Киберинженер
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Штурман
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="work">
                                    <label class="form-check-label" for="flexCheckDefault">
                                        Пилот дронов
                                    </label>
                                </div>
                            </div>
                    
                            <div class="form-group">
                                <label for="sexRadio">Укажите пол</label>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="sex" checked>
                                    <label class="form-check-label" for="flexRadioDefault1">
                                        Мужской
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="sex">
                                    <label class="form-check-label" for="flexRadioDefault2">
                                        Женский
                                    </label>
                                </div>
                            </div>
                    
                            <div class="form-group">
                                <label for="about">Почему вы хотите принять участие в миссии?</label>
                                <textarea class="form-control" id="about" rows="3" name="why"></textarea>
                            </div>
                    
                            <div class="form-group">
                                <label for="photo">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                    
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                            </div>
                    
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                        </div>
                    </body>
                    
                    </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['emain'])
        print(request.form['education'])
        print(request.form['work'])
        print(request.form['sex'])
        print(request.form['why'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
