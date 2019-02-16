user_operation = input("Operation (you can type addition, subtraction, multiplication, or division) - ")
user_num_one = input("Number one (in numbers) - ")
user_num_two = input("Number two - ")

if user_operation == "addition":
    print float(user_num_one) + float(user_num_two)
elif user_operation == "subtraction":
    print float(user_num_one) - float(user_num_two)
elif user_operation == "multiplication":
    print float(user_num_one) * float(user_num_two)
elif user_operation == "division":
    print float(user_num_one) / float(user_num_two)
