import os

def read_words_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    return words

def read_txts_in_directory(directory_path):
    all_words = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            words = read_words_from_txt(file_path)
            all_words.extend(words)
    return all_words

def save_words_to_file(words, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + "\n")

# Specify the directory containing the .txt files
directory_path = './data/'
output_file_path = './data/words_list.txt'

# Read all .txt files in the directory and extract words
all_words = read_txts_in_directory(directory_path)

# Save all words to a single file
save_words_to_file(all_words, output_file_path)

print("Words extraction and saving complete!")
