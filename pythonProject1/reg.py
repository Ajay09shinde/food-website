from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['users']

client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['users']

@app.route
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        user_data = {
            'username': username,
            'password': password
        }
        collection.insert_one(user_data)
        return redirect(url_for('index'))
    else:
        return 'Please fill all the fields!'
