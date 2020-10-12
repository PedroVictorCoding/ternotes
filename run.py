import os, sys
import shutil

args = sys.argv
current_dir = os.path.dirname(os.path.abspath(__file__))
base_file = current_dir + "/notes/base.kra"
new_note_path = current_dir + "/notes/" + str(args[2]) + "/" + str(args[3]) + "/" + str(args[4]) + "/" + str(args[5]) + "/"

print(base_file)
print(new_note_path)


print("Args: " + str(args))

if args[1] == "--help" or args[1] == "-h":
    print("Use: notes [title] [category] [YYYY] [mm] [dd] ")
else:

    if not os.path.exists(new_note_path):
        os.makedirs(new_note_path)
    os.system("krita ~/ternotes/notes/base.kra --export --export-filename ~/ternotes/notes/" + args[2] + "/" + args[3] + "/" + args[4] + "/" + args[5] + "/" + args[1] + ".kra")
    os.system("krita --nosplash --canvasonly  ~/ternotes/notes/" + args[2] + "/" + args[3] + "/" + args[4] + "/" + args[5] + "/" + args[1] + ".kra")

## Run Krita here with settings 



## Exiting
os.system("\n\n\n\n\n")
os.system("clear")
os.system("exit")