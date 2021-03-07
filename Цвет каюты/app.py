from flask import Flask, render_template
from random import randint
app = Flask(__name__)


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
    image_path = 'img/child.png' if age < 21 else 'img/adult.png'
    color = (255, 0, randint(0, 255)) if sex == 'female' else (0, randint(0, 255), 255)
    color = [f'{"0" * int(len(hex(i)) == 3)}{hex(i)[2:]}' for i in color]
    return render_template('table.html', title='Анкета', color=','.join(color), age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')