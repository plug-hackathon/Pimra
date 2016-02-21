
from flask import Flask
from flask import request
from utils.crossdomain import crossdomain

from scripts.pimraNFC import nfc_poll, nfc_dump, mfoc_dump, nfc_write

app = Flask(__name__)



@app.route("/nfc/poll", methods=['GET'])
@crossdomain(origin='*')
def poll():
    """
    Poll for UID
    """
    print(request.data)
    print(request.get_json())
    return nfc_poll()



@app.route("/nfc/read", methods=['GET', 'POST', 'OPTIONS'])
@crossdomain(origin='*')
def nfc_read():
    """
    Dump card using nfc-mfclassic
    """
    print(request.data)
    return nfc_dump()



@app.route("/nfc/mfoc", methods=['GET'])
@crossdomain(origin='*')
def mfoc():
    """
    Dump card using MFOC
    """
    return mfoc_dump()



@app.route("/nfc/write", methods=['GET'])
@crossdomain(origin='*')
def clone_card():
    """
    Write to a blank card using nfc-mfclassic
    """
    return nfc_write()


if __name__ == "__main__":
    app.run()
