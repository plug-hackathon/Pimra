"""
This module executes nfc related shell cmds

Dump paths are provided via django, and names if not
provided are default to datetime.now()
"""

import subprocess
from datetime import datetime

DEFAULT_NAME = datetime.now().strftime("%y-%m-%d-%H:%M")


def nfc_poll(dump_path, dump_name=DEFAULT_NAME):
    """
    nfc-poll to collect UID
    """
    print('Running nfc-poll...')
    save_path = dump_path + dump_name + ".mfd"
    cmd = "nfc-poll > " + save_path

    print('Saving dump to: ' + save_path)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()

    print("Done...")
    return "nfc-poll saved to: " + save_path


def nfc_dump(dump_path, dump_name=DEFAULT_NAME):
    """
    nfc-mfclassic to attempt a full card dump
    """
    print('Running nfc-mfclassic...')
    save_path = dump_path + dump_name + ".mfd"
    cmd = "nfc-mfclassic r a " + save_path
    print('Saving dump to: ' + save_path)

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()
    print(output)

    print('Done....')
    return "nfc-read dump saved to: " + save_path


def mfoc_dump(dump_path, dump_name=DEFAULT_NAME):
    """ 
    mfoc to attemp cracking & dumping a card 
    """
    print('Running mfoc...')
    save_path = dump_path + dump_name + ".mfd"
    cmd = "mfoc -P 500 -O " + save_path
    print('Saving dump to: ' + save_path)

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = proc.communicate()

    print('Done...')
    return "MFOC dump saved to: " + save_path

def nfc_write(dump_path):
    """
    Write dump file to unlocked card
    """
    print('Running nfc-mfclassic UNLOCKED WRITE...')
    cmd = "nfc-mfclassic W a " + dump_path
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)    

    return "Cloned " + original_dump
