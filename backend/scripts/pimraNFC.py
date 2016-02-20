
import subprocess
from datetime import datetime

DUMP_PATH = "/home/rasmus/documents/dev/Pimra/backend/dumps/"

def nfc_poll(dump_name=datetime.now().strftime("%y-%m-%d-%H:%M")):
    """
    nfc-poll to collect UID
    """
    save_path = DUMP_PATH + "poll/"
    cmd = "nfc-poll > " + save_path + dump_name
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    output = proc.communicate()[0]
    return output


def nfc_dump(dump_name=datetime.now().strftime("%y-%m-%d-%H:%M")):
    """
    nfc-mfclassic to attempt a full card dump
    """
    save_path = DUMP_PATH + "full/"
    cmd = "nfc-mfclassic r a " + save_path + dump_name + ".mfd"
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    output = proc.communicate()[0]
    return "nfc-read dump saved as " + dump_name


def mfoc(dump_name=datetime.now().strftime("%y-%m-%d-%H:%M")):
    """
    mfoc to attemp cracking an encrypted card
    """
    save_path = DUMP_PATH + "mfoc/"
    cmd = "mfoc -P 500 -O " + save_path + dump_name
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    output = proc.communicate()[0]

    return "MFOC dump saved as " + dump_name
