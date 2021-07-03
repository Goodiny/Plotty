from __future__ import annotations
import sys

from app.plotty.plotty import Plotty, Item, ItemSet
from app.beat_board.beat import BeatBoard


class TimeLine(BeatBoard):

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int):
        self._length = length

    @property
    def scene_pull(self) -> Plotty:
        return self._scene_pull

    @scene_pull.setter
    def scene_pull(self, scene_pull: Plotty):
        self._scene_pull = scene_pull

    @property
    def beat_bord(self) -> Plotty:
        return self._beat_board

    @beat_bord.setter
    def beat_bord(self, beat_bord: Plotty) -> None:
        self._beat_board = beat_bord

    def show(self) -> None:
        print()


if __name__ == "__main__":
    print("Hallo")
    # print(sys.version)
