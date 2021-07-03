"""
Plotty, Item, ItemSet

"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Plotty(ABC):
    """
    Базовый интерфейс объявляет общие операции как для простых, так и для
    сложных объектов структуры
    """

    @property
    def parent(self) -> Plotty:
        return self._parent

    @parent.setter
    def parent(self, parent: Plotty):
        """
        При необходимости базовый класс может объявить интерфейс для
        установки и получения родителя компонента в древовидной структуре. Он
        также может предоставить некоторую реализацию по умолчанию для этих
        компонентов

        :param parent:
        :return:
        """

        self._parent = parent

    """
    В некоторых случая целесообразно определить операции управления потомками
    прямо в базовом классе Компонент. Таким образом, вам не нужно будет
    предоставлять конкретные классы компонентов клиентскому коду, даже во время
    сборки дерева объектов. Недостаток такого подхода в том, что эти методы
    будут пустыми для компонентов уровня листа.
    """

    def add(self, plot: Plotty) -> None:
        pass

    def remove(self, plot: Plotty) -> None:
        pass

    def is_composite(self) -> bool:
        """
        Позволяет клиентскому коду понять, может ли компонент иметь вложенные
        объекты.
        """

        return False

    @abstractmethod
    def get(self) -> Plotty:
        pass

    @abstractmethod
    def show(self) -> None:
        pass


class Item(Plotty):

    def __init__(self, title: str = '', description: str = ''):
        self._title = title
        self._description = description

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    def edit(self, title: str, description: str) -> None:
        self._title = title
        self._description = description

    def get(self) -> Plotty:
        return self

    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self._title}\n{self._description}"


class ItemSet(Plotty):
    def __init__(self) -> None:
        self._children: List[Plotty] = []

    @property
    def children(self) -> List[Plotty]:
        return self._children

    def add(self, plot: Plotty) -> None:
        if plot not in self._children:
            self._children.append(plot)
            plot.parent = self
        else:
            raise ValueError

    def remove(self, plot: Plotty) -> None:
        self._children.remove(plot)
        plot.parent = None

    def is_composite(self) -> bool:
        return True

    def get(self) -> Plotty:
        return self

    def show(self) -> None:
        i = 1
        for item in self._children:
            print(str(i), end='. ')
            item.show()
            i += 1

    def __str__(self) -> str:
        result = ""
        i = 1
        for item in self._children:
            result += str(i) + '. ' + str(item) + "\n"
            i += 1
        return result


if __name__ == "__main__":
    item = Item()
    item.title = 'Начало истории'
    item.description = 'Когда-то давно началась эта история'
    item.edit("Новое начало", "Да так уж и быть")
    # item.page = 2
    item.show()
    print(type(item.get()))

    items = ItemSet()
    items.add(item)
    items.add(Item("Продолжение", "Все нарасталоч то по накатанной"))
    items.show()
