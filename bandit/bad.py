import os
import subprocess

password = "hunter2"  # hardcoded password (Bandit will catch this)

def dangerous_eval(user_input):
    return eval(user_input)  # Bandit flags this as a major issue

def insecure_shell():
    os.system("ls -l")  # Bandit flags this as unsafe
    subprocess.call("rm -rf /tmp/somedir", shell=True)  # shell=True is dangerous

dangerous_eval("print('hello')")
insecure_shell()
