import subprocess
from subprocess import check_output

output = subprocess.Popen('python3 valid_number.py < input.txt > out.txt', stdout=subprocess.PIPE, shell = True)

difference = subprocess.run(['diff', 'ans.txt', 'out.txt'], capture_output = True)

if difference.returncode == 0:
    print('well done')
else:
    print('check you code again')