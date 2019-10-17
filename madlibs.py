"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 5)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():
    """Playing game"""

    if request.args.get("play_game") == "Yes":
        return render_template("/game.html")
    else:
        return render_template("/goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Display madlib results based off of game answers"""

    noun = request.args.get("noun")
    color = request.args.get("color")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    verb = request.args.get("verb")
    animals = request.args.getlist('animals')


    surprise = request.args.get("surprise")

    madlibs = ["madlib.html", "madlib2.html"]

    return render_template(
                            choice(madlibs),
                            color=color,
                            noun=noun,
                            person=person,
                            adjective=adjective,
                            verb=verb,
                            surprise=surprise,
                            animals=animals
                            )

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
