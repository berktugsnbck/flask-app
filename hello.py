from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
    app.run1(host='0.0.0.0',port=5001)