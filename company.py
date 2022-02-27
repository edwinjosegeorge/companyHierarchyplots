from role import ROLE

root_name = input("Enter root role name : ")
ROOT = ROLE(root_name)
print(ROOT)

operation = 0
while True:
    try:
        print("\nOperations :")
        print("\t1. Add Sub Role")
        print("\t2. Exit")
        operation = int(input("Operation to be performed : "))
        if operation == 2:
            break

        if operation == 1:  # add sub role
            child_name = input("Enter sub role name : ")
            parent_name = input("Enter reporting to role name : ")
            ROOT.addSub(parent_name, child_name)

    except Exception as e:
        print(f"Error: {e}")
