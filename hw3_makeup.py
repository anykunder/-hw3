class CountVectorizer():
    def __init__(self, *corpus):
        self.corpus = corpus

    def get_feature_names(self):
        mergedlist_ex = []
        for i in self.corpus:
            mergedlist_ex.extend(i.lower().split())
        wo = list(dict.fromkeys(mergedlist_ex))
        return wo  # wo dup

    def fit_transform(self):
        mergedlist_ap = []
        for k in self.corpus:
            mergedlist_ap.append(k.lower().split())
        matrix = []
        for j in mergedlist_ap:
            counter = []
            for every in self.get_feature_names():
                counter.append(j.count(every))
            matrix.append(counter)
        return matrix


if __name__ == '__main__':
    corpus = ('Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste')
    vectorizer = CountVectorizer(*corpus)
    print(vectorizer.get_feature_names())
    print(vectorizer.fit_transform())
