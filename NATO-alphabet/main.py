import pandas
# read csv file
nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# Create a dictionary
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
answer = input("Tell me a word: ")
answer_list = list(answer.upper())

answer_alphabet = [phonetic_alphabet_dict[letter] for letter in answer_list]
print(answer_alphabet)
