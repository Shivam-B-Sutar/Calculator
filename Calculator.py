print("Welcome to the Calculator All-in-one\n")
barrier="----------------------------------------------------------"
def addition():
    print('Welcome to the Addition\n')
    addnum1=float(input("Enter the first number:"))
    addnum2=float(input("Enter the second number:"))
    sum=addnum1+addnum2
    print(f"{addnum1} + {addnum2} = {sum}")
    print(barrier)

def subtraction():
    print("Welcome to the Substraction\n")
    subnum1=float(input("Enter the first number:"))
    subnum2=float(input("Enter the second number:"))
    diff=subnum1-subnum2
    print(f"{subnum1} - {subnum2} = {diff}")
    print(barrier)

def multiplication():
    print("Welcome to the Multiplication\n")
    mulnum1=float(input("Enter the first number:"))
    mulnum2=float(input("Enter the second number:"))
    totalmulti=mulnum1*mulnum2
    print(f"{mulnum1} x {mulnum2} = {totalmulti}")
    print(barrier)

def division():
    print("Welcome to the Division")
    divnum1=float(input("Enter the first number:"))
    divnum2=float(input("Enter the second number:"))
    totaldiv=divnum1/divnum2
    print(f"{divnum1} / {divnum2} = {totaldiv}")
    print(barrier)

def stardelta():
    print("Welcome to the Star to Delta & Delta to star connected netork conversion\n")
    barrier = "-------------------------------------------------------------\n"
    print(barrier)

    select = int(input("Enter '1' for Star to Delta Conversion, enter '2' for Delta to Star Conversion:"))

    if select == 1:
        select = int(input("Enter '1' for Star to Delta Conversion, enter '2' for Delta to Star Conversion:"))

    if select == 1:
        print(barrier)
        print("You have selected Star to Delta Conversion\n")
        Ra = float(input("Enter the value of Ra:"))
        Rb = float(input("Enter the value of Rb:"))
        Rc = float(input("Enter the value of Rc:"))
        print(barrier)
        print("Calculating...\n")
        R1 = (Ra * Rb + Rb * Rc + Rc * Ra) / Ra
        R2 = (Ra * Rb + Rb * Rc + Rc * Ra) / Rb
        R3 = (Ra * Rb + Rb * Rc + Rc * Ra) / Rc
        print("The converted Delta resistances are as follows:\n")
        print(f"R1 = {R1:.2f} ohm")
        print(f"R2 = {R2:.2f} ohm")
        print(f"R3 = {R3:.2f} ohm")
        print(barrier)
    elif select == 2:
        print(barrier)
        print("You have selected Delta to Star Conversion\n")
        R1 = float(input("Enter the value of R1:"))
        R2 = float(input("Enter the value of R2:"))
        R3 = float(input("Enter the value of R3:"))
        print(barrier)
        print("Calculating...\n")
        Ra = (R1 * R2) / (R1 + R2 + R3)
        Rb = (R2 * R3) / (R1 + R2 + R3)
        Rc = (R3 * R1) / (R1 + R2 + R3)
        print("The converted Star resistances are as follows:\n")
        print(f"Ra = {Ra:.2f} ohm")
        print(f"Rb = {Rb:.2f} ohm")
        print(f"Rc = {Rc:.2f} ohm")
        print(barrier)
    else:
        print("Invalid selection! Please run the program again and select either '1' or '2'.")
        print(barrier)

def percentage():
    print("Welcome to the Percentage or Marks Calculator\n")
    total=float(input("Enter the total Total Number:"))
    obtained=float(input("Enter the Obtained Number:"))
    percent=(obtained/total)*100
    print(f"The percentage is {percent:.2f}%")
    print(barrier)

fuctions={
    "Addition": "1",
    "Subtraction": "2",
    "Multiplication": "3",
    "Division": "4",
    "Star-Delta Convertor": "5",
    "Percentage Calculator": "6"
}
for key, value in fuctions.items():
    print(f"Enter '{value}' for {key}")
select=int(input("Select the operation you want to perform:"))

if select==1:
    addition()
elif select==2:
    subtraction()
elif select==3:
    multiplication()
elif select==4:
    division()
elif select==5:
    stardelta()
elif select==6:
    percentage()
else:
    print("Selection error\n")