
import subprocess
from datetime import datetime

DUMP_PATH = "/root/nfcstuff/Pimra/backend_django/dumps/"
DEFAULT_NAME = datetime.now().strftime("%y-%m-%d-%H:%M")


def nfc_poll(dump_name=DEFAULT_NAME):
    """
    nfc-poll to collect UID
    """
    save_path = DUMP_PATH + "poll/" + dump_name + ".mfd"
    cmd = "nfc-poll > " + save_path

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()
    return "nfc-poll saved to: " + save_path


def nfc_dump(dump_name=DEFAULT_NAME):
    """
    nfc-mfclassic to attempt a full card dump
    """
    print('Running nfc-mfclassic...')
    save_path = DUMP_PATH + "full/" + dump_name + ".mfd"
    print('Saving dump to: '+save_path)
    cmd = "nfc-mfclassic r a " + save_path

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    output = proc.communicate()
    print(output)
    print('Done....')
    return "nfc-read dump saved to: " + save_path


def mfoc_dump(dump_name=DEFAULT_NAME):
    """
    mfoc to attemp cracking & dumping a card
    """
    save_path = DUMP_PATH + "mfoc/" + dump_name + ".mfd"
    cmd = "mfoc -P 500 -O " + save_path

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()
    return "MFOC dump saved to: " + save_path

def nfc_write(original_dump):
    """
    Write dump file to unlocked card
    """
    cmd = "nfc-mfclassic W a " + DUMP_PATH + "full/" + original_dump
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)    
    return "Cloned " + original_dump
