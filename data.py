import string


def join_text(text):
    return ' '.join((''.join(i for i in text if i in string.ascii_letters + ' ')).split())


class Data:

    def __init__(self, location):
        self.sentences = list()
        self.sub_sentences = dict()
        self.data = list()
        self.init_data(location)

    """
    get file location and return list of strings,
    each string is a line in the file
    """

    def read_file_as_list(self, file):
        with open(file, encoding="utf8") as f:
            sentences = f.readlines()
        f.close()
        return [sentence.strip() for sentence in sentences]

    """
    get list of name files 
    return a list with all the sentences from the file
    and a dictionary with all the substring of the list sentences as keys 
    """

    def init_data(self, location):
        index_data = 0

        for index_file, file in enumerate(location):
            self.sentences = self.read_file_as_list(file)
            # go over every string and add to the dictionary all its substring as keys
            for offset, sentence in enumerate(self.sentences):
                curr_sentence = join_text(sentence)
                length = len(curr_sentence)
                curr_sentence = [curr_sentence[i: j + 1] for i in range(length) for j in range(i, length)]

                if length:
                    for word in curr_sentence:
                        curr_word = word.strip()
                        self.sub_sentences.update({curr_word: {index_data}}) \
                            if curr_word not in self.sub_sentences.keys() \
                            else self.sub_sentences[curr_word].add(index_data)

                    self.data.append([sentence, index_file, offset])
                    index_data += 1

        return self
