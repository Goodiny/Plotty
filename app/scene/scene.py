from __future__ import annotations

from typing import List, Union, Tuple


class Header(object):
    # loc_type = {"INT", "EXT", "NAT", "ИНТ", "ЭКТ", "НАТ"}
    # loc_time = {"DAY",
    #             "NIGHT",
    #             "EVENING",
    #             "AFTERNOON",
    #             "ДЕНЬ",
    #             "НОЧЬ",
    #             "ВЕЧЕР",
    #             "УТРО",
    #             "ЧУТЬ ПОЗЖЕ",
    #             "ЧЕРЕЗ ПЯТЬ МИНУТ",
    #             "ЗАВТРА",
    #             "ПРОШЛЫМ ВЕЧЕРОМ"}

    def __init__(self, value: str = "", *, l_type: str = "", loc: str = "", l_time: str = ""):
        if value != "":
            self.type = value.split('. ')[0].upper()
            self.location = value.split('. ')[1].split(' - ')[0].upper()
            self.time = value.split(' - ')[1].upper()
        else:
            self.type = l_type.upper()
            self.location = loc.upper()
            self.time = l_time.upper()

    def __str__(self) -> str:
        return f"{self.type}. {self.location} - {self.time}"


class Scene(object):
    __itemSet: ItemSet = ItemSet()
    __characterList: List[Character] = []

    def __init__(self, header: Header, *, name: str = '', items: ItemSet = ItemSet()):
        self._header = header
        self._name = name
        self.__itemSet = items

    def add_item(self, value: Union[Item, str], it: Union[IType, str] = None):
        self.__itemSet.add_item(value, it)

    def set_header(self, header: Header):
        self._header = header

    def get_header(self) -> Header:
        return self._header

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def get_chars(self) -> Tuple[Item]:

        return self.__itemSet.find_type("character")

    def show_items(self):
        self.__itemSet.show_all_item()

    def show_header(self):
        print(self._header)

    @property
    def itemSet(self) -> ItemSet:
        return self.__itemSet

    @itemSet.setter
    def itemSet(self, value: ItemSet):
        self.__itemSet = value


if __name__ == "__main__":
    h = Header(l_type="инт", loc="комната", l_time="вечер")
    s = Header("инт. комната - день")

    print(h, s, sep='\n')

    items: List[Item] = [Action('Вечереет', "1")]
    item = Item.create_item("Питер", it="character")
    items.append(item)
    item = Diolog('Привет', "2f")
    items.append(item)

    scene = Scene(Header("инт. комната - утро"), items=ItemSet(items))
    scene.add_item(Action("Что-то случилось"))
    scene.show_items()
    print(scene.itemSet.items, scene.itemSet.items[1])
    scene.itemSet.update_item("1", Action("Было уже поздно"))
    scene.show_items()
    print()
    scene.itemSet.remove_item("1")
    scene.show_items()
    print()
    scene.add_item("Начало преступления", "shot")
    scene.add_item("Кто-то выходит из леса и идет в сторону деревни", "action")
    scene.add_item("Остоновливается смотрит по сторонам и идёт дальше", "action")
    scene.add_item("Кто-то выходит из леса всед за ним и идёт в сторону деревни", "action")
    scene.add_item("Начало преступления два", "shot")
    scene.add_item("У одного из них отваливается рука в которой нож", "action")
    scene.add_item("Вася", "character")

    scene.show_items()
    # item_set.remove_item("4")
    print()
    scene.show_items()

    print(scene.itemSet.find_type("character"))
