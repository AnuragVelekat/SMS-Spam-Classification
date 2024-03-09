from flask import Flask, render_template, request
from models import get_model_output

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_text():
    if request.method == 'POST':
        user_input = request.form['user_input']
        output = get_model_output(user_input)  
        return render_template('index.html', output=f"The message '{user_input}' is classified as {output}")  
    else:
        return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True, port=8080)