from src.GoodGraders import GoodGraders
from src.Types import DataType
import pytest


class TestGoodGraders:

    @pytest.fixture()
    def input_data(self) -> DataType:
        data: DataType = {
            "Студент1": [
                ("предмет1", 79),
                ("предмет2", 90),
            ],
            "Студент2": [
                ("предмет1", 92),
                ("предмет2", 100),
            ],
            "Студент3": [
                ("предмет1", 76),
                ("предмет2", 61),
            ],
        }
        return data

    def test_find_good_graders(self, input_data: DataType) -> None:
        finder = GoodGraders(input_data)
        result = finder.calc()
        assert result == 2

    def test_find_no_good_graders(self, input_data: DataType) -> None:
        data_without_one_hundred: DataType = {
            "Студент1": [
                ("предмет1", 61),
                ("предмет2", 63),
            ],
            "Студент2": [
                ("предмет1", 70),
                ("предмет2", 75),
            ],
        }

        finder = GoodGraders(data_without_one_hundred)
        result = finder.calc()
        assert result == 0