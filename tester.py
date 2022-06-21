from genericpath import exists
import subprocess
import sys
import os

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

DIR = "test/"
test = ""
test_cases = os.listdir(DIR)

filtered = []

for test in test_cases:
    if test.endswith('.toma'):
        filtered.append(test)

def check():
    for file in filtered:
        result = subprocess.run(["python3", "inter.py", DIR + file], stdout = subprocess.PIPE)
        std = (result.stdout).decode('utf-8')

        origin = DIR + file.rsplit('.', 1)[0] + '.txt'
        if exists(origin):
            with open(origin, 'r') as ori:
                data = ori.read()

            data = data.split()
            std = std.split()
            
            if data == std:
                print(file + ": " + colors.OKGREEN + "OK" + colors.ENDC)
        else:
            assert False, "the file does not exists"

def record():
    for file in filtered:
        result = subprocess.run(["python3", "inter.py", DIR + file], stdout = subprocess.PIPE)
        std = (result.stdout).decode('utf-8').replace("\r", "")

        destination = DIR + file.rsplit('.', 1)[0] + '.txt'
        with open(destination, 'w+') as dst:
            dst.write(std)

if __name__ == '__main__':

    argv = sys.argv
    if len(argv) != 2:
        assert False, "A flag (-record) or (-check) need to be provided"

    if argv[1] == '-record':
        record()
    elif argv[1] == '-check':
        check()
    else:
        assert False, "wrong flag"