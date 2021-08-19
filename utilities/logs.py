from utilities.chia import check_balance
from datetime import date
import logging
import re
import os


''' Program Functions. Do not change. '''
def old_balance(path, current_balance):
    log_path = path + "\\utilities\\balance.log"

    # Create Log file if it Doesn't Exist
    if not os.path.exists(log_path):
        update_log(log_path, current_balance)

    with open(log_path,'r') as reader:
        line = reader.read()

    old_balance = re.findall('Chia Balance: (\d*\.\d*)', line)
    return old_balance[0]


def compare_chia(new_balance, old_balance):
    if float(new_balance) > float(old_balance):
         return True
    return False


def update_log(path, chia_balance):
    logging.basicConfig(filename=path + "\\utilities\\balance.log", filemode='w', format='%(message)s')
    logger=logging.getLogger()

    logger.setLevel(logging.INFO)
    logger.info('Chia Balance: ' + chia_balance)
