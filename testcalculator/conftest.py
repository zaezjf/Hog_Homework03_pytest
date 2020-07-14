from typing import List

import pytest
import yaml


@pytest.fixture(scope='function')
def read(request):
    print("开始计算")
    yield request.param
    print("计算结束")


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        if 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        if 'env' in item.nodeid:
            item.add_marker(pytest.mark.env)


# parser: 用户命令行参数与ini文件值的解析器
def pytest_addoption(parser):
    mygroup = parser.getgroup("hog_homeworkk")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env (test, dev, st)'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    print("测试环境：" + myenv)
    if myenv == 'test':
        myenvpath = '../datas/test.yml'
    elif myenv == 'dev':
        myenvpath = '../datas/dev.yml'
    elif myenv == 'st':
        myenvpath = '../datas/st.yml'
    else:
        print("输入环境参数有误，使用默认环境:test")
        myenvpath = '../datas/test.yml'
    with open(myenvpath) as f:
        datas = yaml.safe_load(f)
    return myenv, datas
