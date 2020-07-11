import pytest


@pytest.fixture(autouse=True)
def read(request):
    print("开始计算")
    yield request.param
    print("计算结束")
