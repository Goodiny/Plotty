from __future__ import annotations

from typing import List, Tuple, Union


class ItemSet(object):
    __items: List[Item] = []

    def __init__(self, items: Union[List[Item], None] = None):
        if items is not None:
            if len(items) != 0:
                for i in range(0, len(items)):
                    items[i].num = str(i + 1)
            self.__items = items
            self.__count = len(self.__items)
        else:
            self.__items = []
            self.__count = 0

    def add_item(self, value: Union[Item, str], it: Union[IType, str] = None) -> None:
        """
        Examle it = itemSet()
        it.add_item("Hallo", "Diolog")
        it.add_item(Action("He is walking"))
        :param value:
        :param it:
        :return:
        """
        self.__items.append(self.create_item(value, it))
        self.__count += 1

    def create_item(self, value: Union[Item, str], it: Union[IType, str, None] = None) -> Item:
        if isinstance(value, Item):  # value is Item
            value.num = str(self.__count + 1)
            return value
        elif isinstance(value, str):  # value is str
            return Item.create_item(value, str(self.__count + 1), it)
        raise ValueError

    def find_item(self, value: Union[Item, str]) -> Tuple[int, Item]:
        index = 0
        for item_local in self.__items:
            if isinstance(value, Item):
                if item_local == value:
                    return index, item_local
            elif isinstance(value, str):
                if item_local.num == value:
                    return index, item_local
            index += 1
        raise ValueError

    def find_type(self, it: Union[IType, str]) -> Tuple[Item]:
        items_list: List[Item] = []
        if isinstance(it, str):
            if it.upper() in IType.__dict__["_member_names_"]:
                it = IType.__dict__["_member_map_"][it.upper()]
            else:
                raise ValueError
        for item_local in self.__items:
            if item_local.get_it() == it:
                if item_local not in items_list:
                    items_list.append(item_local)
        return tuple(items_list)

    def update_item(self, find: Union[Item, str], value: Union[Item, str],
                    it: Union[IType, str, None] = None) -> None:
        index, item_last = self.find_item(find)
        if isinstance(value, Item):
            value.num = item_last.num
            self.__items[index] = value
        elif isinstance(value, str):
            self.__items[index] = Item.create_item(value, item_last.num, it)
        else:
            raise ValueError

    def remove_item(self, value: Union[Item, str]) -> None:
        index, find = self.find_item(value)
        self.__items.remove(find)
        if self.__count - 1 != index + 1:
            for i in range(index, self.__count - 1):
                self.__items[i].num = str(i + 1)
        self.__count -= 1

    def show_item(self, value: Union[Tuple[str, Item], Item, str]):
        index, item = self.find_item(value)
        print(f"{item.num}. {item.desc}")

    def show_all_item(self):
        index = 0
        for item in self.__items:
            print(f"{item.num}. {item}")
            index += 1

    @property
    def count(self) -> int:
        return self.__count

    @property
    def items(self) -> List[Item]:
        return self.__items

    @items.setter
    def items(self, value: List[Item]) -> None:
        if isinstance(value, List):
            self.__items = value
        raise ValueError


if __name__ == "__main__":
    items: List[Item] = [Action('Вечереет', "1")]
    i = Item.create_item("Питер", it="character")
    items.append(item)
    item = Diolog('Привет', "2f")
    items.append(item)
    print(items)

    print(item == Diolog("Привет", "2"))

    item_set = ItemSet(items)
    item_set.add_item(Action("Что-то случилось"))
    item_set.show_all_item()
    print(item_set.items, item_set.items[1])
    item_set.update_item("1", Action("Было уже поздно"))
    item_set.show_all_item()
    print()
    item_set.remove_item("1")
    item_set.show_all_item()
    print()
    item_set.add_item("Начало преступления", "shot")
    item_set.add_item("Кто-то выходит из леса и идет в сторону деревни", "action")
    item_set.add_item("Остоновливается смотрит по сторонам и идёт дальше", "action")
    item_set.add_item("Кто-то выходит из леса всед за ним и идёт в сторону деревни", "action")
    item_set.add_item("Начало преступления два", "shot")
    item_set.add_item("У одного из них отваливается рука в которой нож", "action")
    item_set.add_item("Вася", "character")

    item_set.show_all_item()
    # item_set.remove_item("4")
    print()
    item_set.show_all_item()

    print(item_set.find_type("character"))
