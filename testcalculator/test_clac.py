import sys

import pytest
import yaml
from pythoncode.calc import Calculator
sys.path.append('..')
with open("./data.yaml", encoding='utf-8') as f:
    c = yaml.safe_load(f)
    ids_add = [f"{c[i][0]} + {c[i][1]}" for i in range(len(c))]
    ids_sub = [f"{c[i][0]} - {c[i][1]}" for i in range(len(c))]
    ids_mul = [f"{c[i][0]} × {c[i][1]}" for i in range(len(c))]
    ids_div = [f"{c[i][0]} ÷ {c[i][1]}" for i in range(len(c))]


def isstr(a, b):
    if isinstance(a, str):
        return 0
    if isinstance(b, str):
        return 0


class CheckEnv:

    def check_env(self, cmdoption):
        print("测试环境验证")
        env, datas = cmdoption
        ip = datas['env']['ip']
        port = datas['env']['port']
        url = 'http://' + str(ip) + ":" + str(port)
        print(f"环境：{env}，地址：{url}")


class TestCalc:

    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    # @pytest.mark.xfail(reason="deliberate fail")
    @pytest.mark.parametrize('read', c, ids=ids_add, indirect=True)
    def check_add(self, read):
        print(f"计算：{read[0]} + {read[1]}，预期结果为：{read[2]}")
        if isstr(read[0], read[1]) == 0:
            raise TypeError
        else:
            temp_result = self.cal.add(read[0], read[1])
            # assert temp_result == read[2]
            assert True

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.parametrize('read', c, ids=ids_sub, indirect=True)
    def check_sub(self, read):
        print(f"计算：{read[0]} - {read[1]}，预期结果为：{read[3]}")
        if isstr(read[0], read[1]) == 0:
            raise TypeError
        else:
            temp_result = self.cal.sub(read[0], read[1])
            assert temp_result == read[3]

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    @pytest.mark.parametrize('read', c, ids=ids_mul, indirect=True)
    def check_mul(self, read):
        print(f"计算：{read[0]} * {read[1]}，预期结果为：{read[4]}")
        if isstr(read[0], read[1]) == 0:
            raise TypeError
        else:
            temp_result = self.cal.mul(read[0], read[1])
            assert temp_result == read[4]

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.parametrize('read', c, ids=ids_div, indirect=True)
    def check_div(self, read):
        print(f"计算：{read[0]} ÷ {read[1]}，预期结果为：{read[5]}")
        if isstr(read[0], read[1]) == 0:
            raise TypeError
        elif read[1] == 0:
            raise ZeroDivisionError
        else:
            temp_result = self.cal.div(read[0], read[1])
            assert temp_result == read[5]

