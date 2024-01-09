# -*- coding: utf-8 -*-
from Types import DataType


class GoodGraders:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count = 0
        for student, subjects in self.data.items():
            all_good_graders = all(score >= 76 for _, score in subjects)
        
        if all_good_graders:
            count += 1
        return count
