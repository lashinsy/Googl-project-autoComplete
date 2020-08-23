import os

from complete import Complete
from data import Data, join_text


def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list


def start():
    print("Loading the files and preparing the system...")

    files_list = get_file_list("technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/faq")
    complete = Complete(Data(files_list))
    print("The system is ready.")

    input_ = join_text(input("\nEnter your text: "))

    while 1:
        text = " "

        while text[-1] != '#':
            match_sentences = complete.get_best_5_completions(input_)

            if len(match_sentences) != 0:
                for sentence in match_sentences:
                    print(f"{sentence.completed_sentence} ({files_list[sentence.source_text]} {sentence.offset})")
            else:
                print("there is no items")
            text = input(input_)
            input_ += join_text(text)

        input_ = join_text(input("\nEnter your text: "))


if __name__ == '__main__':
    start()
