from mrjob.job import MRJob, MRStep
import itertools


class friends_list(MRJob):

    def mapper1(self, _, line):
        f1 = int(line.split()[0])
        f2 = int(line.split()[1])
        yield (f1 ,f2)
        yield (f2, f1)

    def reducer1(self, key, values):
        f_list = list(values)
        yield (key, f_list)

    def mapper2(self, key, f_list):
        pairs = itertools.combinations(f_list,2)
        for i in pairs:
                yield (i , 1)

    def reducer2(self, key, values):
        yield (key , sum(values))


    def steps(self):
        return [MRStep(mapper=self.mapper1,
        reducer=self.reducer1),
        MRStep(mapper=self.mapper2,
        reducer=self.reducer2),]


if __name__ == '__main__':
    friends_list.run()
