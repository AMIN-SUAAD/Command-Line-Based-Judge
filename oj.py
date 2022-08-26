import subprocess
from subprocess import TimeoutExpired
import sys

if __name__ == '__main__':

    output = subprocess.Popen('python3 valid_number.py < input.txt > out.txt', shell=True, stderr=subprocess.PIPE)

    try:
        outs, errs = output.communicate(timeout=2)
    except TimeoutExpired:
        output.kill()
        outs, errs = output.communicate()
        print('Timeout expired')
        sys.exit()

    if len(errs) == 0:

        difference = subprocess.run(['diff', 'ans.txt', 'out.txt'], capture_output=True)

        if difference.returncode == 0:
            print('well done')
        else:
            print('check you code again')
    else:
        print(errs)
