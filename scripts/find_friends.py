import json
from mrjob.job import MRJob



class MRFindFriends(MRJob):

    def mapper(self, _, line):
        yield ("{}_{}".format(section, stemmed_wrd), 1)

    def combiner(self, key, counts):
        yield (key, sum(counts))

    def reducer(self, key, counts):
        yield (key, sum(counts))

if __name__ == '__main__':
    MRFindFriends.run()
