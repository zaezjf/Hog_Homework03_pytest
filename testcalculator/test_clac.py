import pytest
from testcalculator.calc import Calculator


class TestCalc:

    @pytest.mark.add
    def test_add(self, read):
        print(f"计算：{read[0]} + {read[1]}，预期结果为：{read[2]}")
        cal = Calculator()
        temp_result = cal.add(read[0], read[1])
        assert temp_result == read[2]

    @pytest.mark.red
    def test_red(self, read):
        print(f"计算：{read[0]} - {read[1]}，预期结果为：{read[3]}")
        cal = Calculator()
        temp_result = cal.red(read[0], read[1])
        assert temp_result == read[3]

    @pytest.mark.mul
    def test_mul(self, read):
        print(f"计算：{read[0]} * {read[1]}，预期结果为：{read[4]}")
        cal = Calculator()
        temp_result = cal.mul(read[0], read[1])
        assert temp_result == read[4]

    @pytest.mark.div
    def test_div(self, read):
        print(f"计算：{read[0]} ÷ {read[1]}，预期结果为：{read[5]}")
        cal = Calculator()
        temp_result = cal.div(read[0], read[1])
        assert temp_result == read[5]

