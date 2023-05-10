from flask import Flask, render_template, url_for, request, redirect, session , Markup
import requests
import markdown
app = Flask(__name__)
app.secret_key = 'mysecretkey'

def get_quote():
    url = f'https://api.quotable.io/random?tag={session["tag"]}'
    response = requests.get(url)
    data = response.json()
    content = data['content']
    author = data['author']
    quote = [content, author]
    return quote


@app.route('/')
def main():
    return render_template('index2.html')

@app.route('/show')
def display():
    quote = get_quote()
    content = quote[0]
    author = quote[1]
    return render_template('index.html', content=content, author=author)

@app.route('/quotes', methods=['GET', 'POST'])
def quotes():
    if request.method == 'POST':
        category = request.form.get('category')
        session['tag'] = category
    return redirect(url_for('display'))


@app.route('/markdown')
def markdown():
    return render_template('temp.html')

if __name__ == '__main__':
    app.run(debug=True)
 