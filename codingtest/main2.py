from datetime import datetime


def gen(str: str):
    yield str


def gen2(str: str):
    return str


def solution():
    str: str = '/Users/siner/PycharmProjects/codingtest/venv/bin/python /Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevd.py --multiproc --qt-support=auto --client 127.0.0.1 --port 61201 --file /Users/siner/PycharmProjects/codingtest/main1.py Connected to pydev debugger (build 193.7288.30)'
    start_time = datetime.now()
    print(next(gen(str)))
    end_time = datetime.now()
    print(end_time - start_time)

    start_time_2 = datetime.now()
    end_time_2 = datetime.now()
    print(end_time_2 - start_time_2)
    return 'end'


if __name__ == '__main__':
    print(solution())
