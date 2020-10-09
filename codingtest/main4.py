class A:
    def __init__(self):
        print('A 1')
        print('A 2')

    @staticmethod
    def quack():
        print('a')


class B(A):
    def __init__(self):
        print('B 1')
        A.__init__(self)
        print('B 2')

    def quack(self):
        super().quack()
        print('i am b')


class C(A):
    def __init__(self):
        print('C 1')
        A.__init__(self)
        print('C 2')

    def quack(self):
        super().quack()
        print('i am c')


class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)

    pass


def solution():
    print(D.mro())
    d = D()
    # d.quack()
    answer = 4
    return answer


if __name__ == '__main__':
    print(solution())
