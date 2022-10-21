import json

print("Welcome to Vokabular.")

print("For documentation, run 'help'.")


while True:
    print("")
    command = input(">>> ")

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
            words = data[name]
            if learn_type == "def":
                def learning():
                    for i in data[name]:
                        if i in list(words):
                            ans = input("What does {} mean? ".format(i))
                            if ans == data[name][i]:
                                words.pop(i)
                                print("Correct!")
                            else:
                                print(f"Wrong! It was {data[name][i]}.")
                                print("")

                while True:
                    if data[name]:
                        learning()
                    else:
                        break

                print("Well done! Set studied.")





    def command_master(command):
        command = command.split()
        keyword = command[0]

        if keyword == "sets":
            sets()

        if keyword == "new":
            new()

        if keyword == "del":
            try:
                name = command[1]
                delete(name)
            except:
                print("Missing argument (set name).")

        if keyword == "recall":
            try:
                name = command[1]
                recall(name)
            except:
                print("Missing argument (set name).")

        if keyword == "edit":
            try:
                name = command[1]
                edit(name)
            except:
                print("Missing argument (set name).")

        # learn not an option for now.
        """if keyword == "learn":
            #try:
            name = command[1]
            type = command[2]
            learn(name, type)
            #except:
                #print("Missing argument (set name).")"""


    command_master(command)







