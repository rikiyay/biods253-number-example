#!/usr/bin/env python3
# this program will eliminate all odd numbers from a specific file one at a time, creating a commit for each removal.

import sys
import subprocess

def eliminate_first_odd(fn):
    lines = open(fn, 'r').readlines()
    for lineno, line in enumerate(lines):
        int_value = int(line)
        is_odd = ((int(line) % 2) == 1)
        if is_odd:
            lines = lines[:lineno] + lines[lineno+1:]
            open(fn, 'w').write(''.join(lines))
            return int_value
    return None

def commit_change(fn, num):
    message = 'commit change for removal for %d' % num
    subprocess.run(['git', 'commit', '-m', message, fn])


if __name__ == '__main__':

    fn = sys.argv[1]

    while True:
        # 1. remove the first odd number in the file
        number_eliminated = eliminate_first_odd(fn)
        # if None is returned, there no odd numbers in the file
        if number_eliminated is None:
            break
        
        # 2. commit, into the current branch, the change removing one odd number
        commit_change(fn, number_eliminated)