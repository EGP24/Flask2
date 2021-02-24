from flask import Flask, render_template

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
@app.route('/auto_answer')
def answer():
    kwargs = {'title': 'Анкета'}


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')