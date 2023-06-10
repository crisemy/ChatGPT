import random
from flask import Flask, render_template

app = Flask(__name__)

# Read quotes from the file and store them in a list
with open('quotes.txt', 'r') as file:
    quotes = [line.strip() for line in file]

@app.route('/')
def index():
    # Choose a random quote from the list
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run()

