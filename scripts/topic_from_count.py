import os
from mrjob.job import MRJob
from mrjob.step import MRStep
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import json
from string import punctuation

sno = SnowballStemmer('english')

class WordCountByTopic(MRJob):

    # Mapper 1: word count by section
    def mapper1(self, _, line):
        d = json.loads(line)
        topic = d['section_name']
        for art_text in d['content']:
            art_text = art_text.strip().encode("ascii", "ignore").decode('utf-8').lower()
            translator = art_text.maketrans('', '', punctuation)
            clean_text = art_text.translate(translator)
            for word in word_tokenize(clean_text):
                wrd = sno.stem(word)
                yield (topic + "_" + wrd, 1)

    def combiner1(self, key, counts):
        yield (key, sum(counts))

    def reducer1(self, key, counts):
        yield (key, sum(counts))

    # Mapper 2: For each word, what topic appears most frequent?
    def mapper2(self, key, count):
        topic, word = key.split('_')
        yield word, (topic, count)

    def combiner2(self, word, values):
        yield word, max(values, key=lambda x: x[1])

    def reducer2(self, word, values):
        yield word, max(values, key=lambda x: x[1])[0]

    def steps(self):
        return [
            MRStep(mapper=self.mapper1,
                   combiner=self.combiner1,
                   reducer=self.reducer1),

            MRStep(mapper=self.mapper2,
                   combiner=self.combiner2,
                   reducer=self.reducer2)
        ]

if __name__ == '__main__':
    WordCountByTopic.run()
