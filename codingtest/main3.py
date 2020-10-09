from sys import getrefcount


class GrandParent(object):

    @classmethod
    def some(cls):
        print('asdf')


class Parent(GrandParent):
    pass


class Child(Parent):
    pass


def solution():
    answer = 3
    print(getrefcount(GrandParent()))
    grand = GrandParent()
    grand2 = GrandParent()
    print(getrefcount(grand))
    print(getrefcount(grand2))
    print(isinstance(grand, GrandParent))
    print(issubclass(Parent, GrandParent))
    return answer


if __name__ == '__main__':
    print(solution())
