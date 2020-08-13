def thisList(num1):
    for char in num1:
        if char in this_list:
            print("Its available!")
            print(this_list.index(char))
        else:
            print("Error")
this_list=["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
print(this_list)
print(len(this_list))
num2=input("Enter your word:")
thisList(num2)

