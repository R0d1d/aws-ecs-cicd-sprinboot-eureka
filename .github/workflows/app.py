from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "I'm learning CI/CD!"

if __name__ == '__main__':
    app.run()