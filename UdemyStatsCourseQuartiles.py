
samplesCourse = [9, 10, 10, 11, 13, 15, 16, 19, 19, 21, 23, 28, 30, 33, 34, 36, 44, 45, 47, 60]

class sampleSet:
    def __init__(self, sampleList):
        self.sampleList = sampleList
        self.interList = list(sampleList) # interList is sampleList alias; alias used to maintain integrity of original sampleList

    def find_median(self):
        self.median = 0

        if len(self.sampleList) % 2 == 0:
            # find median for even-numbered sample list length
            self.medL = self.interList[int(len(self.interList)/2)-1]
            self.medU = self.interList[int(len(self.interList)/2)]
            self.median = (self.medL + self.medU)/2

        else:
            # find median for odd-numbered sample list length
            self.median = self.interList[int((len(self.interList)-1)/2)]
        return self.median

    def find_1stQuartile(self, median):
        self.lower50List = []
        self.Q1 = 0

        # break out lower 50 percentile from sampleList
        if len(self.interList) % 2 == 0:
            self.lower50List = self.interList[:int(len(self.interList)/2)]
        else:
            # drop median to make list ready to divide into 50 percentiles
            self.interList.pop(interList.index(self.median))
            self.lower50List = self.interList[:int(len(self.interList)/2)]

        # find 1st quartile (median of lower 50 percentiles)
        if len(self.lower50List) % 2 == 0:
            self.Q1L = self.lower50List[int(len(self.lower50List)/2)-1]
            self.Q1U = self.lower50List[int(len(self.lower50List)/2)]
            self.Q1 = (self.Q1L + self.Q1U)/2

        else:
            self.Q1 = self.lower50List[int((len(self.lower50List)-1)/2)]

        return self.Q1

    def find_3rdQuartile(self, median):
        self.upper50List = []
        self.Q3 = 0

        # break out upper 50 percentile from sampleList
        if len(self.sampleList) % 2 == 0:
            self.upper50List = self.interList[int(len(self.interList)/2):]
        else:
            self.interList.pop(interList.index(self.median))
            self.upper50List = self.interList[int(len(self.interList)/2):]

        # find 3rd quartile (median of upper 50 percentiles)
        if len(self.upper50List) % 2 == 0:
            self.Q3L = self.upper50List[int(len(self.upper50List)/2)-1]
            self.Q3U = self.upper50List[int(len(self.upper50List)/2)]
            self.Q3 = (self.Q3L + self.Q3U)/2

        else:
            self.Q3 = self.upper50List[int((len(self.upper50List)-1)/2)]

        return self.Q3

    def find_InterQuartileRange(self, Q1, Q3):
        self.IQR = self.Q3 - self.Q1
        return self.IQR

    def find_UpperFence(self, Q3, IQR):
        self.fence = self.Q3 + 1.5 * self.IQR
        return self.fence

samples = sampleSet(samplesCourse)
median = samples.find_median()
firstQ = samples.find_1stQuartile(median)
thirdQ = samples.find_3rdQuartile(median)
iqr = samples.find_InterQuartileRange(firstQ, thirdQ)
fence = samples.find_UpperFence(thirdQ, iqr)

print("Median is: ", median)
print("1st quartile is: ", firstQ)
print("3rd quartile is: ", thirdQ)
print("IQR is: ", iqr)
print("Upper fence is: ", fence)
