# -*- coding: utf-8 -*-

import argparse
from . import cli


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--bfp', nargs='+')
    parser.add_argument('-s', '--stock', nargs='+')
    parser.add_argument('-r', '--realtime', nargs='+')
    args = parser.parse_args()

    if args.bfp:
        cli.best_four_point.run(args.bfp)
    elif args.stock:
        cli.stock.run(args.stock)
    elif args.realtime:
        cli.realtime.run(args.realtime)
