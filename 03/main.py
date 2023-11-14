"""
Файл для 2 дз
"""


class CustomList(list):
    """Updating list"""

    def __init__(self, lst):
        """Initialized"""
        super().__init__()
        self.lst = lst

    def __add__(self, other):
        """+"""
        if isinstance(other, CustomList):
            app1_list = other.lst.copy()
        else:
            app1_list = other.copy()
        app2_list = self.lst.copy()
        if len(app1_list) < len(app2_list):
            app1_list += [0 for i in range(-len(app1_list) + len(app2_list))]
        if len(app1_list) > len(app2_list):
            app1_list += [0 for i in range(len(app1_list) - len(app2_list))]
        return CustomList([app1_list[i] + app2_list[i] for i in range(len(app1_list))])

    def __radd__(self, other):
        """+"""
        app1_list = other.copy()
        app2_list = self.lst.copy()
        if len(app1_list) < len(app2_list):
            app1_list += [0 for i in range(-len(app1_list) + len(app2_list))]
        if len(app1_list) > len(app2_list):
            app1_list += [0 for i in range(len(app1_list) - len(app2_list))]
        return CustomList([app1_list[i] + app2_list[i] for i in range(len(app1_list))])

    def __sub__(self, other):
        """-"""
        if isinstance(other, CustomList):
            app1_list = other.lst.copy()
        else:
            app1_list = other.copy()
        app2_list = self.lst.copy()
        if len(app1_list) < len(app2_list):
            app1_list += [0] * (len(app2_list) - len(app1_list))
        if len(app1_list) > len(app2_list):
            app2_list += [0] * (len(app1_list) - len(app2_list))
        return CustomList([app2_list[i] - app1_list[i] for i in range(len(app1_list))])

    def __rsub__(self, other):
        """-"""
        app1_list = other.copy()
        app2_list = self.lst.copy()
        if len(app1_list) < len(app2_list):
            app1_list += [0 for i in range(-len(app1_list) + len(app2_list))]
        if len(app1_list) > len(app2_list):
            app2_list += [0 for i in range(len(app1_list) - len(app2_list))]
        return CustomList([app1_list[i] - app2_list[i] for i in range(len(app1_list))])

    def __lt__(self, other):
        """<"""
        if isinstance(other, CustomList):
            return sum(self.lst) < sum(other.lst)
        return NotImplemented

    def __le__(self, other):
        """<="""
        if isinstance(other, CustomList):
            return sum(self.lst) <= sum(other.lst)
        return NotImplemented

    def __eq__(self, other):
        """=="""
        if isinstance(other, CustomList):
            return sum(self.lst) == sum(other.lst)
        return NotImplemented

    def __ne__(self, other):
        """!="""
        if isinstance(other, CustomList):
            return sum(self.lst) != sum(other.lst)
        return NotImplemented

    def __gt__(self, other):
        """>"""
        if isinstance(other, CustomList):
            return sum(self.lst) > sum(other.lst)
        return NotImplemented

    def __ge__(self, other):
        """>="""
        if isinstance(other, CustomList):
            return sum(self.lst) >= sum(other.lst)
        return NotImplemented

    def __str__(self):
        return f"CustomList: {self.lst}, sum: {sum(self.lst)}"


lst1 = CustomList([1, 2, 3, 4, 5])
lst2 = CustomList([5, 4, 6])
