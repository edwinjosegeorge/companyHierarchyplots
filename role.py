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
        self.child = list()

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
        parent.child.append(child)
