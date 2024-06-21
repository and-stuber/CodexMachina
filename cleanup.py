import os
import re

def clean_word(word):
    # Remover sinais de pontuação e manter apenas palavras
    # print("Remover sinais de pontuação e manter apenas palavras")
    word = re.sub(r'[^\w\s]', '', word)
    return word

def is_valid_word(word):
    # Verificar se a palavra tem mais de 3 letras e não contém números
    # print("Verificar se a palavra tem mais de 3 letras e não contém números")
    if len(word) > 3 and not any(char.isdigit() for char in word):
        return True
    return False

def is_link(word):
    # Verificar se a palavra parece um link para website
    # print("Verificar se a palavra parece um link para website")
    if re.match(r'http[s]?://', word) or re.match(r'www\.', word):
        return True
    return False

def read_words_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as infile:
            print(f"Lendo {file_path}")
            lines = infile.readlines()
        words = []
        for line in lines:
            # Ignorar linhas que contenham números ou links
            if not any(char.isdigit() for char in line) and not is_link(line):
                for word in line.split():
                    cleaned_word = clean_word(word)
                    if is_valid_word(cleaned_word):
                        words.append(cleaned_word)
        return words
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
        return []

def read_txts_in_directory(directory_path):
    all_words = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            words = read_words_from_txt(file_path)
            all_words.extend(words)
            print("Ate agora lemos " + str(len(all_words)) + " palavras")
    return all_words

def remove_duplicates_and_save(words, output_file_path):
    try:
        seen = set()
        unique_words = []
        for word in words:
            if word not in seen:
                seen.add(word)
                unique_words.append(word)
        
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            print("Gravando...")
            print("Gravando " + str(len(unique_words)) + " palavras no arquivo")
            for word in unique_words:
                outfile.write(word + "\n")
        
        print(f"Palavras únicas salvas em {output_file_path}")
    except Exception as e:
        print(f"Erro ao escrever em {output_file_path}: {e}")

# Exemplos de uso
directory_path = './data/extracted/'
output_file_path = './data/dictio.txt'

# Ler todos os arquivos .txt no diretório e extrair palavras válidas
all_words = read_txts_in_directory(directory_path)
# Remover duplicatas e salvar palavras únicas no arquivo de saída
remove_duplicates_and_save(all_words, output_file_path)

