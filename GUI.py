from main import load_data
from tkinter import *

complete, files = load_data()


def clear_result():
    if result.get(1.0, END):
        result.delete(1.0, END)


def clear_input():
    text_input.delete(0, 'end')


def search_complete():
    clear_result()
    input_ = text_input.get()
    match_sentences = complete.get_best_5_completions(input_)
    res = ""

    if len(match_sentences):

        for index, sentence in enumerate(match_sentences):
            res += f"{index + 1}) {sentence.completed_sentence}\n  " \
                   f"source:{files[sentence.source_text]}  " \
                   f"line:{sentence.offset}\n\n"
    else:
        res += "there is no items"
    result.insert(INSERT, res)
    result.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("AutoComplete")

    label = Label(master, text="The system is ready, Enter your text: ", fg='red', font=14).pack(side=TOP)

    text_input = Entry(master, width=30, bd=5, font=12)
    text_input.pack()

    result = Text(master, width=250, font=9)
    result.pack()

    clear_button = Button(master, text="clear", command=clear_input, width=10, font=9, bg="lightgrey")
    clear_button.pack(side=LEFT)

    close_button = Button(master, text="close", command=master.quit, width=10, font=9, bg="lightgrey")
    close_button.pack(side=RIGHT)

    search_button = Button(master, text="search", command=search_complete, width=10, font=9, bg="lightgrey")
    search_button.pack(side=BOTTOM)

    mainloop()
