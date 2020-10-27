
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """Shows a greeting to the user."""
    return f'Are you there, world? It\'s me, Ducky!'


@app.route('/frog')
def my_favorite_animal():
    """shows user my favorite animal"""
    return f'Frogs are cute!'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}'


@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    return f'That is one {adjective} {noun}'


@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if (number1.isdigit() == True) & (number2.isdigit() == True):
        answer = int(number1) * int(number2)
        return answer
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"


@app.route('/sayntimes/<word>/<number>')
def sayntimes(word, number):
    if number.isdigit() == True:
        string = ""
        for word in range(int(number)):
            string += str(word)
        return
    else:
        return f"Invalid input. Please try again by entering a word and a number!"


if __name__ == '__main__':
    app.run(debug=True)
