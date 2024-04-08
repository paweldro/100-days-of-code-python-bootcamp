import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

program_running = True
while program_running:
    user_input = input("Enter a word: ")
    if user_input.lower() == "exit":
        program_running = False
    else:
        result = [nato_dict[letter.upper()] for letter in user_input]
        print(result)
