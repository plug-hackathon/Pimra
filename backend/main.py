
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/nfc/read", methods=['GET'])
def nfc_read():
    """
    Dump/read data from nfc
    """
    print(request.data)
    return "Hello World!"


if __name__ == "__main__":
    app.run()
