class Student:
    def __init__(self, PIB):
        self.name = PIB
        self.marks = {}

    def add_mark(self, subject, *marks):
        self.marks[subject] = marks

    def average_mark(self, subject):
        marks = self.marks[subject]
        return sum(marks) / len(marks)

    def __str__(self):
        result = f'{self.name} marks: {self.marks}\n'
        for subject in self.marks:
            result += f'Average mark for {subject}: {self.average_mark(subject)}'
        return result
    
s1 = Student('Pro John Ok')
s1.add_mark('DVV', 5, 4, 3, 2, 1)
s1.add_mark('ML', 3, 4, 3, 3, 1)
s1.add_mark('F', 5, 5, 5, 5)
print(s1)