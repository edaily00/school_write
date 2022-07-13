import json


class NobelData:

    def __init__(self):
        self._everything = []
        self._winner_list = []

        with open("nobels.json", "r") as infile:
            self._everything = json.load(infile)

    def search_nobel(self, year, category):
        for outer in self._everything:
            for deep in self._everything[outer]:
                if deep["year"] == year:
                    if deep["category"] == category:
                        for deeper in deep["laureates"]:
                            self._winner_list.append(deeper["surname"])

        for i in range(1, len(self._winner_list)):
            j = i
            while self._winner_list[j-1].lower() < self._winner_list[j] and j > 0:
                temp = self._winner_list[j-1]
                self._winner_list[j-1] = self._winner_list[j]
                self._winner_list[j] = temp
                j -= 1

        return self._winner_list




#data = NobelData()

#print(data.searching("2019", "physics"))


#print(data._everything["2021"])


#dictionary = {"apple": "fruit", "carrot": "veg"}

#print(dictionary["apple"])