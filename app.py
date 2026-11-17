from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Math Adventure</title>
    </head>

    <body>
        <h1>Selamat Datang di Math Adventure!</h1>
        <p>Yuk, belajar mengenal angka bersama!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)