from abc import ABC, abstractmethod

class Role(ABC):
    @abstractmethod
    def permissions(self):
        pass


class EmployeeRole(Role):
    def permissions(self):
        return ["read_documents"]


class ManagerRole(Role):
    def permissions(self):
        return ["read_documents", "approve_budget"]


class AdminRole(Role):
    def permissions(self):
        return ["read_documents", "approve_budget", "modify_users"]


class User:
    def __init__(self, name, role: Role):
        self.name = name
        self.role = role

    def get_permissions(self):
        return self.role.permissions()


# Testing
manager = User("Alice", ManagerRole())
admin = User("Bob", AdminRole())

print(manager.get_permissions())
print(admin.get_permissions())