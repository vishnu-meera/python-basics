class LotteryPlayer:
    
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def total(self):
        return sum(self.grades)


# player1 = LotteryPlayer("Vishnu",(18,18,19,30))
# player2 = LotteryPlayer("Meera",(20,30,31,30))

# print(player1.name)
# print(player1.total())

# print(player2.name)
# print(player2.total())

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    
    def student_marks_avg(self):
        return sum(self.marks)/len(self.marks)
    
    #@classmethod
    @staticmethod
    def go_to_school():
        print("Go to school")

# anna = Student("vishnu","navodhaya")
# anna.marks.append(92)
# anna.marks.append(81)
# anna.marks.append(99)
# anna.marks.append(98)
# anna.marks.append(96)
# anna.go_to_school()
# Student.go_to_school()
# # print(anna.name)
# # print(anna.school)
# # print(anna.student_marks_avg())

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        newStore = Store(store.name + " - franchise")
        newStore.items = store.items
        return newStore
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name,store.stock_price())


store  = Store ("test")
store2 = Store ("Amazon")

Store.franchise(store)
Store.franchise(store2)

Store.store_details(store)
Store.store_details(store)