import re
import sys
from glob import glob
from multiprocessing.pool import ThreadPool
from subprocess import call


def parse_threads():
    threads = 1  # default value, if there is no argument passed
    for arg in sys.argv:
        if arg.startswith('--threads='):
            threads = int(re.search(r'\d+', arg).group())
            sys.argv.remove(arg)
            break
    return threads


def parse_features():
    return glob('features/*.feature')  # collect all ".feature" files


def run_parallel_feature(feature):
    argline = ''
    for arg in sys.argv[1:]:
        argline = argline + ' ' + arg
    command = f'behave {feature} {argline}'
    r = call(command, shell=True)
    status = 'Passed' if r == 0 else 'Failed'
    print(f'{feature}: {status}')


def main():
    thread_pool = ThreadPool(parse_threads())
    features = parse_features()
    thread_pool.map(run_parallel_feature, features)


if __name__ == '__main__':
    sys.exit(main())
