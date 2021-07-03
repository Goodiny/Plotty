from __future__ import annotations
from enum import Enum
from typing import Union, Tuple


IType = Enum("IType", names="GENERAL ACTION SHOT CHARACTER PARENTHESES DIOLOG TRANSITION")


class Item(object):
    """

    """
    it: IType = IType.GENERAL

    def __init__(self, desc: Union[Tuple[str, str], str], num: str = ""):
        """

        :param desc:
        :param num:
        """
        if isinstance(desc, Tuple):
            self._desc = desc[1]
            self._num = desc[0]
        elif isinstance(desc, str):
            self._desc = desc
            self._num = num
        else:
            raise ValueError

    def get_it(self) -> IType:
        """

        :return:
        """
        return self.it

    def show(self):
        print(self)

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, value: str):
        self._desc = value

    @property
    def num(self) -> str:
        return self._num

    @num.setter
    def num(self, value: str):
        self._num = value

    def __eq__(self, other: Item) -> bool:
        return True if self._num == other.num and \
                       self._desc == other.desc and \
                       self.get_it() == other.get_it() else False

    def __repr__(self) -> str:
        return f"{self.__class__}.{self._desc}"

    def __str__(self) -> str:
        return f"{self.get_it().name}.{self._desc}"

    @classmethod
    def create_item(cls, desc: str, num: str = "", it: Union[IType, str] = None):
        if isinstance(it, str):
            if it.upper() in IType.__dict__["_member_names_"]:
                it = IType.__dict__["_member_map_"][it.upper()]
            else:
                raise ValueError

        if it is None or it.name == "GENERAL":
            return Item(desc, num)
        elif it.name == "ACTION":
            return Action(desc, num)
        elif it.name == "SHOT":
            return Shot(desc, num)
        elif it.name == "CHARACTER":
            return Character(desc, num)
        elif it.name == "PARENTHESIS":
            return Parenthesis(desc, num)
        elif it.name == "DIOLOG":
            return Diolog(desc, num)
        elif it.name == "TRANSITION":
            return Transition(desc, num)

        raise ValueError


class Action(Item):
    it = IType.ACTION


class Shot(Item):
    it = IType.SHOT

    def __init__(self, desc: Union[Tuple[str, str], str], num: str = ""):
        if isinstance(desc, Tuple):
            l_desc = desc[1]
            l_num = desc[0]
        elif isinstance(desc, str):
            l_desc = desc
            l_num = num
        else:
            raise ValueError
        super(Shot, self).__init__(l_desc.upper() if l_desc[-1] == ":" else l_desc.upper() + ":",
                                   l_num)
        self._desc = l_desc.upper() if l_desc[-1] == ":" else l_desc.upper() + ":"
        self._num = l_num

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, value: str):
        self._desc = value.upper() if value[-1] == ":" else value.upper() + ":"


class Character(Item):
    it = IType.CHARACTER

    def __init__(self, desc: Union[Tuple[str, str], str], num: str = ""):
        if isinstance(desc, Tuple):
            l_desc = desc[1]
            l_num = desc[0]
        elif isinstance(desc, str):
            l_desc = desc
            l_num = num
        else:
            raise ValueError

        super(Character, self).__init__(l_desc.upper(), num)
        self._desc = l_desc.upper()
        self._num = l_num

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, value: str):
        self._desc = value.upper()


class Parenthesis(Item):
    it = IType.PARENTHESES

    def __init__(self, desc: Union[Tuple[str, str], str], num: str = ""):
        if isinstance(desc, Tuple):
            l_desc = desc[1]
            l_num = desc[0]
        elif isinstance(desc, str):
            l_desc = desc
            l_num = num
        else:
            raise ValueError

        if l_desc[0] != "(":
            l_desc = "(" + l_desc
        if desc[-1] != ")":
            l_desc += ")"

        if l_desc[1] == "(" and l_desc[0] == "(":
            l_desc = "(" + l_desc[2:]
        if l_desc[-2] == ")" and l_desc[-1] == ")":
            l_desc = l_desc[:-2] + ")"

        super(Parenthesis, self).__init__(l_desc.lower())
        self._desc = l_desc.lower()
        self._num = l_num

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, value: str):
        if value[0] != "(":
            value = "(" + value
        if value[-1] != ")":
            value += ")"

        if value[1] == "(" and value[0] == "(":
            value = "(" + value[2:]
        if value[-2] == ")" and value[-1] == ")":
            value = value[:-2] + ")"

        self._desc = value.lower()


class Diolog(Item):
    it = IType.DIOLOG


class Transition(Item):
    it = IType.TRANSITION

    def __init__(self, desc: Union[Tuple[str, str], str], num: str = ""):
        if isinstance(desc, Tuple):
            l_desc = desc[1]
            l_num = desc[0]
        elif isinstance(desc, str):
            l_desc = desc
            l_num = num
        else:
            raise ValueError
        super(Transition, self).__init__(l_desc.upper() if l_desc[-1] == ":" else l_desc.upper() + ":",
                                         l_num)
        self._desc = l_desc.upper() if l_desc[-1] == ":" else l_desc.upper() + ":"
        self._num = l_num

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, value: str):
        self._desc = value.upper() + ":"


if __name__ == '__main__':

    i = Item('Hali', "1")
    print(i == Item(('1', "Hali")))
    print(i.get_it())

    Color = Enum("Color", names="RED GREEN BLUE")

    print(Color)

    print(i.get_it().name == "GENERAL")
    # print("general")

    cr = Item.create_item("Hallo", "1", "action")
    cr.show()

    a = Action('Hallo', "1")
    a.desc = "Непосильная ноша"
    a.show()
    s = Shot('наезд', "2")
    s.show()
    c = Character("Вася", "3")
    c.show()
    p = Parenthesis("тихо", "4")
    p.show()
    d = Diolog("Привет как дела?", "5")
    d.show()
    t = Transition('зтм', "6")
    t.show()

    print(type(cr), type(i), type(a), type(s))
