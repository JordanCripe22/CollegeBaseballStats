
class DataPoint:

    def __init__(self, level, text):
        self.level = level
        self.text = text

    def show(self):
        print("lvl", end=": ")
        print(self.level, end=", ")
        print(self.text)


    def cleanText(self):
        self.text = self.text.replace(u'\xa0', ' ')

        if " III" in self.text or " IV" in self.text or " II" in self.text or " Jr." in self.text:
            self.text = self.text.replace(" III", "").replace(" IV", "").replace(" II", "").replace(" Jr.", "")

        return self
