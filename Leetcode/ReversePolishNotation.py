operations_list = {
   "+": lambda x, y: x + y,
   "*": lambda x, y: x * y,
   "/": lambda x, y: int(y / x)
}


rpn = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
operand_list = []
for i in rpn:
   if i not in ["*", "+", "/"]:
       operand_list.append(int(i))
   else:
       operand_list.append(operations_list[i](operand_list.pop(), operand_list.pop()))
print(operand_list.pop())