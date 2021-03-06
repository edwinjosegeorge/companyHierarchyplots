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

    def deleteUser(self, username: str):
        """Deletes username from the tree"""
        if username not in self.userMaps:
            return
        role = self.userMaps[username]
        if username in role.userlist:
            role.userlist.remove(username)
        del self.userMaps[username]

    def commonBoss(self, user1: str, user2: str) -> list:
        """Return a list of top common boss of two users """

        if user1 not in self.userMaps:
            raise ValueError(f"Username {user1} not found")
        if user2 not in self.userMaps:
            raise ValueError(f"Username {user2} not found")

        # top most common boss of any valid users is the user at root note
        root = self
        while root.parent is not None:
            root = root.parent
        if len(root.userlist) == 0:
            return [f'no users at role {root}']
        return root.userlist

        # alternate long appraoch!
        # map role-1 to top
        role1 = self.userMaps[user1]
        role1_route = list()
        while role1 is not None:
            role1_route.add(role1)
            role1 = role1.parent
        role1_route.reverse()

        # map role-2 to top
        role2 = self.userMaps[user2]
        role2_route = list()
        while role2 is not None:
            role2_route.add(role2)
            role2 = role2.parent
        role2_route.reverse()

        # find common points
        common = set(role1_route).intersection(set(role2_route))
        for topCommon in role1_route:
            if topCommon in common:
                if len(topCommon.userlist) == 0:
                    return [f'no users at role {topCommon}']
                return topCommon.userlist
        return ['no common boss']
