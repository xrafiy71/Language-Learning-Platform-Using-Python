from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('vocab.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS words (
                        id INTEGER PRIMARY KEY,
                        word TEXT,
                        definition TEXT
                    )''')
    conn.commit()
    conn.close()

# Route to add a new word
@app.route('/add_word', methods=['POST'])
def add_word():
    word = request.form['word']
    definition = request.form['definition']

    conn = sqlite3.connect('vocab.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO words (word, definition)
                      VALUES (?, ?)''', (word, definition))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# Route to display all words
@app.route('/')
def index():
    conn = sqlite3.connect('vocab.db')
   
