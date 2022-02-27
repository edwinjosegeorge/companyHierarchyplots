# Role Hierarchy
An sample python program that lets you view the hierarchy structure of an company. The hierarchy is based on roles, assigned to each individual.
An individual can hold only one role and report to only one supervisor.

![Structure preview](/images/structure_preview.png "A sample company structure")

## Reading the program
* File [role.py](/role.py) houses the properties of role, defined via class **ROLE**
* File [company.py](/company.py) houses the driver code.

## Running the program
```bash
python3 company.py
```

## Available methods/functions

1. Add Sub Role
2. Display Roles
3. Delete Role
4. Add User
5. Display Users
6. Display Users and Sub Users
7. Delete User
8. Number of users from top
9. Height of role hierarchy
10.Common boss of users
