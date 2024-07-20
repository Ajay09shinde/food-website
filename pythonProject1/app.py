from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Establish MongoDB connection
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['information']
    collection = db['inform']
except Exception as e:
    print("Error:", e)


@app.route('/')
def home():
    return render_template('signup.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    user_data = {
        'username': username,
        'password': password,
        'email': email
    }
    collection.insert_one(user_data)

    return redirect(url_for('success'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']

    user = collection.find_one({'username': username, 'password': password})

    if user:
        return redirect(url_for('success'))

    return render_template('login.html', error=True)


@app.route('/success')
def success():
    return render_template('home.html')


@app.route('/aboutentry', methods=['POST'])
def aboutentry():
    username = request.form['username']
    password = request.form['password']
    mob = request.form['mob']
    state = request.form['state']
    email = request.form['email']
    radio = request.form['radio']

    user_data = {
        'username': username,
        'password': password,
        'email': email,
        'state': state,
        'mob': mob,
        'radio': radio
    }
    collection.insert_one(user_data)

    return redirect(url_for('success'))


@app.route('/bill_form')
def bill_form():
    return render_template('bill_form.html')


@app.route('/generate_bill', methods=['POST'])
def generate_bill():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    item = request.form['item']
    quantity = request.form['quantity']
    price = request.form['price']
    total = int(quantity) * int(price)
    return f'''
    <h2>Bill Details</h2>
    <p>Name: {name}</p>
    <p>Email: {email}</p>
    <p>Address: {address}</p>
    <p>Item: {item}</p>
    <p>Quantity: {quantity}</p>
    <p>Price: {price}</p>
    <p>Total: {total}</p>
    '''


if __name__ == '__main__':
    app.run(debug=True)
