#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')
#Вторая страница
@app.route('/info')
def info(): 
     return render_template('info.html')
@app.route('/prichina')
def prichina(): 
     return render_template('prichina.html')
@app.route('/posledstvia')
def posledstvia(): 
     return render_template('posledstvia.html')
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

#Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

#Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
#Форма
@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']
    with open('form.txt', 'a',) as f:
            f.write(name + '\n')
            f.write(email + '\n')
            f.write(address + '\n')
            f.write(date + '\n')
    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html',name=name,email=email,address=address,date=date)

app.run(debug=True)