

with open("./Input/Names/invited_names.txt", "r") as file_inv:
    all_names = file_inv.readlines()


for name in all_names:
    stripped_name = name.strip()
    with open("./Input/Letters/starting_letter.txt", "r") as file_let:
        all_lines = file_let.readlines()
        all_lines[0] = all_lines[0].replace("[name]", stripped_name)

        # for x in range(len(all_lines)):
        #    print(all_lines[x])
        #    new_lines.append(all_lines[x].replace("[name]", name))

        with open(f"./Output/ReadyToSend/{name}.txt", "w") as file_ready:
            for line in all_lines:
                file_ready.write(line)
