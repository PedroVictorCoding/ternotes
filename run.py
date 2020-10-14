import os, sys
import shutil
import json
import re

args = sys.argv
current_dir = os.path.dirname(os.path.abspath(__file__))
base_file = current_dir + "/notes/base.kra"

print("Args: " + str(args))

if args[1] == "--help" or args[1] == "-h":
    print("Create notes: notes create [title*] [category*] [YYYY*] [mm*] [dd*] [tag1] [tag2] [tagn]")
    print("Find notes: notes find [category:(category)] or [title:(title) or tag:(tag)] or []")
    print("Open notes: notes open [id]")
    print("Attributes with * are required")

elif args[1] == "open":
    note_logs = open('noteLogs.json') 
    data = json.load(note_logs)
    j = 0
    while j < len(data["notes"]):
        id_entered = json.dumps(data["notes"][j]["id"]).strip('"')
        if id_entered == args[2]:
            print("Opening", json.dumps(data["notes"][j]).strip('"'))
            os.system("krita --nosplash " + json.dumps(data["notes"][j]["location"]).strip('"'))
        j+=1

elif args[1] == "find":
    note_logs = open('noteLogs.json') 
    data = json.load(note_logs)
    print(len(data["notes"]))
    i = 0
    search_terms = len(args) - 1

    if search_terms < 2:
        j = 0
        while j < len(data["notes"]):
            print("Found", json.dumps(data["notes"][j]).strip('"'))
            #print("JSON data", json.dumps(data["notes"][i]["category"]))
            j += 1 

    else:
        while i <= search_terms:
            if "category:" in args[i]:
                entered_search = args[i]
                search = re.sub('category:', '', entered_search)
                print("Searched category:", search)
                print("All notes under the category:", search)
                j = 1
                while j < len(data["notes"]):
                    categories = json.dumps(data["notes"][j])
                    if '"category": "' + search + '"' in categories:
                        print("Found", json.dumps(data["notes"][j]).strip('"'))
                    else:
                        pass
                    #print("JSON data", json.dumps(data["notes"][i]["category"]))
                    j += 1 

            elif "title:" in args[i]:
                entered_search = args[i]
                search = re.sub('title:', '', entered_search)
                print("Searched title:", search)
                print("All notes under the title:", search)
                j = 1
                while j < len(data["notes"]):
                    title = json.dumps(data["notes"][j])
                    if '"title": "' + search + '"' in title:
                        print("Found", json.dumps(data["notes"][j]).strip('"'))
                    else:
                        pass
                    #print("JSON data", json.dumps(data["notes"][i]["category"]))
                    j += 1 

            i+=1


    '''while i < len(data["notes"]):
        categories = json.dumps(data["notes"][i]["category"]).strip('"')
        if categories == args[2]:
            print("Found", categories)
        else:
            pass
        #print("JSON data", json.dumps(data["notes"][i]["category"]))
        i += 1'''


elif args[1] == "create":
    note_logs = open('noteLogs.json') 
    data = json.load(note_logs)
    new_note_path = current_dir + "/notes/" + str(args[3]) + "/" + str(args[4]) + "/" + str(args[5]) + "/" + str(args[6]) + "/"
    if not os.path.exists(new_note_path):
        os.makedirs(new_note_path)
    os.system("krita ~/ternotes/notes/base.kra --export --export-filename ~/ternotes/notes/" + args[3] + "/" + args[4] + "/" + args[5] + "/" + args[6] + "/" + args[2] + ".kra")
    os.system("krita --nosplash  ~/ternotes/notes/" + args[3] + "/" + args[4] + "/" + args[5] + "/" + args[6] + "/" + args[2] + ".kra")

    note_log_location = current_dir + "/noteLogs.json"

    with open(note_log_location, "r+", encoding = "utf-8") as note_log_file:
        note_log_file.seek(0, os.SEEK_END)
        pos = note_log_file.tell() - 1
        while pos > 0 and note_log_file.read(1) != "\n":
            pos -= 1
            note_log_file.seek(pos, os.SEEK_SET)
        if pos > 0:
            note_log_file.seek(pos, os.SEEK_SET)
            note_log_file.truncate()

    with open(note_log_location, "a") as myfile:
        myfile.write(',\n\t\t{"id": "' + str(len(data["notes"]) - 1) + '", "category":"' + args[3] + '", "title":"' + args[2] + '", "location":"' + '~/ternotes/notes/' + args[3] + '/' + args[4] + '/' + args[5] + '/' + args[6] + '/' + args[2] + '.kra", "date":"' + args[4] + "/" + args[5] + "/" + args[6] + '"}\n]}')



## Exiting
os.system("\n\n\n\n\n")