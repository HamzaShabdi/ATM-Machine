Balance = 10000
copy = Balance
Deposit = 0
Withdrawal = 0
Exit = 0
add = 0
subtract = 0
User = ""
while User != PIN:

     User = int(input("Enter 4-digit Pin : "))

     if str(User) == PIN:
         print("You are allowed to see menu")
         break

     else:
         print("Wrong PIN Enter Again")

while choice != "4":
     print("ATM MENU")
     print("1.Check Balance")
     print("2.Deposit")
     print("3.Withdrawal")
     print("4.Exit")


     choice = input("Which Option Do U Want To Choose? : ")

     if choice == "1":
         print(f"Balance = {Balance}")

     elif choice == "2":
         print("You Chose Deposit")
         print("How much amount u want to deposit?")
         print(f"Balance - {copy}")
         amount = int(input("Enter Amount : "))
         print(f"{amount}")
         Balance = Balance + amount
         print(f"Balance - {Balance}")

     elif choice == "3":
         print("You Chose Withdrawal")
         print("How much amount u want to withdrawal?")
         print(f"Balance - {copy}")
         amount = int(input("Enter Amount : "))
         print(f"{amount}")
         Balance = Balance - amount
         print(f"Balance - {Balance}")

     else:
         print("Exit")
         exit()