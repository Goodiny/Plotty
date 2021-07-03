from __future__ import annotations

from app.plotty.plotty import Plotty, Item, ItemSet


class Beat(Item):
    """
    A short description.

    A bit longer description.

    Args:
        variable (type): description

    Returns:
        type: description

    Raises:
        Exception: description

    """

    def __init__(self, title: str = '', description: str = '',
                 page: int = 0):
        super(Beat, self).__init__(title, description)
        self._page = page

    @property
    def page(self) -> int:
        return self._page

    @page.setter
    def page(self, page: int):
        self._page = page

    def is_structure_point(self) -> bool:
        return False

    def show(self) -> None:
        print(str(self) + "\n[basic_beat]")

    def __str__(self) -> str:
        return f"{self._title}" \
               f"{' | ' + str(self._page) + ' page' if self._page != 0 else ''}\n" \
               f"{self._description}"


class StructureBeat(Beat):
    def is_structure_point(self) -> bool:
        return True

    def show(self) -> None:
        print(str(self) + "\n[structure_point]")


class BeatBoard(ItemSet):
    def add(self, beat: Plotty) -> None:
        if isinstance(beat, Beat) or isinstance(beat, StructureBeat):
            if beat not in self._children:
                self._children.append(beat)
                beat.parent = self
            else:
                raise ValueError
        else:
            raise TypeError

    def remove(self, beat: Plotty) -> None:
        if isinstance(beat, Beat) or isinstance(beat, StructureBeat):
            self._children.remove(beat)
            beat.parent = None
        else:
            raise TypeError


if __name__ == "__main__":
    item = StructureBeat()
    item.title = 'Начало истории'
    item.description = 'Когда-то давно началась эта история'
    item.edit("Новое начало", "Да так уж и быть")
    item.page = 2
    item.show()
    print(type(item.get()))

    items = BeatBoard()
    items.add(item)
    items.add(Beat("Продолжение", "Все нарасталоч то по накатанной", 5))
    items.show()
