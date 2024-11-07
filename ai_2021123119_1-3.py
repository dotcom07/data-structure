class Cal:
    def __init__(self, operand_1, operator, operand_2):
        self.operand_1 = operand_1
        self.operator = operator
        self.operand_2 = operand_2

    def plus_minus(self):
        if self.operator=="plus" :
            result = self.operand_1 + self.operand_2
        elif self.operator=="minus": 
            result = self.operand_1 - self.operand_2
        return result
    

n = int(input())
result_list = list()

for i in range(n) :
    operand_1, operator, operand_2 = input().split()
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)

    cal = Cal(operand_1, operator, operand_2)
    result = cal.plus_minus()
    result_list.append(result)


for result in result_list:
    print(result)