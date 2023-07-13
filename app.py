from flask import Flask, request, render_template
from textblob import Word

app = Flask(__name__)

@app.route('/spell-check', methods=['GET', 'POST'])
def spell_check():
    if request.method == 'GET':
        return render_template('spell_check.html')
    else:
        word = request.form['word']
        is_correct = Word(word).spellcheck()[0][0] == word
        if is_correct:
            return 'The word "{}" is spelled correctly.'.format(word)
        else:
            return 'The word "{}" is spelled incorrectly.'.format(word)

if __name__ == '__main__':
    app.run(debug=True)
