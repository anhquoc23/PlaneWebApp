from flask import render_template
from planeweb import app

@app.route('/')
def home():
    values = []
    name = 'NGUYỄN ANH QUỐC'
    for i in range(100):
        values.append(i * 10 + 5)
    return render_template('index.html', data=values, name=name)

if __name__ == '__main__':
    app.run(debug=True)