# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        food = request.form['food']
        qty = request.form['qty']
        print(f"New Order:\nName: {name}\nFood: {food}\nQuantity: {qty}")
        return f"""
        <h2>Thank you, {name}!</h2>
        <p>You ordered {qty} {food}(s).</p>
        <a href="/">Back to Home</a>
        """
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
