import re
import psutil
import os
from subprocess import check_output
from datetime import date


''' Program Functions. Do not change. '''
def process_running(processName):
    processes = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName in proc.name():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def check_balance(directory):
    command = r".\chia.exe wallet show"

    os.chdir(directory)
    wallet = check_output(command)
    try:
        chia = re.findall(r'\-Total Balance: (\d*\.\d*) xch', str(wallet))
        return chia[0]
    except:
        return 0


def check_farm(directory):
    command = r".\chia.exe farm summary"

    os.chdir(directory)
    try:
        farm = check_output(command)
    except:
        farm = 0

    plot_count = re.findall(r'Plot count for all harvesters: (\d*)', str(farm))
    total_size = re.findall(r'Total size of plots: (\d*\.\d*) \w*', str(farm))

    return [plot_count[0], total_size[0]]


def get_running_plots():
    running_plots = 0

    for process in psutil.process_iter():
        if process.name() == 'chia.exe':
            running_plots += 1

    return running_plots
