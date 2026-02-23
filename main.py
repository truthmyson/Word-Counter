from count_words import count_words
from pathlib import Path
import os



if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), 'E_M_Goldratt_-_The_Goal.pdf')
    print(file_path)
    number = count_words(file_path)
    print(number)