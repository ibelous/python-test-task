import argparse


def flag():
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='input parameter N')

    n = parser.parse_args().N
    if not n % 2 == 0:
        raise argparse.ArgumentError

    Flag = '#'*(3*n+2)+'\n'+int(n/2)*('#'+' '*3*n+'#'+'\n')
    for i in range(int(n/2), 0, -1):
        Flag += '#' + ' '*(n+i-1) + '*' + 'o'*2*(int(n/2) - i) + '*' + ' '*(n+i-1) + '#' + '\n'

    for i in range(1, int(n/2)+1):
        Flag += '#' + ' '*(n+i-1) + '*' + 'o'*2*(int(n/2) - i) + '*' + ' '*(n+i-1) + '#' + '\n'

    Flag += int(n/2)*('#'+' '*3*n+'#'+'\n')+'#'*(3*n+2)+'\n'
    print(Flag)


if __name__ == "__main__":
    flag()
