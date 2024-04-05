

with open("./Input/Names/invited_names.txt", "r") as file:
    all_names = file.readlines()


for name in all_names:
    stripped_name = name.strip()
    with open("./Input/Letters/starting_letter.txt", "r") as file:
        all_lines = file.readlines()
        all_lines[0] = all_lines[0].replace("[name]", stripped_name)

        # for x in range(len(all_lines)):
        #    print(all_lines[x])
        #    new_lines.append(all_lines[x].replace("[name]", name))

        with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
            for line in all_lines:
                file.write(line)

