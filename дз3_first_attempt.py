class CountVectorizer():
    def __init__(self, *args):
        self.args = args

    def get_merged_list(self):
        mergedlist_ap = []
        mergedlist_ex = []
        for i in self.args:
            mergedlist_ap.append(i.lower().split())
            mergedlist_ex.extend(i.lower().split())
        return [mergedlist_ap, mergedlist_ex]

    def get_feature_names(self):
        wo = list(dict.fromkeys(test_data.get_merged_list()[1]))
        return wo  # wo dup

    def fit_transform(self):
        matrix = []
        for j in test_data.get_merged_list()[0]:
            counter = []
            for every in test_data.get_feature_names():
                counter.append(j.count(every))
            matrix.append(counter)
        return matrix

test_data = CountVectorizer('Crock Pot Pasta Never boil pasta again',
'Pasta Pomodoro Fresh ingredients Parmesan to taste')
print(test_data.get_feature_names())
print(test_data.fit_transform())

