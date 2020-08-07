import os
from os import listdir
from os.path import isfile, join
import re
import sys


PACKAGE_NAME_PATTERN = "^(.+)-\d+"
WORKDIR = ''
DESTDIR = ''


def get_package_name(package):
    p = re.compile(PACKAGE_NAME_PATTERN)
    name = p.match(package)
    if name:
        return name.group(1)
    return None


def pre_check():
    global WORKDIR
    global DESTDIR
    if len(sys.argv) < 2:
        print(f'Usage: {os.path.basename(__file__)}  source_dir  [destination_dir]')
        exit(1)
    WORKDIR = sys.argv[1]
    DESTDIR = sys.argv[2] if len(sys.argv) >= 3 else WORKDIR
    if not os.path.exists(WORKDIR):
        print(f'Error: {WORKDIR} does not exists')
        exit(1)
    if not os.path.exists(DESTDIR):
        res = input(f'Notice: {DESTDIR} does not exists, create it [y/N]? ')
        if str(res).lower() != 'y':
            exit(1)
        else:
            os.mkdir(DESTDIR)
            print(f'Created dir {DESTDIR}')
            print('=' * 15)


def move_files():
    count = 0
    onlyfiles = [f for f in listdir(WORKDIR) if isfile(join(WORKDIR, f))]
    for f in onlyfiles:
        pkg_name = get_package_name(f)
        if pkg_name:
            pkg_source = join(WORKDIR, f)
            pkg_path = join(DESTDIR, pkg_name)
            if not os.path.exists(pkg_path):
                os.mkdir(pkg_path)
                print(f'Created {pkg_path}')
            os.system(f'mv -f {pkg_source} {pkg_path}')
            print(f'Moved file {f} to {pkg_path}')
            print('=' * 15)
            count += 1
    print(f'Done! {count} files sorted in {DESTDIR}')


def main():
    pre_check()
    move_files()


if __name__ == '__main__':
    main()
