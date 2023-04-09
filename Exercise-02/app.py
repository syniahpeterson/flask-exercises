#Syniah Peterson
#I used https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=844s to set up and complete the exercise.
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form.get('num')
        return redirect(url_for('calculate', num=num))
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    num = request.args.get('num')
    try:
        if num.isdigit() == True:
            user_num = int(num)
            if user_num % 2 == 0:
                return render_template("calculate.html", even_or_odd= str(user_num) + " is even.")
            elif user_num % 2 == 1:
                return render_template("calculate.html", even_or_odd= str(user_num) + " is odd.")
            elif user_num == "":
                return render_template("calculate.html", even_or_odd= "No number provided!")
            else:
                return render_template("calculate.html", even_or_odd= str(user_num) + " is not an integer!")
        elif num == "":
            return render_template("calculate.html", even_or_odd= "No number provided!")
        else:
            return render_template("calculate.html", even_or_odd= str(num) + " is not an integer!")
    except:
        return "There was an issue determining whether your number is even or odd."
    
if __name__ == "__main__":
    app.run(debug=True)