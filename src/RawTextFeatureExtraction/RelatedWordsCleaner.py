from nltk.corpus import wordnet as wn

class RelatedWordsCleaner(object):
    def __init__(self, configuration_map):
        self.__configuration_map = configuration_map

    def get_cleaned_tokens(self, tokens):
        final_tokens = []
        for word1 in tokens:
            word1_synsets = wn.synsets(word1)
            if self.__synset_is_empty(word1_synsets):
                continue
            word1_synset = word1_synsets[0]
            final_word = self.__check_word_with_any_other_word(word1, word1_synset, tokens)
            final_tokens.append(final_word)
        return final_tokens

    def __synset_is_empty(self, synset):
        return len(synset) == 0

    def __words_are_the_same(self, word1, word2):
        return word1 == word2


    def __check_word_with_any_other_word(self, first_word, first_word_synset, tokens):
        final_word = first_word
        smallest_depth = first_word_synset.min_depth()
        for word2 in tokens:
                if self.__words_are_the_same(first_word, word2):
                    continue
                word2__synsets = wn.synsets(word2)
                if self.__synset_is_empty(word2__synsets):
                    continue
                word2__synset = word2__synsets[0]
                word2_depth = word2__synset.min_depth()

                similarity_level = first_word_synset.path_similarity(word2__synset)
                shortest_path_distance = first_word_synset.shortest_path_distance(word2__synset)
                if similarity_level == None or shortest_path_distance == None:
                    continue;

                min_similarity_level = self.__configuration_map['related_words_minimum_similarity_level']
                max_distance = self.__configuration_map['related_words_maximum_path_distance']
                if similarity_level > min_similarity_level or shortest_path_distance < max_distance:
                    if smallest_depth > word2_depth:
                        final_word = word2
                        # print "Replacing words: "+first_word+" to "+word2
                        # print "smallest_depth = " + str(smallest_depth) + " to " + str(word2_depth)
        return final_word

