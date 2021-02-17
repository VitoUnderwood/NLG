# -*- coding:utf-8 -*-

import argparse

def print_hi(name):
    print(f'Hi, {name}')

def argsParser():
    """
    -h, --help show help messages
    """
    parser = argparse.ArgumentParser(description='自然语言生成工具')
    #=============================================================
    parser.add_argument('task', metavar='N', type=int, nargs='+', help='具体的生成任务')
    # =============================================================
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = argsParser()

    print(args.task)

    print_hi('PyCharm')

