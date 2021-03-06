import sys
from logging import exception

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


class CheckEnv:

    @pytest.mark.run(order=1)
    def check_env(self, cmdoption):
        if cmdoption is None:
            print("环境参数错误，可选参数：test, dev, st")
            assert False
        print("测试环境验证")
        env, data = cmdoption
        ip = data['env']['ip']
        port = data['env']['port']
        url = 'http://' + str(ip) + ":" + str(port)
        print(f"环境：{env}，地址：{url}")


class TestCalc:

    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(name="add")
    # @pytest.mark.xfail(reason="deliberate fail")
    @pytest.mark.parametrize('read', c, ids=ids_add, indirect=True)
    def check_add(self, read):
        print(f"计算：{read[0]} + {read[1]}，预期结果为：{read[2]}")
        try:
            temp_result = self.cal.add(read[0], read[1])
            assert temp_result == read[2]
        except Exception as e:
            print(e)
            assert False

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.parametrize('read', c, ids=ids_sub, indirect=True)
    def check_sub(self, read):
        print(f"计算：{read[0]} - {read[1]}，预期结果为：{read[3]}")
        try:
            temp_result = self.cal.sub(read[0], read[1])
            assert temp_result == read[3]
        except Exception as e:
            print(e)
            assert False

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(name="mul")
    @pytest.mark.parametrize('read', c, ids=ids_mul, indirect=True)
    def check_mul(self, read):
        print(f"计算：{read[0]} * {read[1]}，预期结果为：{read[4]}")
        try:
            temp_result = self.cal.mul(read[0], read[1])
            assert temp_result == read[4]
        except Exception as e:
            print(e)
            assert False

    @pytest.mark.run(order=5)
    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.parametrize('read', c, ids=ids_div, indirect=True)
    def check_div(self, read):
        print(f"计算：{read[0]} ÷ {read[1]}，预期结果为：{read[5]}")
        try:
            temp_result = self.cal.div(read[0], read[1])
            assert temp_result == read[5]
        except Exception as e:
            print(e)
            assert False

