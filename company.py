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
        print("\t4. Add User")
        print("\t5. Display Users")
        print("\t6. Display Users and Sub Users")
        print("\t7. Delete User")
        print("\t8. Number of users from top")
        print("\t9. Exit")
        operation = int(input("Operation to be performed : "))
        if operation == 9:
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

        elif operation == 4:  # Add new user
            username = input("Enter User name : ")
            rolename = input("Enter Role : ")
            ROOT.addUser(username, rolename)

        elif operation == 5:  # Display Users
            for username in ROOT.userMaps:
                print(username, "-", ROOT.userMaps[username])

        elif operation == 6:  # Display Users and sub users
            for username in ROOT.userMaps:
                print(username, "-", end=" ")
                headRole = ROOT.userMaps[username]
                for subrole in headRole:
                    if subrole == headRole:
                        continue
                    for users in subrole.userlist:
                        print(users, end=" ")
                print()

        elif operation == 7:  # Delete username
            username = input("Enter username to be deleted : ")
            ROOT.deleteUser(username)

        elif operation == 8:  # Height of user from top level
            username = input("Enter the user name : ")
            levelRoles = [ROOT]
            height = 0
            found = False
            while len(levelRoles) != 0 and not found:
                newLevel = list()
                for role in levelRoles:
                    if username in role.userlist:
                        found = True
                        break
                    newLevel.extend(role.child)
                else:
                    height += 1
                    levelRoles = newLevel
            if found:
                print(f"Number of users from top : {height}")
            else:
                print("Username not found")

    except Exception as e:
        print(f"Error: {e}")
