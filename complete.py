import string
from auto_complete_data import AutoCompleteData


class Complete:

    def __init__(self, data, len_result=5):
        self.data = data
        self.LEN_RESULT = len_result
        self.__complete_sentences = []

    def get_reduce_points(self, i):
        return - 10 + 2 * i if i < 4 else -2

    def is_exist(self, sentence):
        for s in self.__complete_sentences:
            if s.completed_sentence == sentence:
                return True
        return False

    def add_complete_sentence(self, sentence, score):
        if sentence in self.data.sub_sentences.keys():

            for id_ in self.data.sub_sentences[sentence]:
                if not self.is_exist(self.data.data[id_][0]):
                    self.__complete_sentences.append(AutoCompleteData(self.data.data[id_][0], self.data.data[id_][1], self.data.data[id_][2], score))
                    if len(self.__complete_sentences) == self.LEN_RESULT:
                        return True

        return False

    def replace_letter(self, input_, index, score):
        for letter in string.ascii_letters:
            if self.add_complete_sentence(input_[:index] + letter + input_[index + 1:], score):
                return True

        return False

    def add_letter(self, input_, index, score):
        for letter in string.ascii_letters:
            if self.add_complete_sentence(input_[:index] + letter + input_[index:], score):
                return True
        return False

    def change_input(self, input_):
        len_ = len(input_)
        basic_score = 2 * (len_ - 1)

        ''' replace all the letters in place > 4'''
        score = basic_score + self.get_reduce_points(4) // 2
        for i in range(len_ - 1, 3, -1):
            if self.replace_letter(input_, i, score):
                return

        '''replace character in 4 place (the score is deferent)'''
        if self.replace_letter(input_, 3, basic_score + self.get_reduce_points(3) // 2):
            return

        '''delete or add the letters in place > 4'''
        score = basic_score + self.get_reduce_points(4)
        for i in range(len_ - 1, 3, -1):
            if self.add_letter(input_, i, score):
                return
            if self.add_complete_sentence(input_[:i] + input_[i + 1:], score):
                return

        '''replace the letter in the 2 or 3 places'''
        if self.replace_letter(input_, 2, basic_score + self.get_reduce_points(2) // 2) or \
                self.replace_letter(input_, 1, basic_score + self.get_reduce_points(1) // 2):
            return

        '''add or delete 4 letter'''
        if self.add_letter(input_, 3, score):
            return
        if self.add_complete_sentence(input_[:3] + input_[3 + 1:], basic_score + self.get_reduce_points(3)):
            return

        '''replace the first letter'''
        if self.replace_letter(input_, 0, basic_score + self.get_reduce_points(0) // 2):
            return

        '''delete or add the 3 first letters'''
        for i in range(2, -1, -1):
            score = basic_score + self.get_reduce_points(i)
            if self.add_letter(input_, i, score):
                return
            if self.add_complete_sentence(input_[:i] + input_[i + 1:], score):
                return

    def get_best_5_completions(self, input_):
        self.__complete_sentences.clear()

        # check if the sentence is complete in the data
        if self.add_complete_sentence(input_, 2 * len(input_)):
            return self.__complete_sentences

        # else try to change the input
        self.change_input(input_)
        return self.__complete_sentences

