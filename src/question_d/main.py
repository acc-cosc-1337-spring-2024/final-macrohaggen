#add import
from question_d import create_multiplication_table, display_multiplication_table
i = 0
listy = []
while i != 3:
    i = int(input("Multiplication Table Menu\n1-Create Multiplication Table\n2-Display Multiplication Table\n3-Exit\n"))
    if i == 1:
        listy = create_multiplication_table()
        print("Table Created!")
        continue
    if i == 2:
        print(display_multiplication_table(listy))
        continue
    

