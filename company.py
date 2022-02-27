from role import ROLE

root_name = input("Enter root role name : ")
ROOT = ROLE(root_name)
print(ROOT)

operation = 0
while True:
    try:
        print("\nOperations :")
        print("\t1. Add Sub Role")
        print("\t2. Display Roles")
        print("\t3. Delete Role")
        print("\t4. Exit")
        operation = int(input("Operation to be performed : "))
        if operation == 4:
            break

        elif operation == 1:  # add sub role
            child_name = input("Enter sub role name : ")
            parent_name = input("Enter reporting to role name : ")
            ROOT.addSub(parent_name, child_name)

        elif operation == 2:  # display roles
            for role in ROOT:
                print(role, end=" ")
            print()

        elif operation == 3:  # delete a role
            child_name = input("Enter the role to be deleted : ")
            parent_name = input("Enter the role to be transferred : ")
            ROOT.deleteAndTransfer(child_name, parent_name)

    except Exception as e:
        print(f"Error: {e}")
