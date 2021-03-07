from flask import Flask, render_template, request
from random import randint
from datetime import datetime
from form import MyForm
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key_also_fesenko_lox)))'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', profession=prof, title='Тренировка')


@app.route('/list_prof/<lst>')
def list_prof(lst):
    profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
             'климатолог', 'специалитс по радиоционной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
             'метеоролог', 'оператор марсаходп', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('prof_list.html', list=lst, title='Список профессий', profs=profs)


@app.route('/answer')
def answer():
    form = {'Фамилия': 'Wanty', 'Имя': 'Mark', 'Образование': 'выше среднего', 'Профессия': 'штурман марсохода',
            'Пол': 'male', 'Мотивация': 'Всегда мечтал застрять на Марсе!', 'Готовы остаться на Марсе?': 'True'}
    return render_template('auto_answer.html', title='Анкета', form=form)


@app.route('/auto_answer/<surname>/<name>/<education>/<profession>/<sex>/<motivation>/<ready>')
def auto_answer(surname, name, education, profession, sex, motivation, ready):
    form = {'Фамилия': surname, 'Имя': name, 'Образование': education, 'Профессия': profession,
            'Пол': sex, 'Мотивация': motivation, 'Готовы остаться на Марсе?': ready}
    return render_template('auto_answer.html', title='Анкета', form=form)


@app.route('/distribution')
def distribution():
    man = ['Переверза Владислав', 'Фесенко Артём', 'Соловьёв Александр', 'Ридли Скотт', 'Энди Уир']
    return render_template('distribution.html', title='Анкета', man=man)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    color = (255, 0, randint(0, 255)) if sex == 'female' else (0, randint(0, 255), 255)
    color = [f'{"0" * int(len(hex(i)) == 3)}{hex(i)[2:]}' for i in color]
    return render_template('table.html', title='Анкета', color=''.join(color), age=age)


@app.route('/gallery', methods=['POST', 'GET'])
def gallery():
    form = MyForm()
    if not os.path.exists('static/img'):
        os.mkdir('static/img')
    if not os.path.exists('static/img/gallery'):
        os.mkdir('static/img/gallery')
    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(f'user_image_{datetime.now()}')
        file.save(f'static/img/gallery/{filename}.jpg')
    images_path = os.listdir('static/img/gallery')
    return render_template('gallery.html', title='Анкета', images_path=images_path, form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')