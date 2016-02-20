
from flask import Flask
from flask import request

from scripts.pimraNFC import nfc_poll, nfc_dump

app = Flask(__name__)

@app.route("/nfc/read", methods=['GET'])
def nfc_read():
    """
    Dump/read data from nfc
    """
    print(request.data)
    return nfc_dump()


@app.route("/nfc/poll", methods=['GET'])
def poll():
    """
    Poll for UID
    """
    print(request.data)
    return nfc_poll()

if __name__ == "__main__":
    app.run()
