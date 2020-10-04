import os
import subprocess
import time
import io
def main():
    print("test")
    cmd = 'python libgen/ -s "recursion"'
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)s
    for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):  # or another encoding
        print("t: ",str(line))
    time.sleep(10)
    out = p.communicate(input=b'22')[0]
if __name__ == "__main__":
    main()