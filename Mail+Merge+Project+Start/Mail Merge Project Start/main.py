# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:/Users/User/Documents/Replit Python projektek/Mail+Merge+Project+Start/Mail"
          " Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


edited_texts = []

for name in names:
    with open("C:/Users/User/Documents/Replit Python projektek/Mail+Merge+Project+Start/"
              "Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as old_letter:
        text = old_letter.read()
        edited_text = text.replace("[name]", name.strip())
        edited_texts.append(edited_text)

length = len(edited_texts)
name_index = 0

for name in names:
    name = name.strip()
    new_file_name = ("C:/Users/User/Documents/Replit Python projektek/Mail+Merge+Project+Start/"
                     "Mail Merge Project Start/Output/ReadyToSend/letter_for_") + name + ".txt"
    with open(new_file_name, mode="w") as new_letter:
        new_letter.write(edited_texts[name_index])
    name_index += 1
