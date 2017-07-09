#!/usr/bin/env python3

import os
import re
import subprocess


def main():
    git_cmd = "git log"
    result = subprocess.getoutput(git_cmd)
    print("*******************1")
    print(result)
    commit_id = re.search(r'commit\s(.*)', result).group(1)
    print("*******************2")
    print(commit_id)
    print(len(commit_id))


if __name__ == '__main__':
    main()