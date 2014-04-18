from nltk.corpus import wordnet as wn
class AdjectivesCleaner(object):
    def __init__(self):
        self.__NOUN = 'n'
        self.__VERB = 'v'
        self.__ADJECTIVE = 'a'
        self.__ADJECTIVE_SATELLITE = 's'
        self.__ADVERB = 'r'

    def clean_adjectives(self, tokens):
        cleaned_tokens = []
        for token in tokens:
            token_as_nouns = self.__convert(token, self.__ADJECTIVE, self.__NOUN)
            if len(token_as_nouns) > 0:
                
                # print "Raplacing : " + str(token) + " to " + str(token_as_nouns[0][0])
                cleaned_tokens.append(token_as_nouns[0][0].lower())
            else:
                cleaned_tokens.append(token)
        return cleaned_tokens
 

    def __convert(self, word, from_pos, to_pos):
        synsets = wn.synsets(word, pos=from_pos)
         
        if not synsets:
            return []
         
        lemmas = [l for s in synsets
        for l in s.lemmas
        if s.name.split('.')[1] == from_pos
        or from_pos in (self.__ADJECTIVE, self.__ADJECTIVE_SATELLITE)
        and s.name.split('.')[1] in (self.__ADJECTIVE, self.__ADJECTIVE_SATELLITE)]
         
        derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in lemmas]
         
        related_noun_lemmas = [l for drf in derivationally_related_forms
        for l in drf[1]
        if l.synset.name.split('.')[1] == to_pos
        or to_pos in (self.__ADJECTIVE, self.__ADJECTIVE_SATELLITE)
        and l.synset.name.split('.')[1] in (self.__ADJECTIVE, self.__ADJECTIVE_SATELLITE)]
         
        words = [l.name for l in related_noun_lemmas]
        len_words = len(words)         
        result = [(w, float(words.count(w))/len_words) for w in set(words)]
        result.sort(key=lambda w: -w[1])
         
        # return all the possibilities sorted by probability
        return result
