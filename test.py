# class School():
#     def wear_uniform(self):
#         return "В школе все должны носить форму"
    
# School()

# class University():
#     def wear_uniform(self):
#         return "Можно носить любую одежду, если ты студент"

    
# student1 = School()
# student2 = University()
# print(student1.wear_uniform())
# print(student2.wear_uniform())

class BankAccount():
    def __init__(self, balance):
        self.balance = 0

    def deposit(self, money):
        self.balance += money
        return self.balance

    def withdraw(self, money):
        if self.balance < 0: 
            print("Сумма не может быть меньше нулья")
        self.balance -= money
        return self.balance

Timur = BankAccount(0)

print(Timur.deposit(1000))
print(Timur.withdraw(100))

