from flask import Flask, render_template, request, redirect, url_for
from bd import *
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def start_page():
    type = request.args.get('type')
    if type in progs:
        return redirect(url_for('progs_page', type=type))
    return render_template('index.html', progs=progs)

@app.route('/<type>')
def progs_page(type):
    page = progs[type]
    choices = request.args
    print(list(choices))
    if not choices:
        return render_template('items.html', type=type, page=page)
    new_page = []
    for article in page:
        if str(article['id']) in choices:
            new_page.append(article)
    max_result = max(new_page, key=lambda x: x['result'])['name']
    return render_template('result.html',type=type, page=new_page, max_result=max_result)


if __name__ == '__main__':
    app.run(debug = True)