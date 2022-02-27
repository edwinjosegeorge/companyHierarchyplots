class ROLE_ITERATE:
    """
    Iterable version of class ROLE
    """

    def __init__(self, RoleObj):
        self.lst = [RoleObj]

    def __next__(self):
        if len(self.lst) == 0:
            raise StopIteration
        nxt = self.lst[0]
        self.lst.remove(nxt)
        self.lst.extend(nxt.child)
        return nxt


class ROLE:
    """
    Class for handling roles
    """

    def __init__(self, name: str):
        """Constructor to initialize role name"""
        self.name = name
        self.parent = None
        self.child = list()
        self.userlist = set()
        self.userMaps = dict()  # to be shared by all objects

    def __str__(self) -> str:
        return self.name

    def __iter__(self):
        return ROLE_ITERATE(self)

    def findRole(self, name: str):
        """Search and return role object identified by name in sub tree"""
        for role in self:
            if role.name == name:
                return role
        return None

    def addSub(self, parent_name: str, child_name: str) -> None:
        """Add new sub role to parent in this subtree. Creates new child"""

        parent = self.findRole(parent_name)
        child = self.findRole(child_name)
        if parent is None:
            raise ValueError(f"No role {parent_name} found")
        if child is not None:
            raise ValueError(f"Role {child_name} pre-exist")

        child = ROLE(child_name)
        child.parent = parent
        child.userMaps = self.userMaps  # shallow copy ensures all node share one table
        parent.child.append(child)

    def deleteAndTransfer(self, del_name: str, tran_name: str) -> None:
        """Delete child and transfter its properties to parent"""

        if del_name == tran_name:
            raise ValueError("Deleted role and transfered role are identical")

        transfer = self.findRole(tran_name)
        delRole = self.findRole(del_name)
        if transfer is None:
            raise ValueError(f"No role {tran_name} found")
        if delRole is None:
            raise ValueError(f"No role {del_name} found")
        if delRole.parent is None:
            raise ValueError(f"Cannot delete ROOT role {del_name}")

        # is role to be transferd a sub role of deleted role?
        # if yes, transfer propeties to parent of deleted role
        for role in delRole:
            if role == transfer:
                transfer = delRole.parent
                break

        delRole.parent.child.remove(delRole)
        transfer.child.extend(delRole.child)

        # update on usernames, transfer to new role
        for username in delRole.userlist:
            self.userMaps[username] = transfer
            transfer.userlist.add(username)

    def addUser(self, username: str, rolename: str):
        """adds a new user to a specific role"""

        if username in self.userMaps:
            raise ValueError(f"user {username} cannot have more than one role")

        newrole = self.findRole(rolename)
        if newrole is None:
            raise ValueError(f"No role {rolename} found")

        newrole.userlist.add(username)
        self.userMaps[username] = newrole
