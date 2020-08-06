import os
from os import walk, listdir
from os.path import isfile, join
import re
import sys

if len(sys.argv) < 2:
    print(f'Usage: {os.path.basename(__file__)}  source_dir  [destination_dir]')
    exit(1)
package_name_pattern = "^(.+)-\d+"
workdir = sys.argv[1]
destdir = sys.argv[2] if len(sys.argv) >= 3 else workdir

if not os.path.exists(workdir):
    print(f'Error: {workdir} does not exists')
    exit(1)

if not os.path.exists(destdir):
    res = input(f'Notice: {destdir} does not exists, create it [y/N]? ')
    if str(res).lower() != 'y':
        exit(1)
    else:
        os.mkdir(destdir)
        print(f'Created dir {destdir}')
        print('=' * 15)

def get_package_name(package):
    p = re.compile(package_name_pattern)
    name = p.match(package)
    if name:
        return name.group(1)
    return None
count = 0
onlyfiles = [f for f in listdir(workdir) if isfile(join(workdir, f))]
for f in onlyfiles:
    pkg_name = get_package_name(f)
    if pkg_name:
        pkg_source = join(workdir, f)
        pkg_path = join(destdir, pkg_name)
        if not os.path.exists(pkg_path):
            os.mkdir(pkg_path)
            print(f'Created {pkg_path}')
        os.system(f'mv -f {pkg_source} {pkg_path}')
        print(f'Moved file {f} to {pkg_path}')
        print('=' * 15)
        count += 1
print(f'Done! {count} files sorted in {destdir}')

        
