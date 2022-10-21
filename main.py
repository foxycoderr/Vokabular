import json

print("Welcome to Vokabular.")

print("For documentation, run 'help'.")

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def sets():
    with open("sets.json", "r") as f:
        data = json.load(f)

    for key in data:
        print(key)


def new():
    print("Enter set words in format term:definition (to exit type exit)")

    dict_words = {}

    while True:
        word = input()
        if ":" in word:
            index = word.index(":")
            term = word[0:index]
            leng = len(word)
            defin = word[index + 1:leng]

            if term in dict_words:
                print("Word already in set! Updating meaning.")
                dict_words[term] = defin
            else:
                dict_words[term] = defin

        elif word == "exit":
            print("Finishing set creation...")
            name = input("Set created. Enter name: ")
            with open("sets.json", "r") as f:
                data = json.load(f)

            while True:
                if name in data:
                    name = input("Invalid set name. Enter name: ")
                else:
                    break

            data[name] = dict_words

            with open("sets.json", "w") as f:
                json.dump(data, f)

            print(f"Set recorded with name {name}.")

            break

        else:
            print("Wrong input...")


def delete(name):
    with open("sets.json", "r") as f:
        data = json.load(f)

    if name in data:
        confirmation = input("Are you sure you want to delete {}? Y/n ".format(name))

        if confirmation == 'Y':
            data.pop(name)
            with open("sets.json", "w") as f:
                json.dump(data, f)

            print("Set deleted.")

        else:
            print("Deletion cancelled.")

    else:
        print("Set not found!")


def recall(name):
    with open("sets.json", "r") as f:
        data = json.load(f)

    if name in data:
        for i in data[name]:
            print(i, ":", data[name][i])


    else:
        print("Set not found.")


def edit(name):
    with open("sets.json", "r") as f:
        data = json.load(f)

    if name in data:
        dict_words = data[name]
        index = 0
        for i in dict_words:
            print(index, "-", i, ":", dict_words[i])
            index += 1

        line = input("Enter line you would like to change: ")
        if int(line) <= index:
            word = input("Enter new term:definition: ")
            if ":" in word:
                i1 = 0
                for i in dict_words:
                    if i1 == int(line):
                        kw = i
                    i1 += 1

                data[name].pop(kw)
                index1 = word.index(":")
                term = word[0:index1]
                leng = len(word)
                defin = word[index1 + 1:leng]
                data[name][term] = defin

                with open("sets.json", "w") as f:
                    json.dump(data, f)

                print("Value updated.")
            else:
                print("Wrong input.")

        else:
            print("Line out of range.")

    else:
        print("Set not found.")


# learn is still broken.
def learn(name, learn_type):
    with open("sets.json", "r") as f:
        data = json.load(f)

    if name in data:
        words = list(data[name])
        if learn_type == "def":
            def learning():
                for i in data[name]:
                    if i in list(words):
                        ans = input("What does {} mean? ".format(i))
                        if ans == data[name][i]:
                            words.pop(words.index(i))
                            print("Correct!")
                        else:
                            print(f"Wrong! It was {data[name][i]}.")
                            print("")

            while True:
                if words:
                    learning()
                else:
                    break

            print("Well done! Set studied.")

def help():
    print(color.BOLD + "Vokabular"  + color.END + " - vocabulary learning tool.")

    print()

    print(color.BOLD + "Usage" + color.END)
    print("Vokabular has all the functionality to serve as a script which helps you learn words of, say, a foreign \n language, or any other pairs of data. ")

    print()

    print(color.BOLD + "Commands" + color.END)
    print("sets - returns the list of your sets stored in sets.json.")
    print("new - initiates the procedure of creating a new set.")
    print("delete [set_name] - delete a set.")
    print("recall [set_name] - recall the terms of a set.")
    print("edit [set_name] - edit a set.")
    print("learn [set_name] [mode]- learn the set. Currently, only def (definition) mode is supported.")

    print()
    print(color.BOLD + "Credits: "  + color.END + "FoxyCoder")

def command_master(command):
    command = command.split()
    keyword = command[0]

    if keyword == "sets":
        sets()

    elif keyword == "new":
        new()

    elif keyword == "del":
        try:
            name = command[1]
            delete(name)
        except:
            print("Missing argument (set name).")

    elif keyword == "recall":
        try:
            name = command[1]
            recall(name)
        except:
            print("Missing argument (set name).")

    elif keyword == "edit":
        try:
            name = command[1]
            edit(name)
        except:
            print("Missing argument (set name).")

    # learn not an option for now.
    elif keyword == "learn":
        try:
            name = command[1]
            type = command[2]
            learn(name, type)
        except:
            print("Missing argument (set name).")

    elif keyword == "help":
        help()

    else:
        print("Command mot found! Use help to get the documentation.")

def main():
    while True:
        print("")
        command = input(">>> ")

        command_master(command)


if __name__ == "__main__":
    main()







