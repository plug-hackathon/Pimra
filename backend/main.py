
from flask import Flask
from flask import request

from scripts.pimraNFC import nfc_poll, nfc_dump, mfoc_dump, nfc_write

app = Flask(__name__)

@app.route("/nfc/poll", methods=['GET'])
def poll():
    """
    Poll for UID
    """
    print(request.data)
    return nfc_poll()


@app.route("/nfc/read", methods=['GET'])
def nfc_read():
    """
    Dump card using nfc-mfclassic
    """
    print(request.data)
    return nfc_dump()


@app.route("/nfc/mfoc", methods=['GET'])
def mfoc():
    """
    Dump card using MFOC
    """
    return mfoc_dump()


@app.route("/nfc/write", methods=['GET'])
def poll():
    """
    Write to a blank card using nfc-mfclassic
    """
    return nfc_write()


if __name__ == "__main__":
    app.run()
