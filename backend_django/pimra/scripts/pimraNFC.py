
import subprocess
from datetime import datetime

DUMP_PATH = "/home/root/Pimra/backend/dumps/"
DEFAULT_NAME = datetime.now().strftime("%y-%m-%d-%H:%M")

def nfc_poll(dump_name=DEFAULT_NAME):
    """
    nfc-poll to collect UID
    """
    save_path = DUMP_PATH + "poll/"
    cmd = "nfc-poll > " + save_path + dump_name

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()[0]
    return "nfc-poll saved as " + dump_name


def nfc_dump(dump_name=DEFAULT_NAME):
    """
    nfc-mfclassic to attempt a full card dump
    """
    save_path = DUMP_PATH + "full/"
    cmd = "nfc-mfclassic r a " + save_path + dump_name + ".mfd"

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()[0]
    return "nfc-read dump saved as " + dump_name


def mfoc_dump(dump_name=DEFAULT_NAME):
    """
    mfoc to attemp cracking & dumping a card
    """
    save_path = DUMP_PATH + "mfoc/"
    cmd = "mfoc -P 500 -O " + save_path + dump_name

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()[0]
    return "MFOC dump saved as " + dump_name

def nfc_write(original_dump):
    """
    Write dump file to unlocked card
    """
    cmd = "nfc-mfclassic W a " + DUMP_PATH + original_dump
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)    
    return "Cloned " + original_dump