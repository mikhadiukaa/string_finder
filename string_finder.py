from flask import Flask, render_template, request
from string_finder_func import string_finder_func

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def vsearch() -> str:
    text = request.form['text']
    sign = request.form['sign']
    return render_template('results.html',
                           the_title='Вот ваши результаты:', the_results=string_finder_func(sign, text),
                           the_sign=sign, the_text=text)


@app.route('/')
@app.route('/entry', methods=['GET'])
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to world of Lorem Ipsum')


app.run()
