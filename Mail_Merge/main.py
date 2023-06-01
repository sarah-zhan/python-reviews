# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        with open("./Input/Letters/starting_letter.txt") as letter:
            content = letter.read()
            # Replace the [name] placeholder with the actual name.
            # strip out the return line
            new_content = content.replace("[name]", name.strip())
            # Save the letters in the folder "ReadyToSend".
            with open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w+") as new:
                new.write(new_content)
