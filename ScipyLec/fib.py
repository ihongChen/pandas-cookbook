import argparse


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # print(list(fib(10)))
    parser = argparse.ArgumentParser(description='fibonocci list with yield')
    parser.add_argument('--input', type=int, dest='inputnum')
    args = parser.parse_args()

    print(list(fib(args.inputnum)))
