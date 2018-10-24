#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import os
import shutil


def remove_pycache():
    cwd = os.getcwd()
    for dirpath, dirnames, _ in os.walk(cwd, followlinks=True):
        for dirname in dirnames:
            if dirname == "__pycache__":
                pycache_dir_path = os.path.join(dirpath, dirname)
                if os.path.isdir(pycache_dir_path):
                    shutil.rmtree(pycache_dir_path)


if __name__ == "__main__":
    pass
