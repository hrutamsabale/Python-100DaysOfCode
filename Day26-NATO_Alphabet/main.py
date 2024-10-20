import pandas

nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dict = {row.letter : row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}
name = input("Enter your name: ").upper()

name_phonetic = [nato_phonetic_alphabet_dict[letter] for letter in name if 1]

print(name_phonetic)