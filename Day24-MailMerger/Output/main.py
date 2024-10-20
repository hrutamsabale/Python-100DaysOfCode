with open("../Input/Letters/starting_letter.txt") as base_letter:
    letter_format = base_letter.read()

with open("../Input/Names/invited_names.txt") as invited_guests:
    guest_list = invited_guests.readlines()

for name in guest_list:
    new_letter = letter_format.replace("[name]", name.strip())
    with open(f"./ReadyToSendInDocx/letter_for_{name.strip()}.docx", mode="w") as letter:
        letter.write(new_letter)


