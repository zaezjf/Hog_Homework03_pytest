import pytest
import yaml


@pytest.fixture(params=(yaml.safe_load(open("./data.yaml", encoding='utf-8'))), autouse=True)
def read(request):
    print("开始计算")
    # print(type(request.param))
    yield request.param
    print("计算结束")
