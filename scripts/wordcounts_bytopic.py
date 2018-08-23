from mrjob.job import MRJob
from string import punctuation
from pathlib import Path
import os


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        file_path = os.environ['map_input_file']
        topic = file_path.split('.')[-1].split('/')[0]
        for word in line.split():
            word = word.strip(punctuation).lower()
            yield (topic + '_'+ word, 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    MRWordFreqCount.run()
