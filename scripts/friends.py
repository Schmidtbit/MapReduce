from mrjob.job import MRJob, MRStep
import itertools


class friends_list(MRJob):

    def mapper(self, _, line):
        # turn each row into integer pairs
        clean = [int(x) for x in line.strip().split(' ')]
        f1 = clean[0]
        f2 = clean[1]
        yield (f1 ,f2)
        yield (f2, f1)

    def reducer(self, key, values):
        # this reducer just makes a list of all the values with that same key
        yield (key, list(values))

    def mapper2(self, key, f_list):
        # make all possible friend combinations
        pairs = itertools.combinations(f_list,2)
        for i in pairs:
            yield (i , 1)
        # reassign value to 0 if already friends
        for f in f_list:
            yield (key, f), 0

    def reducer2(self, key, values):
        # count how many friends each pair has in common
        count = 0
        for flag in values:
            if flag == 0:
                # if friend pair is already friends, discard
                return
            count+= flag
        yield (key , count)

    def mapper3(self, key, values):
        # reformat the friend pairs and values
        yield key[0], (key[1], values)
        yield key[1], (key[0], values)

    def reducer3(self, key, values):
        # recommend the user to friend the user with the most connections
        f2 = max(values, key=lambda x : x[1])[0]
        yield key, f2

    def steps(self):
        return [MRStep(mapper=self.mapper,
        reducer=self.reducer),
        MRStep(mapper=self.mapper2,
        reducer=self.reducer2),
        MRStep(mapper=self.mapper3,
        reducer=self.reducer3)]


if __name__ == '__main__':
    friends_list.run()
