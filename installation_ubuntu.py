import os
from pathlib import Path

HOME_DIR = str(Path.home())
bash_location = os.path.join(HOME_DIR, '.bashrc')

current_dir = os.path.dirname(os.path.abspath(__file__))
runable_python = os.path.join(current_dir + "/run.py")

os.system("echo Starting installation")
os.system("sudo apt install krita")

os.system("sudo apt install virtualenv")
os.system("virtualenv venv -p python3")
os.system("source venv/bin/activate")
os.system("pip install -r requirements.txt")
os.system("deactivate")

with open(bash_location, "a") as myfile:
    myfile.write("\n\nalias notes='source " + current_dir + "/venv/bin/activate && python3 " + runable_python + "'")
    print("alias added")
    print("Use 'notes' to run the program")

os.system("source ~/.bashrc")
print("Open a new terminal to start using the program")