class Pr:
    def __init__(self, text):
        self.text = text


class ch(Pr):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number


parent_obj = Pr('Da eto ono')
print(parent_obj.text)

child_obj = ch('This lab number', 8)
print(child_obj.text, child_obj.number)

