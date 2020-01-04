import os
import sys


def get_cmd(module, console=False):
    console_arg = '--console' if console else '--window'
    trained_arg = '--trained' if trained else '--train'
    return 'python3 -m src.' + str(module) + '.main ' + console_arg + ' ' + trained_arg


if __name__ == "__main__":
    console = '--console' in sys.argv
    trained = '--trained' in sys.argv
    if '--cars' in sys.argv:
        os.system(get_cmd('cars', console))
    elif '--submarines' in sys.argv:
        os.system(get_cmd('submarines', console))
