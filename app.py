from flask import Flask

app = Flask(__name__)


@app.route('/soma/<num1>/<num2>')
def soma(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'{num1} + {num2} =  {num1 + num2}'
    except ValueError:
        return f"Digite um número"

@app.route('/subtracao/<num1>/<num2>')
def subtracao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'{num1} - {num2} =  {num1 - num2}'
    except ValueError:
        return f"Digite um número"

@app.route('/multiplicacao/<num1>/<num2>')
def multiplicacao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return (f'{num1} * {num2} =  {num1 * num2}')
    except ValueError:
        return f"Digite um número"

@app.route('/divisao/<num1>/<num2>')
def divisao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'{num1} / {num2} =  {num1 / num2}'
    except ValueError:
        return f"Digite um número"

@app.route('/par-impar/<num>')
def valor(num):
    try:
        num = int(num)
        resultado = num % 2
        if resultado == 0:
            return f'Par'
        else:
            return f'Impar'
    except ValueError:
        return f"Digite um número"



if __name__ == '__main__':
    app.run(debug=True)
