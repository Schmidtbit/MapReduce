import json
from string import punctuation
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import os
from mrjob.job import MRJob

sno = SnowballStemmer('english')


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        d = json.loads(line)
        section = d['section_name']
        for line in d['content']:
            line = line.strip().encode('ascii','ignore').decode('utf-8').lower()
            translator = line.maketrans('', '', punctuation)
            new_line = line.translate(translator)
            for word in word_tokenize(new_line):
                    stemmed_wrd = sno.stem(word)
                    # Total word count
                    #yield("SUM_{}".format(stemmed_wrd), 1)
                    # Word count by section name
                    yield ("{}_{}".format(section, stemmed_wrd), 1)

    def combiner(self, key, counts):
        yield (key, sum(counts))

    def reducer(self, key, counts):
        yield (key, sum(counts))

if __name__ == '__main__':
    MRWordFreqCount.run()
