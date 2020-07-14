import pytest
import yaml
from testcalculator.calc import Calculator

c = yaml.safe_load(open("./data.yaml", encoding='utf-8'))


def isstr(self, a, b):
    if isinstance(a, str):
        return 0
    if isinstance(b, str):
        return 0


class TestCalc:

    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.parametrize('read', c, ids=[f"{c[i][0]} + {c[i][1]}" for i in range(len(c))], indirect=True)
    @pytest.mark.add
    def test_add(self, read):
        print(f"计算：{read[0]} + {read[1]}，预期结果为：{read[2]}")
        temp_result = self.cal.add(read[0], read[1])
        assert temp_result == read[2]

    @pytest.mark.parametrize('read', c, ids=[f"{c[i][0]} - {c[i][1]}" for i in range(len(c))], indirect=True)
    @pytest.mark.red
    def test_red(self, read):
        print(f"计算：{read[0]} - {read[1]}，预期结果为：{read[3]}")
        temp_result = self.cal.red(read[0], read[1])
        assert temp_result == read[3]

    @pytest.mark.parametrize('read', c, ids=[f"{c[i][0]} * {c[i][1]}" for i in range(len(c))], indirect=True)
    @pytest.mark.mul
    def test_mul(self, read):
        print(f"计算：{read[0]} * {read[1]}，预期结果为：{read[4]}")
        temp_result = self.cal.mul(read[0], read[1])
        assert temp_result == read[4]

    @pytest.mark.parametrize('read', c, ids=[f"{c[i][0]} / {c[i][1]}" for i in range(len(c))], indirect=True)
    @pytest.mark.div
    def test_div(self, read):
        print(f"计算：{read[0]} ÷ {read[1]}，预期结果为：{read[5]}")
        temp_result = self.cal.div(read[0], read[1])
        assert temp_result == read[5]

