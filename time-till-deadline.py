from datetime import datetime

user_input = input("Enter your goal and deadline \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.today()
# calculation
print(f"Dear user, the time remaining is: {deadline_date - today}")

